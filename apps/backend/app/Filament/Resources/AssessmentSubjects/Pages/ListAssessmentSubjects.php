<?php

namespace App\Filament\Resources\AssessmentSubjects\Pages;

use App\Filament\Resources\AssessmentSubjects\AssessmentSubjectResource;
use Filament\Actions\CreateAction;
use Filament\Resources\Pages\ListRecords;

class ListAssessmentSubjects extends ListRecords
{
    protected static string $resource = AssessmentSubjectResource::class;

    protected function getHeaderActions(): array
    {
        return [
            CreateAction::make(),
        ];
    }
}
