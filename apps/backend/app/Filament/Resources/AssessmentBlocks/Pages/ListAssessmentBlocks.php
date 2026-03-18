<?php

namespace App\Filament\Resources\AssessmentBlocks\Pages;

use App\Filament\Pages\ImportAiQuestionDraft;
use App\Filament\Resources\AssessmentBlocks\AssessmentBlockResource;
use App\Filament\Resources\AssessmentQuestions\AssessmentQuestionResource;
use Filament\Actions\Action;
use Filament\Resources\Pages\ListRecords;

class ListAssessmentBlocks extends ListRecords
{
    protected static string $resource = AssessmentBlockResource::class;

    public function getTitle(): string
    {
        return 'Bloques y contextos';
    }

    public function getSubheading(): ?string
    {
        return 'Aquí revisas la estructura editorial del banco: contexto compartido, bloque y relación entre preguntas. Es una vista de soporte, no la puerta principal de captura.';
    }

    protected function getHeaderActions(): array
    {
        return [
            Action::make('goToQuestionBank')
                ->label('Ir al banco de preguntas')
                ->icon('heroicon-o-rectangle-stack')
                ->tooltip('La entrada principal para alimentar y consultar el banco está en Banco de preguntas.')
                ->url(AssessmentQuestionResource::getUrl('index', panel: 'admin')),
            Action::make('addQuestions')
                ->label('Agregar preguntas')
                ->icon('heroicon-o-sparkles')
                ->color('gray')
                ->url(ImportAiQuestionDraft::getUrl(panel: 'admin')),
        ];
    }
}
