<?php

namespace App\Filament\Resources\AssessmentQuestions\Schemas;

use App\Models\AssessmentQuestion;
use Filament\Forms\Components\Placeholder;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TagsInput;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Schemas\Schema;
use Illuminate\Support\Str;

class AssessmentQuestionForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
            Placeholder::make('source_key')
                ->label('Clave global')
                ->content(fn (?AssessmentQuestion $record): string => $record?->source_key ?? 'Pendiente de sincronización'),
            Placeholder::make('template')
                ->label('Plantilla editorial')
                ->content(fn (?AssessmentQuestion $record): string => $record?->template?->title ?? 'Sin plantilla'),
            Placeholder::make('source_slug')
                ->label('Origen editorial')
                ->content(fn (?AssessmentQuestion $record): string => $record?->source_slug ?? 'Sin origen'),
            Placeholder::make('stem_preview')
                ->label('Vista rápida del enunciado')
                ->content(fn (?AssessmentQuestion $record): string => $record instanceof AssessmentQuestion
                    ? Str::limit(Str::of(strip_tags((string) $record->stem_html))->squish()->value(), 420)
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
                ->helperText('Editable desde backend para no depender del MDX en la clasificación.')
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
                ->helperText('Usa etiquetas cortas para filtrado docente.'),
            Textarea::make('teacher_notes')
                ->label('Notas docentes')
                ->rows(5)
                ->nullable(),
        ]);
    }
}
