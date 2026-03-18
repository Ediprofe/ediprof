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

    public function getTitle(): string
    {
        return 'Banco de preguntas';
    }

    public function getSubheading(): ?string
    {
        return 'Aquí construyes el banco reusable del proyecto. Agregas preguntas al banco y el sistema las organiza internamente por bloques con contexto compartido cuando corresponde.';
    }

    protected function getHeaderActions(): array
    {
        return [
            Action::make('importBlock')
                ->label('Agregar preguntas')
                ->icon('heroicon-o-sparkles')
                ->tooltip('Pega preguntas o un bloque contextual y revisa la preview antes de guardarlo en el banco.')
                ->url(ImportAiQuestionDraft::getUrl(panel: 'admin')),
            Action::make('importBooklet')
                ->label('Traer preguntas desde cuadernillo')
                ->icon('heroicon-o-document-duplicate')
                ->color('gray')
                ->tooltip('Usa esta vía cuando el material viene como simulacro o taller completo y quieres poblar el banco en lote.')
                ->url(ImportAssessmentBooklet::getUrl(panel: 'admin')),
        ];
    }
}
