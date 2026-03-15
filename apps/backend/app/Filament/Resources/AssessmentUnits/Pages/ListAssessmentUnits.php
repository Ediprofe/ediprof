<?php

namespace App\Filament\Resources\AssessmentUnits\Pages;

use App\Filament\Resources\AssessmentUnits\AssessmentUnitResource;
use Filament\Actions\CreateAction;
use Filament\Resources\Pages\ListRecords;

class ListAssessmentUnits extends ListRecords
{
    protected static string $resource = AssessmentUnitResource::class;

    protected function getHeaderActions(): array
    {
        return [
            CreateAction::make(),
        ];
    }
}
