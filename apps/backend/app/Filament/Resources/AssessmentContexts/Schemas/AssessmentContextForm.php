<?php

namespace App\Filament\Resources\AssessmentContexts\Schemas;

use App\Models\AssessmentContext;
use Filament\Forms\Components\Placeholder;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;
use Illuminate\Support\Str;

class AssessmentContextForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
            Section::make('Identidad editorial')
                ->components([
                    Placeholder::make('source_key')
                        ->label('Clave global')
                        ->content(fn (?AssessmentContext $record): string => $record?->source_key ?? 'Pendiente de sincronización'),
                    Placeholder::make('template')
                        ->label('Bloque editorial')
                        ->content(fn (?AssessmentContext $record): string => $record?->template?->title ?? 'Sin bloque'),
                    Placeholder::make('linked_questions')
                        ->label('Preguntas vinculadas')
                        ->content(fn (?AssessmentContext $record): string => $record instanceof AssessmentContext
                            ? $record->questions()->count().' pregunta(s)'
                            : '0 pregunta(s)'),
                ])
                ->columns(3)
                ->collapsible(),
            Section::make('Contenido del contexto')
                ->description('Aquí sí puedes refinar el texto real del contexto. El Markdown se recompila al guardar.')
                ->components([
                    TextInput::make('title')
                        ->label('Título del contexto')
                        ->maxLength(255)
                        ->nullable()
                        ->columnSpanFull(),
                    Textarea::make('context_mdx')
                        ->label('Contexto (Markdown)')
                        ->rows(18)
                        ->required()
                        ->helperText('Usa este campo para corregir o enriquecer el texto base del bloque contextual.')
                        ->columnSpanFull(),
                    Placeholder::make('context_preview')
                        ->label('Vista rápida actual')
                        ->content(fn (?AssessmentContext $record): string => $record instanceof AssessmentContext
                            ? Str::limit(Str::of(strip_tags((string) $record->context_html))->squish()->value(), 420)
                            : '')
                        ->columnSpanFull(),
                    Textarea::make('teacher_notes')
                        ->label('Notas docentes')
                        ->rows(5)
                        ->nullable()
                        ->helperText('Úsalo solo para observaciones internas sobre el contexto base.')
                        ->columnSpanFull(),
                ]),
            Section::make('Referencia editorial del contexto')
                ->description('El contexto funciona como base general del bloque. La clasificación fina vive sobre todo en las preguntas asociadas.')
                ->components([
                    Placeholder::make('subject_label')
                        ->label('Materia')
                        ->content(fn (?AssessmentContext $record): string => $record?->subject?->label ?? 'Sin materia asignada'),
                    Placeholder::make('unit_label')
                        ->label('Unidad')
                        ->content(fn (?AssessmentContext $record): string => $record?->unit?->label ?? 'Unidad diferida'),
                    Placeholder::make('origin_label')
                        ->label('Origen')
                        ->content(fn (?AssessmentContext $record): string => $record?->originCollection
                            ? sprintf('%s · %s', ucfirst((string) $record->originCollection->origin_type), $record->originCollection->label)
                            : 'Sin origen asignado'),
                    Placeholder::make('editorial_status_label')
                        ->label('Estado editorial')
                        ->content(fn (?AssessmentContext $record): string => match ($record?->editorial_status) {
                            'ready' => 'Lista para usar',
                            'review' => 'Revisar',
                            'archived' => 'Archivada',
                            default => 'Borrador',
                        }),
                    Placeholder::make('tags_label')
                        ->label('Tags')
                        ->content(fn (?AssessmentContext $record): string => filled($record?->tags)
                            ? implode(', ', (array) $record->tags)
                            : 'Sin tags'),
                ])
                ->columns(2)
                ->collapsible()
                ->collapsed(),
        ]);
    }
}
