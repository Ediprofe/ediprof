<?php

namespace App\Http\Controllers\Web\Admin;

use App\Filament\Pages\ImportAiQuestionDraft;
use App\Http\Controllers\Controller;
use App\Models\AssessmentTemplate;
use App\Services\Content\RichContentPayloadNormalizer;
use Illuminate\Http\Request;
use Inertia\Inertia;
use Inertia\Response;

class AssessmentDraftPreviewController extends Controller
{
    public function __invoke(Request $request, AssessmentTemplate $template, RichContentPayloadNormalizer $normalizer): Response
    {
        $user = $request->user();

        abort_unless($user && $user->isAdmin() && $user->member_status !== 'blocked', 403);

        $template->load([
            'contexts' => fn ($query) => $query->where('is_active', true)->orderBy('order_base'),
            'questions' => fn ($query) => $query->where('is_active', true)->orderBy('order_base'),
            'questions.questionOptions' => fn ($query) => $query->orderBy('order_base'),
            'questions.contexts' => fn ($query) => $query->where('is_active', true),
        ]);

        return Inertia::render('Admin/AssessmentDrafts/Preview', [
            'pageTitle' => 'Preview web real del borrador',
            'subtitle' => 'Aquí sí revisamos el mismo renderer web del producto, no una imitación dentro de Filament.',
            'backHref' => ImportAiQuestionDraft::getUrl(panel: 'admin'),
            'draft' => [
                'id' => $template->id,
                'external_id' => $template->external_id,
                'title' => $template->title,
                'status' => $template->is_published ? 'published' : 'draft',
                'subject_label' => $template->subject_label,
                'unit_label' => $template->unit_label,
                'origin_type' => $template->source_content_type,
                'origin_label' => $template->origin_label,
                'question_count' => $template->questions->count(),
                'context_count' => $template->contexts->count(),
                'questions' => $template->questions
                    ->map(function ($question) use ($normalizer): array {
                        return [
                            'id' => (string) $question->external_id,
                            'order' => (int) $question->order_base,
                            'stem_html' => $normalizer->normalizeHtml((string) ($question->stem_html ?? '')),
                            'stem_blocks' => $normalizer->normalizeBlocks((array) ($question->stem_blocks ?? [])),
                            'feedback_html' => $normalizer->normalizeHtml((string) ($question->feedback_html ?? '')),
                            'feedback_blocks' => $normalizer->normalizeBlocks((array) ($question->feedback_blocks ?? [])),
                            'concepts_html' => $normalizer->normalizeHtml((string) ($question->concepts_html ?? '')),
                            'concepts_blocks' => $normalizer->normalizeBlocks((array) ($question->concepts_blocks ?? [])),
                            'correct_option_id' => filled($question->correct_option_id ?? null) ? (string) $question->correct_option_id : null,
                            'options' => $normalizer->normalizeOptions(
                                $question->questionOptions
                                    ->map(fn ($option): array => [
                                        'id' => (string) $option->option_id,
                                        'text' => (string) ($option->plain_text ?? ''),
                                        'text_html' => (string) ($option->html_web ?? ''),
                                        'asset_refs' => (array) ($option->asset_refs ?? []),
                                        'nodes_mobile' => (array) ($option->nodes_mobile ?? []),
                                        'is_correct' => (bool) $option->is_correct,
                                    ])
                                    ->all()
                            ),
                            'contexts' => $question->contexts
                                ->sortBy(fn ($context) => (int) ($context->pivot->order_base ?? $context->order_base ?? 0))
                                ->values()
                                ->map(fn ($context): array => [
                                    'id' => (string) $context->external_id,
                                    'title' => filled($context->title ?? null) ? (string) $context->title : 'Contexto compartido',
                                    'context_html' => $normalizer->normalizeHtml((string) ($context->context_html ?? '')),
                                    'context_blocks' => $normalizer->normalizeBlocks((array) ($context->context_blocks ?? [])),
                                ])
                                ->all(),
                        ];
                    })
                    ->all(),
            ],
        ]);
    }
}
