<?php

namespace App\Filament\Resources\AssessmentContexts\Pages;

use App\Filament\Resources\AssessmentContexts\AssessmentContextResource;
use Filament\Resources\Pages\ListRecords;

class ListAssessmentContexts extends ListRecords
{
    protected static string $resource = AssessmentContextResource::class;

    protected function getHeaderActions(): array
    {
        return [];
    }
}
