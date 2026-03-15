<?php

namespace App\Filament\Resources\AssessmentQuestions\Schemas;

use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentSubject;
use App\Models\AssessmentUnit;
use Filament\Forms\Components\Placeholder;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TagsInput;
use Filament\Forms\Components\Textarea;
use Filament\Schemas\Schema;
use Filament\Schemas\Components\Utilities\Get;
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
                ->helperText('Usa etiquetas cortas para filtrado docente.'),
            Textarea::make('teacher_notes')
                ->label('Notas docentes')
                ->rows(5)
                ->nullable(),
        ]);
    }
}
