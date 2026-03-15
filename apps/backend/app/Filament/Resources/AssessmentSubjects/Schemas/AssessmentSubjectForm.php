<?php

namespace App\Filament\Resources\AssessmentSubjects\Schemas;

use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Schema;

class AssessmentSubjectForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
            TextInput::make('label')
                ->label('Materia')
                ->required()
                ->maxLength(255),
            Toggle::make('is_active')
                ->label('Activa')
                ->default(true)
                ->required(),
        ]);
    }
}
