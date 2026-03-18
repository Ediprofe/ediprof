<?php

namespace App\Services\Content;

use App\Models\AssessmentQuestion;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Support\Collection;
use Illuminate\Support\Str;

class AssessmentQuestionDuplicateDetectionService
{
    public function __construct(
        private readonly AssessmentQuestionFingerprintService $fingerprintService,
    ) {}

    /**
     * @param  array<string, mixed>  $draft
     * @return array<string, mixed>
     */
    public function annotateDraft(array $draft, ?int $subjectId = null): array
    {
        $draftQuestions = collect((array) ($draft['questions'] ?? []))
            ->filter(fn ($question) => is_array($question))
            ->values();

        if ($draftQuestions->isEmpty()) {
            $draft['duplicate_summary'] = [
                'new_questions' => 0,
                'exact_duplicates' => 0,
                'questions_with_similar_candidates' => 0,
                'savable_questions' => 0,
            ];

            return $draft;
        }

        $fingerprints = $draftQuestions
            ->mapWithKeys(fn (array $question): array => [
                (string) ($question['id'] ?? Str::uuid()) => $this->fingerprintService->exactFingerprintFromDraftQuestion($question),
            ]);

        $candidates = $this->candidatePool($subjectId);
        $exactMatches = AssessmentQuestion::query()
            ->with(['template'])
            ->whereIn('exact_fingerprint', $fingerprints->values()->filter()->all())
            ->get()
            ->groupBy('exact_fingerprint');

        $questionsWithSuggestions = 0;
        $exactDuplicates = 0;

        $annotatedQuestions = $draftQuestions
            ->map(function (array $question) use ($fingerprints, $exactMatches, $candidates, &$questionsWithSuggestions, &$exactDuplicates): array {
                $questionId = (string) ($question['id'] ?? Str::uuid());
                $fingerprint = $fingerprints->get($questionId, '');
                /** @var AssessmentQuestion|null $exactMatch */
                $exactMatch = $exactMatches->get($fingerprint)?->first();

                $similarCandidates = $this->findSimilarCandidates(
                    $this->fingerprintService->searchDocumentFromDraftQuestion($question),
                    $candidates,
                    $fingerprint
                );

                if ($exactMatch instanceof AssessmentQuestion) {
                    $exactDuplicates++;
                } elseif ($similarCandidates !== []) {
                    $questionsWithSuggestions++;
                }

                return array_merge($question, [
                    'duplicate_status' => $exactMatch instanceof AssessmentQuestion
                        ? 'exact_duplicate'
                        : ($similarCandidates !== [] ? 'similar_candidates' : 'new'),
                    'save_decision' => $exactMatch instanceof AssessmentQuestion ? 'skip_duplicate' : 'new',
                    'exact_fingerprint' => $fingerprint,
                    'exact_match' => $exactMatch ? $this->serializeCandidate($exactMatch) : null,
                    'similar_candidates' => $similarCandidates,
                ]);
            })
            ->values()
            ->all();

        $draft['questions'] = $annotatedQuestions;
        $draft['duplicate_summary'] = [
            'new_questions' => count($annotatedQuestions) - $exactDuplicates,
            'exact_duplicates' => $exactDuplicates,
            'questions_with_similar_candidates' => $questionsWithSuggestions,
            'savable_questions' => count(array_filter(
                $annotatedQuestions,
                fn (array $question): bool => ($question['save_decision'] ?? 'new') === 'new'
            )),
        ];

        return $draft;
    }

    /**
     * @param  array<string, mixed>  $draft
     * @return array<string, mixed>
     */
    public function extractSavableDraft(array $draft): array
    {
        $questions = collect((array) ($draft['questions'] ?? []))
            ->filter(fn ($question) => is_array($question) && (($question['save_decision'] ?? 'new') === 'new'))
            ->map(function (array $question): array {
                unset(
                    $question['duplicate_status'],
                    $question['save_decision'],
                    $question['exact_fingerprint'],
                    $question['exact_match'],
                    $question['similar_candidates']
                );

                return $question;
            })
            ->values();

        $questionIds = $questions->pluck('id')->filter()->values();

        $links = collect((array) ($draft['question_context_links'] ?? []))
            ->filter(fn ($link) => is_array($link) && $questionIds->contains($link['question_external_id'] ?? null))
            ->values();

        $contextIds = $links->pluck('context_external_id')->filter()->unique()->values();

        $contexts = collect((array) ($draft['contexts'] ?? []))
            ->filter(fn ($context) => is_array($context) && $contextIds->contains($context['external_id'] ?? null))
            ->values()
            ->all();

        return [
            'schema' => (string) ($draft['schema'] ?? 'ai_question_draft_v1'),
            'contexts' => $contexts,
            'questions' => $questions->all(),
            'question_context_links' => $links->all(),
        ];
    }

