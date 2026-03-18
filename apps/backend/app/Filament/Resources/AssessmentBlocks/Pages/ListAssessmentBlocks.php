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
        return 'Banco editorial de bloques';
    }

    public function getSubheading(): ?string
    {
        return 'Aquí construyes el banco reusable del proyecto: puedes agregar bloques sueltos o cargar un cuadernillo completo para revisarlo y guardarlo.';
    }

    protected function getHeaderActions(): array
    {
        return [
            Action::make('importBlock')
                ->label('Agregar bloque al banco')
                ->icon('heroicon-o-sparkles')
                ->tooltip('Pega un bloque y deja que el sistema lo interprete para revisarlo antes de guardarlo.')
                ->url(ImportAiQuestionDraft::getUrl(panel: 'admin')),
            Action::make('importBooklet')
                ->label('Cargar cuadernillo al banco')
                ->icon('heroicon-o-document-duplicate')
                ->color('gray')
                ->tooltip('Trae un simulacro o taller completo por bloques para poblar el banco sin repetir trabajo.')
                ->url(ImportAssessmentBooklet::getUrl(panel: 'admin')),
        ];
    }
}
