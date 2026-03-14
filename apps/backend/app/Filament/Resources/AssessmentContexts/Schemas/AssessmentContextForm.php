<?php

namespace App\Filament\Resources\AssessmentContexts\Schemas;

use App\Models\AssessmentContext;
use Filament\Forms\Components\Placeholder;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TagsInput;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Schemas\Schema;
use Illuminate\Support\Str;

class AssessmentContextForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
            Placeholder::make('source_key')
                ->label('Clave global')
                ->content(fn (?AssessmentContext $record): string => $record?->source_key ?? 'Pendiente de sincronización'),
            Placeholder::make('template')
                ->label('Plantilla editorial')
                ->content(fn (?AssessmentContext $record): string => $record?->template?->title ?? 'Sin plantilla'),
            Placeholder::make('linked_questions')
                ->label('Preguntas vinculadas')
                ->content(fn (?AssessmentContext $record): string => $record instanceof AssessmentContext
                    ? $record->questions()->count().' pregunta(s)'
                    : '0 pregunta(s)'),
            Placeholder::make('context_preview')
                ->label('Vista rápida del contexto')
                ->content(fn (?AssessmentContext $record): string => $record instanceof AssessmentContext
                    ? Str::limit(Str::of(strip_tags((string) $record->context_html))->squish()->value(), 420)
                    : ''),
            TextInput::make('topic')
                ->label('Tema')
                ->maxLength(255)
                ->nullable(),
            TextInput::make('unit_label')
                ->label('Unidad')
                ->maxLength(255)
                ->nullable(),
            TextInput::make('subtopic')
                ->label('Subtema')
                ->maxLength(255)
                ->nullable(),
            TextInput::make('origin_label')
                ->label('Origen')
                ->maxLength(255)
                ->nullable(),
            Select::make('editorial_status')
                ->label('Estado editorial')
                ->options([
                    'draft' => 'Borrador',
                    'ready' => 'Lista para usar',
                    'review' => 'Revisar',
                    'archived' => 'Archivada',
                ])
                ->nullable(),
            TagsInput::make('tags')
                ->label('Tags')
                ->helperText('Sirven para agrupar contextos o bloques reutilizables.'),
            Textarea::make('teacher_notes')
                ->label('Notas docentes')
                ->rows(5)
                ->nullable(),
        ]);
    }
}