    /**
     * @return Collection<int, AssessmentQuestion>
     */
    private function candidatePool(?int $subjectId = null): Collection
    {
        return AssessmentQuestion::query()
            ->with(['template'])
            ->when($subjectId, fn (Builder $query, int $resolvedSubjectId): Builder => $query->where('subject_id', $resolvedSubjectId))
            ->whereNotNull('search_document')
            ->latest('updated_at')
            ->limit(500)
            ->get();
    }

    /**
     * @return array<int, array<string, mixed>>
     */
    private function findSimilarCandidates(string $searchDocument, Collection $candidates, string $exactFingerprint): array
    {
        $needleTokens = $this->tokens($searchDocument);

        if ($needleTokens === []) {
            return [];
        }

        return $candidates
            ->filter(fn (AssessmentQuestion $candidate): bool => $candidate->exact_fingerprint !== $exactFingerprint)
            ->map(function (AssessmentQuestion $candidate) use ($needleTokens): ?array {
                $candidateTokens = $this->tokens((string) ($candidate->search_document ?? ''));
                if ($candidateTokens === []) {
                    return null;
                }

                $score = $this->similarity($needleTokens, $candidateTokens);

                if ($score < 0.32) {
                    return null;
                }

                return array_merge($this->serializeCandidate($candidate), [
                    'similarity' => round($score, 2),
                ]);
            })
            ->filter()
            ->sortByDesc('similarity')
            ->take(3)
            ->values()
            ->all();
    }

    /**
     * @param  array<int, string>  $left
     * @param  array<int, string>  $right
     */
    private function similarity(array $left, array $right): float
    {
        $left = array_values(array_unique($left));
        $right = array_values(array_unique($right));

        $intersection = count(array_intersect($left, $right));
        $denominator = count($left) + count($right);

        if ($denominator === 0) {
            return 0.0;
        }

        return (2 * $intersection) / $denominator;
    }

    /**
     * @return array<int, string>
     */
    private function tokens(string $searchDocument): array
    {
        $stopWords = [
            'para', 'como', 'esta', 'este', 'estos', 'estas', 'desde', 'entre', 'sobre', 'cuando', 'donde',
            'porque', 'cual', 'cuales', 'solo', 'pero', 'cada', 'tiene', 'todas', 'todos', 'luego', 'segun',
            'debe', 'puede', 'hacer', 'hace', 'sera', 'eran', 'sobre', 'ante', 'tras', 'del', 'las', 'los',
            'una', 'uno', 'unos', 'unas', 'que', 'por', 'con', 'sin', 'más', 'mas', 'muy', 'sus', 'esa',
            'ese', 'eso', 'aqui', 'alli', 'ella', 'ellos', 'ellas',
        ];

        return collect(explode(' ', Str::of($searchDocument)->ascii()->lower()->squish()->value()))
            ->map(fn (string $token): string => trim($token))
            ->filter(fn (string $token): bool => strlen($token) >= 4)
            ->reject(fn (string $token): bool => in_array($token, $stopWords, true))
            ->unique()
            ->values()
            ->all();
    }

    /**
     * @return array<string, mixed>
     */
    private function serializeCandidate(AssessmentQuestion $candidate): array
    {
        return [
            'question_id' => $candidate->id,
            'external_id' => $candidate->external_id,
            'block_id' => $candidate->template_id,
            'block_title' => $candidate->template?->title,
            'subject_label' => $candidate->subject_label,
            'unit_label' => $candidate->unit_label,
            'origin_label' => $candidate->origin_label,
            'editorial_status' => $candidate->editorial_status,
            'stem_excerpt' => Str::limit(
                Str::of(strip_tags((string) ($candidate->stem_html ?: $candidate->stem_mdx)))->squish()->value(),
                180
            ),
        ];
    }
}
