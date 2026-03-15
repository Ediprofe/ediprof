<?php

namespace App\Filament\Resources\AssessmentQuestions\Pages;

use App\Filament\Resources\AssessmentQuestions\AssessmentQuestionResource;
use App\Models\AssessmentQuestion;
use App\Services\Content\AssessmentEditorialContentUpdateService;
use Illuminate\Database\Eloquent\Model;
use Filament\Resources\Pages\EditRecord;

class EditAssessmentQuestion extends EditRecord
{
    protected static string $resource = AssessmentQuestionResource::class;

    protected function getHeaderActions(): array
    {
        return [];
    }

    /**
     * @param  array<string,mixed>  $data
     * @return array<string,mixed>
     */
    protected function mutateFormDataBeforeFill(array $data): array
    {
        /** @var AssessmentQuestion $record */
        $record = $this->getRecord();

        $optionsFromRelation = $record->questionOptions()
            ->orderBy('order_base')
            ->get()
            ->map(fn ($option): array => [
                'option_id' => (string) $option->option_id,
                'text' => (string) ($option->plain_text ?? ''),
            ])
            ->all();

        $data['options_editor'] = $optionsFromRelation !== []
            ? $optionsFromRelation
            : collect((array) ($record->options ?? []))
                ->map(fn ($option): array => [
                    'option_id' => trim((string) ($option['id'] ?? '')),
                    'text' => (string) ($option['text'] ?? ''),
                ])
                ->filter(fn (array $option): bool => $option['option_id'] !== '' && trim($option['text']) !== '')
                ->values()
                ->all();

        return $data;
    }

    protected function handleRecordUpdate(Model $record, array $data): Model
    {
        /** @var AssessmentQuestion $record */
        return app(AssessmentEditorialContentUpdateService::class)->updateQuestion($record, $data);
    }
}
