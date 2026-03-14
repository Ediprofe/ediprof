<?php

namespace App\Filament\Resources\Courses\Schemas;

use Filament\Forms\Components\Placeholder;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Schema;

class CourseForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema
            ->components([
                TextInput::make('name')
                    ->label('Nombre del curso')
                    ->required()
                    ->maxLength(120),
                TextInput::make('slug')
                    ->label('Slug opcional')
                    ->helperText('Si lo dejas vacío, Ediprofe genera uno automáticamente.')
                    ->maxLength(120),
                TextInput::make('school_year')
                    ->label('Año escolar')
                    ->maxLength(20)
                    ->default((string) now()->year),
                Toggle::make('is_active')
                    ->label('Curso activo')
                    ->default(true)
                    ->required(),
                Textarea::make('notes')
                    ->label('Notas')
                    ->rows(4)
                    ->columnSpanFull(),
                Placeholder::make('course_hint')
                    ->label('Sugerencia')
                    ->content('Usa nombres claros como ICFES 11°1, ICFES 11°2 o Ciencias 8°.')
                    ->columnSpanFull(),
            ]);
    }
}
