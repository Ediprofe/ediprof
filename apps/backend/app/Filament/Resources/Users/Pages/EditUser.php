<?php

namespace App\Filament\Resources\Users\Pages;

use App\Filament\Resources\Users\UserResource;
use App\Models\User;
use Filament\Actions\DeleteAction;
use Filament\Resources\Pages\EditRecord;

class EditUser extends EditRecord
{
    protected static string $resource = UserResource::class;

    protected function getHeaderActions(): array
    {
        return [
            DeleteAction::make(),
        ];
    }

    protected function mutateFormDataBeforeSave(array $data): array
    {
        $password = trim((string) ($data['password'] ?? ''));
        $firstNames = filled($data['first_names'] ?? null) ? trim((string) $data['first_names']) : null;
        $lastNames = filled($data['last_names'] ?? null) ? trim((string) $data['last_names']) : null;

        if ($password === '') {
            unset($data['password']);
        } else {
            $data['password'] = $password;
        }

        $data['name'] = User::composeDisplayName($lastNames, $firstNames, (string) ($data['name'] ?? ''));
        $data['first_names'] = $firstNames;
        $data['last_names'] = $lastNames;
        $data['email'] = mb_strtolower(trim((string) ($data['email'] ?? '')));
        $data['institutional_code'] = filled($data['institutional_code'] ?? null) ? trim((string) $data['institutional_code']) : null;
        $data['document_number'] = filled($data['document_number'] ?? null) ? trim((string) $data['document_number']) : null;
        $data['grade_group'] = filled($data['grade_group'] ?? null) ? trim((string) $data['grade_group']) : null;
        $data['google_subject'] = filled($data['google_subject'] ?? null) ? trim((string) $data['google_subject']) : null;
        $data['google_avatar_url'] = filled($data['google_avatar_url'] ?? null) ? trim((string) $data['google_avatar_url']) : null;

        return $data;
    }
}
