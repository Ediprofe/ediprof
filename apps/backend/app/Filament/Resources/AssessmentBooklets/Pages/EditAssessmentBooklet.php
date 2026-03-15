<?php

namespace App\Filament\Resources\AssessmentBooklets\Pages;

use App\Filament\Resources\AssessmentBooklets\AssessmentBookletResource;
use Filament\Actions\DeleteAction;
use Filament\Resources\Pages\EditRecord;

class EditAssessmentBooklet extends EditRecord
{
    protected static string $resource = AssessmentBookletResource::class;

    protected function getHeaderActions(): array
    {
        return [
            DeleteAction::make(),
        ];
    }
}
