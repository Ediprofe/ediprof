<?php

namespace App\Filament\Resources\AssessmentSubjects\Pages;

use App\Filament\Resources\AssessmentSubjects\AssessmentSubjectResource;
use Filament\Actions\DeleteAction;
use Filament\Resources\Pages\EditRecord;

class EditAssessmentSubject extends EditRecord
{
    protected static string $resource = AssessmentSubjectResource::class;

    protected function getHeaderActions(): array
    {
        return [
            DeleteAction::make(),
        ];
    }
}
