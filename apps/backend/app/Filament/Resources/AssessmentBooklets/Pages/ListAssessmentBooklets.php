<?php

namespace App\Filament\Resources\AssessmentBooklets\Pages;

use App\Filament\Pages\ImportAssessmentBooklet;
use App\Filament\Resources\AssessmentBooklets\AssessmentBookletResource;
use Filament\Actions\Action;
use Filament\Resources\Pages\ListRecords;

class ListAssessmentBooklets extends ListRecords
{
    protected static string $resource = AssessmentBookletResource::class;

    protected function getHeaderActions(): array
    {
        return [
            Action::make('importBooklet')
                ->label('Importar cuadernillo')
                ->icon('heroicon-o-arrow-up-tray')
                ->url(ImportAssessmentBooklet::getUrl(panel: 'admin')),
        ];
    }
}
