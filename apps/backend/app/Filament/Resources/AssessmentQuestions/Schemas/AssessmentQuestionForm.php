<?php

namespace App\Filament\Resources\AssessmentQuestions\Schemas;

use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentSubject;
use App\Models\AssessmentUnit;
use Filament\Forms\Components\Placeholder;
use Filament\Forms\Components\Repeater;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TagsInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;
use Filament\Schemas\Components\Utilities\Get;
use Illuminate\Support\Str;

class AssessmentQuestionForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
            Section::make('Identidad editorial')
                ->components([
                    Placeholder::make('source_key')
                        ->label('Clave global')
                        ->content(fn (?AssessmentQuestion $record): string => $record?->source_key ?? 'Pendiente de sincronización'),
                    Placeholder::make('template')
                        ->label('Bloque editorial')
                        ->content(fn (?AssessmentQuestion $record): string => $record?->template?->title ?? 'Sin bloque'),
                    Placeholder::make('source_slug')
                        ->label('Origen editorial heredado')
                        ->content(fn (?AssessmentQuestion $record): string => $record?->source_slug ?? 'Sin origen'),
                    Placeholder::make('linked_contexts')
                        ->label('Contextos vinculados')
                        ->content(fn (?AssessmentQuestion $record): string => $record instanceof AssessmentQuestion
                            ? $record->contexts()->count().' contexto(s)'
                            : '0 contexto(s)'),
                ])
                ->columns(4),
            Section::make('Contenido de la pregunta')
                ->description('Aquí puedes corregir el enunciado, las opciones, la respuesta correcta y la explicación pedagógica.')
                ->components([
                    Textarea::make('stem_mdx')
                        ->label('Enunciado (Markdown)')
                        ->rows(10)
                        ->required()
                        ->columnSpanFull(),
                    Repeater::make('options_editor')
                        ->label('Opciones')
                        ->addActionLabel('Agregar opción')
                        ->minItems(2)
                        ->defaultItems(4)
                        ->reorderable(false)
                        ->live()
                        ->schema([
                            TextInput::make('option_id')
                                ->label('Letra')
                                ->required()
                                ->maxLength(5)
                                ->placeholder('A'),
                            Textarea::make('text')
                                ->label('Texto de la opción')
                                ->required()
                                ->rows(3)
                                ->columnSpanFull(),
                        ])
                        ->columns(2)
                        ->columnSpanFull(),
                    Select::make('correct_option_id')
                        ->label('Respuesta correcta')
                        ->options(fn (Get $get): array => collect((array) $get('options_editor'))
                            ->mapWithKeys(function ($option): array {
                                if (! is_array($option)) {
                                    return [];
                                }

                                $optionId = trim((string) ($option['option_id'] ?? ''));
                                if ($optionId === '') {
                                    return [];
                                }

                                $text = Str::limit(
                                    Str::of((string) ($option['text'] ?? ''))->squish()->value(),
                                    80
                                );

                                return [$optionId => $optionId.($text !== '' ? ' · '.$text : '')];
                            })
                            ->all())
                        ->helperText('Selecciona la opción correcta después de revisar las letras definidas arriba.')
                        ->required()
                        ->native(false)
                        ->searchable(false),
                    Placeholder::make('stem_preview')
                        ->label('Vista rápida actual del enunciado')
                        ->content(fn (?AssessmentQuestion $record): string => $record instanceof AssessmentQuestion
                            ? Str::limit(Str::of(strip_tags((string) $record->stem_html))->squish()->value(), 420)
                            : '')
                        ->columnSpanFull(),
                    Textarea::make('feedback_mdx')
                        ->label('Retroalimentación / solución guiada (Markdown)')
                        ->rows(10)
                        ->nullable()
                        ->columnSpanFull(),
                    Textarea::make('concepts_mdx')
                        ->label('Conceptos relacionados (Markdown)')
                        ->rows(10)
                        ->nullable()
                        ->columnSpanFull(),
                ])
                ->columns(2),
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
                        ->helperText('Editable desde backend para no depender del MDX en la clasificación. El origen puede cruzar varias materias.')
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
                        ->helperText('Usa etiquetas cortas para filtrado docente.')
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
