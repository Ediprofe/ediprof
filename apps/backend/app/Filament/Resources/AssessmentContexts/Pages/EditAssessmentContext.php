<?php

namespace App\Filament\Resources\AssessmentContexts\Pages;

use App\Filament\Resources\AssessmentContexts\AssessmentContextResource;
use App\Models\AssessmentContext;
use App\Services\Content\AssessmentEditorialContentUpdateService;
use Illuminate\Database\Eloquent\Model;
use Filament\Resources\Pages\EditRecord;

class EditAssessmentContext extends EditRecord
{
    protected static string $resource = AssessmentContextResource::class;

    protected function getHeaderActions(): array
    {
        return [];
    }

    protected function handleRecordUpdate(Model $record, array $data): Model
    {
        /** @var AssessmentContext $record */
        return app(AssessmentEditorialContentUpdateService::class)->updateContext($record, $data);
    }
}
