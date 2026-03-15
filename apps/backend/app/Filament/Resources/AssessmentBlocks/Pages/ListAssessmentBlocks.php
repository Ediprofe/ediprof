<?php

namespace App\Filament\Resources\AssessmentBlocks\Pages;

use App\Filament\Pages\ImportAiQuestionDraft;
use App\Filament\Pages\ImportAssessmentBooklet;
use App\Filament\Resources\AssessmentBlocks\AssessmentBlockResource;
use Filament\Actions\Action;
use Filament\Resources\Pages\ListRecords;

class ListAssessmentBlocks extends ListRecords
{
    protected static string $resource = AssessmentBlockResource::class;

    protected function getHeaderActions(): array
    {
        return [
            Action::make('importBlock')
                ->label('Importar bloque con IA')
                ->icon('heroicon-o-sparkles')
                ->url(ImportAiQuestionDraft::getUrl(panel: 'admin')),
            Action::make('importBooklet')
                ->label('Importar cuadernillo')
                ->icon('heroicon-o-document-duplicate')
                ->color('gray')
                ->url(ImportAssessmentBooklet::getUrl(panel: 'admin')),
        ];
    }
}
