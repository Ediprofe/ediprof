<?php

namespace App\Filament\Resources\AssessmentBlocks\Pages;

use App\Filament\Resources\AssessmentBlocks\AssessmentBlockResource;
use Filament\Actions\Action;
use Filament\Resources\Pages\EditRecord;

class EditAssessmentBlock extends EditRecord
{
    protected static string $resource = AssessmentBlockResource::class;

    protected function getHeaderActions(): array
    {
        return [
            Action::make('previewWeb')
                ->label('Abrir preview web')
                ->icon('heroicon-o-globe-alt')
                ->url(fn (): string => route('admin.assessment_drafts.preview_web', $this->getRecord()), shouldOpenInNewTab: true),
        ];
    }
}
