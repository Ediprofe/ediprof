<?php

namespace App\Filament\Resources\Courses\Pages;

use App\Filament\Resources\Courses\CourseResource;
use App\Models\Course;
use Filament\Resources\Pages\CreateRecord;

class CreateCourse extends CreateRecord
{
    protected static string $resource = CourseResource::class;

    protected function mutateFormDataBeforeCreate(array $data): array
    {
        $name = trim((string) ($data['name'] ?? ''));
        $slug = trim((string) ($data['slug'] ?? ''));

        return [
            ...$data,
            'name' => $name,
            'slug' => Course::resolveUniqueSlug($slug !== '' ? $slug : $name),
            'school_year' => filled($data['school_year'] ?? null) ? trim((string) $data['school_year']) : null,
            'notes' => filled($data['notes'] ?? null) ? trim((string) $data['notes']) : null,
            'is_active' => (bool) ($data['is_active'] ?? true),
        ];
    }
}
