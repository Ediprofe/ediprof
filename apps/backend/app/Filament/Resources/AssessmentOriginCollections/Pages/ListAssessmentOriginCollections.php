<?php

namespace App\Filament\Resources\AssessmentOriginCollections\Pages;

use App\Filament\Resources\AssessmentOriginCollections\AssessmentOriginCollectionResource;
use Filament\Actions\CreateAction;
use Filament\Resources\Pages\ListRecords;

class ListAssessmentOriginCollections extends ListRecords
{
    protected static string $resource = AssessmentOriginCollectionResource::class;

    protected function getHeaderActions(): array
    {
        return [
            CreateAction::make(),
        ];
    }
}
