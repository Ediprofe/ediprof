<?php

namespace App\Filament\Resources\AssessmentBlocks\Schemas;

use App\Models\AssessmentTemplate;
use Filament\Forms\Components\Placeholder;
use Filament\Forms\Components\TextInput;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;

class AssessmentBlockForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
            Section::make('Identidad del bloque')
                ->components([
                    TextInput::make('title')
                        ->label('Título del bloque')
                        ->required()
                        ->maxLength(255)
                        ->helperText('Usa un nombre corto y claro para reconocer el bloque en el banco.'),
                ]),
            Section::make('Información técnica del sistema')
                ->description('Se deja aquí como referencia del bloque, sin interrumpir el flujo editorial.')
                ->collapsible()
                ->collapsed()
                ->components([
                    Placeholder::make('origin_reference')
                        ->label('Origen de referencia')
                        ->content(fn (?AssessmentTemplate $record): string => $record?->origin_label ?: 'Sin origen'),
                    Placeholder::make('external_id')
                        ->label('ID editorial')
                        ->content(fn (?AssessmentTemplate $record): string => $record?->external_id ?? 'Sin ID'),
                    Placeholder::make('counts')
                        ->label('Estructura del bloque')
                        ->content(fn (?AssessmentTemplate $record): string => $record instanceof AssessmentTemplate
                            ? sprintf(
                                '%d contexto(s) · %d pregunta(s)',
                                $record->contexts()->count(),
                                $record->questions()->count(),
                            )
                            : '0 contexto(s) · 0 pregunta(s)'),
                ])
                ->columns(3),
        ]);
    }
}
