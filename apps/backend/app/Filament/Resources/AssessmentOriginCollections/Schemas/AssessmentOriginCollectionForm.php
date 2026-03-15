<?php

namespace App\Filament\Resources\AssessmentOriginCollections\Schemas;

use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Schema;

class AssessmentOriginCollectionForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
            Select::make('origin_type')
                ->label('Tipo de origen')
                ->options([
                    'simulacro' => 'Simulacro',
                    'taller' => 'Taller',
                    'unidad' => 'Unidad',
                    'manual' => 'Manual',
                ])
                ->required()
                ->native(false),
            TextInput::make('label')
                ->label('Nombre del origen')
                ->required()
                ->maxLength(255),
            Toggle::make('is_active')
                ->label('Activo')
                ->default(true)
                ->required(),
        ])->columns(2);
    }
}
