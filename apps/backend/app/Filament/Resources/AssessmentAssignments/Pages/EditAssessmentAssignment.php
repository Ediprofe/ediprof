<?php

namespace App\Filament\Resources\AssessmentAssignments\Pages;

use App\Filament\Resources\AssessmentAssignments\AssessmentAssignmentResource;
use Filament\Actions\DeleteAction;
use Filament\Resources\Pages\EditRecord;

class EditAssessmentAssignment extends EditRecord
{
    protected static string $resource = AssessmentAssignmentResource::class;

    protected function getHeaderActions(): array
    {
        return [
            DeleteAction::make(),
        ];
    }
}
