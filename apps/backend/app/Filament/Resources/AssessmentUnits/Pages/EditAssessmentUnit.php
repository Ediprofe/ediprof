<?php

namespace App\Filament\Resources\AssessmentUnits\Pages;

use App\Filament\Resources\AssessmentUnits\AssessmentUnitResource;
use Filament\Actions\DeleteAction;
use Filament\Resources\Pages\EditRecord;

class EditAssessmentUnit extends EditRecord
{
    protected static string $resource = AssessmentUnitResource::class;

    protected function getHeaderActions(): array
    {
        return [
            DeleteAction::make(),
        ];
    }
}
