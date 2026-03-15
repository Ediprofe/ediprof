<?php

namespace App\Filament\Resources\AssessmentUnits\Schemas;

use App\Models\AssessmentSubject;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Schema;

class AssessmentUnitForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
            Select::make('subject_id')
                ->label('Materia')
                ->options(fn (): array => AssessmentSubject::query()->where('is_active', true)->orderBy('label')->pluck('label', 'id')->all())
                ->required()
                ->searchable()
                ->preload()
                ->native(false),
            TextInput::make('label')
                ->label('Unidad')
                ->required()
                ->maxLength(255),
            Toggle::make('is_active')
                ->label('Activa')
                ->default(true)
                ->required(),
        ])->columns(2);
    }
}
