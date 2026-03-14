<?php

namespace App\Filament\Resources\AssessmentAssignments\Pages;

use App\Filament\Resources\AssessmentAssignments\AssessmentAssignmentResource;
use Filament\Actions\CreateAction;
use Filament\Resources\Pages\ListRecords;

class ListAssessmentAssignments extends ListRecords
{
    protected static string $resource = AssessmentAssignmentResource::class;

    protected function getHeaderActions(): array
    {
        return [
            CreateAction::make(),
        ];
    }
}
