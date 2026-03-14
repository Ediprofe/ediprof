<?php

namespace App\Filament\Resources\Courses\Pages;

use App\Filament\Resources\Courses\CourseResource;
use App\Models\Course;
use Filament\Actions\DeleteAction;
use Filament\Resources\Pages\EditRecord;

class EditCourse extends EditRecord
{
    protected static string $resource = CourseResource::class;

    protected function getHeaderActions(): array
    {
        return [
            DeleteAction::make(),
        ];
    }

    protected function mutateFormDataBeforeSave(array $data): array
    {
        /** @var Course $record */
        $record = $this->getRecord();
        $name = trim((string) ($data['name'] ?? ''));
        $slug = trim((string) ($data['slug'] ?? ''));

        return [
            ...$data,
            'name' => $name,
            'slug' => Course::resolveUniqueSlug($slug !== '' ? $slug : $name, $record->id),
            'school_year' => filled($data['school_year'] ?? null) ? trim((string) $data['school_year']) : null,
            'notes' => filled($data['notes'] ?? null) ? trim((string) $data['notes']) : null,
            'is_active' => (bool) ($data['is_active'] ?? false),
        ];
    }
}
