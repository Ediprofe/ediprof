<?php

namespace App\Filament\Resources\AssessmentOriginCollections\Pages;

use App\Filament\Resources\AssessmentOriginCollections\AssessmentOriginCollectionResource;
use Filament\Actions\DeleteAction;
use Filament\Resources\Pages\EditRecord;

class EditAssessmentOriginCollection extends EditRecord
{
    protected static string $resource = AssessmentOriginCollectionResource::class;

    protected function getHeaderActions(): array
    {
        return [
            DeleteAction::make(),
        ];
    }
}
