<?php

namespace App\Filament\Resources\Users\Schemas;

use Filament\Forms\Components\DateTimePicker;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Schemas\Schema;

class UserForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema
            ->components([
                TextInput::make('last_names')
                    ->label('Apellidos')
                    ->maxLength(255),
                TextInput::make('first_names')
                    ->label('Nombres')
                    ->maxLength(255),
                TextInput::make('name')
                    ->label('Nombre visible')
                    ->helperText('Si completas apellidos y nombres, este campo se reconstruye automáticamente.')
                    ->required()
                    ->maxLength(255),
                TextInput::make('email')
                    ->label('Correo')
                    ->email()
                    ->required()
                    ->unique(ignoreRecord: true),
                TextInput::make('institutional_code')
                    ->label('Matrícula')
                    ->maxLength(255),
                TextInput::make('document_number')
                    ->label('Documento')
                    ->maxLength(255),
                TextInput::make('grade_group')
                    ->label('Grupo')
                    ->maxLength(255),
                TextInput::make('password')
                    ->label('Contraseña')
                    ->password()
                    ->helperText('Déjala vacía para conservar la actual o para generar una aleatoria en cuentas Google.'),
                Select::make('role')
                    ->label('Rol')
                    ->options([
                        'student' => 'Estudiante',
                        'admin' => 'Administrador',
                    ])
                    ->required()
                    ->default('student'),
                Select::make('member_status')
                    ->label('Estado')
                    ->options([
                        'approved' => 'Activo',
                        'pending' => 'Pendiente',
                        'blocked' => 'Bloqueado',
                    ])
                    ->required()
                    ->default('pending'),
                Select::make('auth_provider')
                    ->label('Proveedor de acceso')
                    ->options([
                        'password' => 'Correo y contraseña',
                        'google' => 'Google',
                    ])
                    ->default('google'),
                TextInput::make('google_subject'),
                TextInput::make('google_avatar_url')
                    ->url(),
                DateTimePicker::make('email_verified_at')
                    ->label('Correo verificado'),
                DateTimePicker::make('last_login_at'),
            ]);
    }
}
