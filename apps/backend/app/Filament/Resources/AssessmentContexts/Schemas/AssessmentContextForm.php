<?php

namespace App\Filament\Resources\AssessmentContexts\Schemas;

use App\Models\AssessmentContext;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentSubject;
use App\Models\AssessmentUnit;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Placeholder;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TagsInput;
use Filament\Forms\Components\Textarea;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;
use Filament\Schemas\Components\Utilities\Get;
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
                ->columns(3),
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
                ]),
            Section::make('Clasificación editorial')
                ->components([
                    Select::make('subject_id')
                        ->label('Materia')
                        ->options(fn (): array => AssessmentSubject::query()->where('is_active', true)->orderBy('label')->pluck('label', 'id')->all())
                        ->searchable()
                        ->preload()
                        ->native(false)
                        ->nullable(),
                    Select::make('unit_id')
                        ->label('Unidad')
                        ->options(fn (Get $get): array => AssessmentUnit::query()
                            ->where('is_active', true)
                            ->when($get('subject_id'), fn ($query, $subjectId) => $query->where('subject_id', $subjectId))
                            ->orderBy('label')
                            ->pluck('label', 'id')
                            ->all())
                        ->searchable()
                        ->preload()
                        ->native(false)
                        ->nullable(),
                    Select::make('origin_collection_id')
                        ->label('Origen')
                        ->helperText('El origen puede reutilizarse en distintas materias y unidades.')
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
                        ->helperText('Sirven para agrupar contextos o bloques reutilizables.')
                        ->columnSpanFull(),
                    Textarea::make('teacher_notes')
                        ->label('Notas docentes')
                        ->rows(5)
                        ->nullable()
                        ->columnSpanFull(),
                ])
                ->columns(2),
        ]);
    }
}
