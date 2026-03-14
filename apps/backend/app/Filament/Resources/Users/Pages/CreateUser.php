<?php

namespace App\Filament\Resources\Users\Pages;

use App\Filament\Resources\Users\UserResource;
use App\Models\User;
use Filament\Resources\Pages\CreateRecord;
use Illuminate\Support\Str;

class CreateUser extends CreateRecord
{
    protected static string $resource = UserResource::class;

    protected function mutateFormDataBeforeCreate(array $data): array
    {
        $password = trim((string) ($data['password'] ?? ''));
        $firstNames = filled($data['first_names'] ?? null) ? trim((string) $data['first_names']) : null;
        $lastNames = filled($data['last_names'] ?? null) ? trim((string) $data['last_names']) : null;
        $displayName = User::composeDisplayName($lastNames, $firstNames, (string) ($data['name'] ?? ''));

        return [
            ...$data,
            'name' => $displayName,
            'first_names' => $firstNames,
            'last_names' => $lastNames,
            'email' => mb_strtolower(trim((string) ($data['email'] ?? ''))),
            'institutional_code' => filled($data['institutional_code'] ?? null) ? trim((string) $data['institutional_code']) : null,
            'document_number' => filled($data['document_number'] ?? null) ? trim((string) $data['document_number']) : null,
            'grade_group' => filled($data['grade_group'] ?? null) ? trim((string) $data['grade_group']) : null,
            'password' => $password !== '' ? $password : Str::random(40),
            'google_subject' => filled($data['google_subject'] ?? null) ? trim((string) $data['google_subject']) : null,
            'google_avatar_url' => filled($data['google_avatar_url'] ?? null) ? trim((string) $data['google_avatar_url']) : null,
        ];
    }
}
