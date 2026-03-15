<?php

namespace App\Services\Content;

use App\Models\AssessmentBooklet;
use App\Models\AssessmentBookletQuestion;
use App\Models\AssessmentBookletSection;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentSubject;
use App\Models\AssessmentTemplate;
use App\Models\AssessmentUnit;
use App\Models\User;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;
use InvalidArgumentException;

class AssessmentBookletImportService
{
    public function __construct(
        private readonly AiQuestionDraftImportService $draftImportService,
    ) {}

    /**
     * @param  array{
     *   title:string,
     *   booklet_type?:string|null,
     *   origin_collection_id:int,
     *   applied_on?:string|null,
     *   school_year?:string|null,
     *   notes?:string|null,
     *   editorial_status?:string|null,
     *   is_active?:bool,
     *   metadata?:array<string,mixed>|null
     * }  $bookletData
     * @param  array<int,array{
     *   title?:string|null,
     *   subject_id:int,
     *   default_unit_id?:int|null,
     *   parsed_draft:array<string,mixed>,
     *   metadata?:array<string,mixed>|null
     * }>  $sections
     */
    public function import(array $bookletData, array $sections, ?User $actor = null): AssessmentBooklet
    {
        if ($sections === []) {
            throw new InvalidArgumentException('El cuadernillo debe tener al menos una sección con preguntas.');
        }

        return DB::transaction(function () use ($bookletData, $sections, $actor): AssessmentBooklet {
            $origin = AssessmentOriginCollection::query()
                ->whereKey((int) ($bookletData['origin_collection_id'] ?? 0))
                ->firstOrFail();

            $booklet = AssessmentBooklet::query()->create([
                'title' => trim((string) $bookletData['title']),
                'booklet_type' => (string) ($bookletData['booklet_type'] ?? 'simulacro'),
                'origin_collection_id' => $origin->id,
                'applied_on' => $bookletData['applied_on'] ?? null,
                'school_year' => filled($bookletData['school_year'] ?? null) ? (string) $bookletData['school_year'] : null,
                'editorial_status' => (string) ($bookletData['editorial_status'] ?? 'draft'),
                'is_active' => (bool) ($bookletData['is_active'] ?? true),
                'notes' => filled($bookletData['notes'] ?? null) ? (string) $bookletData['notes'] : null,
                'metadata' => array_merge(
                    is_array($bookletData['metadata'] ?? null) ? $bookletData['metadata'] : [],
                    [
                        'source' => 'filament-booklet-import',
                        'created_by_user_id' => $actor?->id,
                        'created_by_email' => $actor?->email,
                    ],
                ),
            ]);

            $globalOrder = 1;

            foreach ($sections as $sectionIndex => $sectionData) {
                $subject = AssessmentSubject::query()
                    ->whereKey((int) ($sectionData['subject_id'] ?? 0))
                    ->firstOrFail();

                $defaultUnit = filled($sectionData['default_unit_id'] ?? null)
                    ? AssessmentUnit::query()
                        ->whereKey((int) $sectionData['default_unit_id'])
                        ->where('subject_id', $subject->id)
                        ->firstOrFail()
                    : null;

                $sectionTitle = $this->resolveSectionTitle($sectionData['title'] ?? null, $subject->label, $sectionIndex + 1);

                $template = $this->draftImportService->import(
                    $sectionData['parsed_draft'],
                    [
                        'subject_id' => $subject->id,
                        'unit_id' => $defaultUnit?->id,
                        'origin_collection_id' => $origin->id,
                    ],
                    $this->resolveTemplateTitle(
                        (string) $booklet->title,
                        $sectionTitle,
                        $subject->label,
                        $sectionIndex + 1,
                    ),
                    $actor,
                );

                $template->forceFill([
                    'metadata' => array_merge(
                        is_array($template->metadata ?? null) ? $template->metadata : [],
                        [
                            'booklet_id' => $booklet->id,
                            'booklet_external_id' => $booklet->external_id,
                            'booklet_title' => $booklet->title,
                            'booklet_section_title' => $sectionTitle,
                            'booklet_section_order' => $sectionIndex + 1,
                        ],
                    ),
                ])->save();

                $bookletSection = AssessmentBookletSection::query()->create([
                    'booklet_id' => $booklet->id,
                    'external_id' => $this->resolveSectionExternalId($subject->label, $sectionIndex + 1),
                    'title' => $sectionTitle,
                    'subject_id' => $subject->id,
                    'default_unit_id' => $defaultUnit?->id,
                    'template_id' => $template->id,
                    'order_base' => $sectionIndex + 1,
                    'total_questions' => (int) $template->questions()->count(),
                    'metadata' => array_merge(
                        is_array($sectionData['metadata'] ?? null) ? $sectionData['metadata'] : [],
                        [
                            'source' => 'filament-booklet-import',
                            'origin_collection_id' => $origin->id,
                        ],
                    ),
                ]);

                /** @var \Illuminate\Support\Collection<int, AssessmentQuestion> $templateQuestions */
                $templateQuestions = $template->questions()->orderBy('order_base')->get();

                foreach ($templateQuestions as $question) {
                    AssessmentBookletQuestion::query()->create([
                        'booklet_id' => $booklet->id,
                        'booklet_section_id' => $bookletSection->id,
                        'question_id' => $question->id,
                        'order_base' => $globalOrder,
                    ]);

                    $globalOrder++;
                }
            }

            $booklet->forceFill([
                'total_sections' => count($sections),
                'total_questions' => max($globalOrder - 1, 0),
            ])->save();

            return $booklet->fresh(['originCollection', 'sections.subject', 'sections.defaultUnit', 'sections.template']);
        });
    }

    private function resolveSectionTitle(?string $explicitTitle, string $subjectLabel, int $position): string
    {
        $title = trim((string) $explicitTitle);

        if ($title !== '') {
            return $title;
        }

        return 'Sección '.$position.' · '.$subjectLabel;
    }

    private function resolveSectionExternalId(string $subjectLabel, int $position): string
    {
        return 'section-'.str_pad((string) $position, 2, '0', STR_PAD_LEFT).'-'.Str::slug($subjectLabel);
    }

    private function resolveTemplateTitle(string $bookletTitle, string $sectionTitle, string $subjectLabel, int $position): string
    {
        return collect([
            trim($bookletTitle),
            trim($sectionTitle) !== '' ? trim($sectionTitle) : null,
            trim($subjectLabel) !== '' ? $subjectLabel : null,
            'bloque '.str_pad((string) $position, 2, '0', STR_PAD_LEFT),
        ])
            ->filter()
            ->unique()
            ->implode(' · ');
    }
}
