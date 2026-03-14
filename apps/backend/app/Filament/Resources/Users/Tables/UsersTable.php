<?php

namespace App\Filament\Resources\Users\Tables;

use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;

class UsersTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->defaultSort('last_names')
            ->columns([
                TextColumn::make('last_names')
                    ->label('Apellidos')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('first_names')
                    ->label('Nombres')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('institutional_code')
                    ->label('Matrícula')
                    ->searchable()
                    ->sortable()
                    ->toggleable(),
                TextColumn::make('document_number')
                    ->label('Documento')
                    ->searchable()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
                TextColumn::make('grade_group')
                    ->label('Grupo')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('email')
                    ->label('Correo')
                    ->searchable()
                    ->copyable(),
                TextColumn::make('role')
                    ->label('Rol')
                    ->badge()
                    ->color(fn (string $state): string => $state === 'admin' ? 'warning' : 'primary'),
                TextColumn::make('member_status')
                    ->label('Estado')
                    ->badge()
                    ->color(fn (string $state): string => match ($state) {
                        'approved' => 'success',
                        'blocked' => 'danger',
                        default => 'gray',
                    }),
                TextColumn::make('auth_provider')
                    ->label('Acceso')
                    ->badge()
                    ->formatStateUsing(fn (?string $state): string => $state === 'password' ? 'Correo' : 'Google'),
                TextColumn::make('last_login_at')
                    ->label('Último ingreso')
                    ->dateTime()
                    ->sortable(),
                TextColumn::make('updated_at')
                    ->label('Actualizado')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
            ])
            ->filters([
                SelectFilter::make('role')
                    ->label('Rol')
                    ->options([
                        'student' => 'Estudiante',
                        'admin' => 'Administrador',
                    ]),
                SelectFilter::make('member_status')
                    ->label('Estado')
                    ->options([
                        'approved' => 'Activo',
                        'pending' => 'Pendiente',
                        'blocked' => 'Bloqueado',
                    ]),
            ])
            ->recordActions([
                EditAction::make(),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    DeleteBulkAction::make(),
                ]),
            ]);
    }
}
