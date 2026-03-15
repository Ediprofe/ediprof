<?php

namespace App\Filament\Resources\AssessmentBooklets\Schemas;

use App\Models\AssessmentBooklet;
use App\Models\AssessmentOriginCollection;
use Filament\Forms\Components\Placeholder;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Schema;

class AssessmentBookletForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
            TextInput::make('title')
                ->label('Título del cuadernillo')
                ->required()
                ->maxLength(255),
            Select::make('booklet_type')
                ->label('Tipo')
                ->options([
                    'simulacro' => 'Simulacro',
                    'taller' => 'Taller',
                    'cuadernillo' => 'Cuadernillo',
                ])
                ->required()
                ->native(false),
            Select::make('origin_collection_id')
                ->label('Origen global')
                ->options(fn (): array => AssessmentOriginCollection::query()
                    ->where('is_active', true)
                    ->orderBy('label')
                    ->get()
                    ->mapWithKeys(fn (AssessmentOriginCollection $collection): array => [
                        $collection->id => sprintf('%s · %s', ucfirst($collection->origin_type), $collection->label),
                    ])
                    ->all())
                ->searchable()
                ->preload()
                ->native(false)
                ->required(),
            TextInput::make('applied_on')
                ->label('Fecha de aplicación')
                ->type('date'),
            TextInput::make('school_year')
                ->label('Año escolar')
                ->maxLength(20),
            Select::make('editorial_status')
                ->label('Estado editorial')
                ->options([
                    'draft' => 'Borrador',
                    'ready' => 'Lista para usar',
                    'review' => 'Revisar',
                    'archived' => 'Archivado',
                ])
                ->native(false),
            Toggle::make('is_active')
                ->label('Activo')
                ->default(true),
            Textarea::make('notes')
                ->label('Notas')
                ->rows(4)
                ->columnSpanFull(),
            Placeholder::make('totals')
                ->label('Resumen')
                ->content(fn (?AssessmentBooklet $record): string => $record
                    ? "{$record->total_sections} sección(es) · {$record->total_questions} pregunta(s)"
                    : 'Se llenará después de importar el cuadernillo.')
                ->columnSpanFull(),
        ]);
    }
}
