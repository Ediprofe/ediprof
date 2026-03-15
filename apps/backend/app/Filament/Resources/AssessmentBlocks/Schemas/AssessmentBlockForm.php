<?php

namespace App\Filament\Resources\AssessmentBlocks\Schemas;

use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentSubject;
use App\Models\AssessmentTemplate;
use App\Models\AssessmentUnit;
use Filament\Forms\Components\Placeholder;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Schemas\Components\Utilities\Get;
use Filament\Schemas\Schema;
use Illuminate\Support\Str;

class AssessmentBlockForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
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
            Placeholder::make('block_preview')
                ->label('Vista rápida')
                ->content(fn (?AssessmentTemplate $record): string => $record instanceof AssessmentTemplate
                    ? Str::limit(
                        Str::of(strip_tags((string) optional($record->contexts()->orderBy('order_base')->first())->context_html))->squish()->value(),
                        320
                    )
                    : ''),
            TextInput::make('title')
                ->label('Título del bloque')
                ->required()
                ->maxLength(255),
            Select::make('subject_id')
                ->label('Materia')
                ->options(fn (): array => AssessmentSubject::query()->where('is_active', true)->orderBy('label')->pluck('label', 'id')->all())
                ->searchable()
                ->preload()
                ->native(false)
                ->required()
                ->live(),
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
                ->nullable()
                ->helperText('Puede quedar diferida si todavía estás clasificando el banco.'),
            Select::make('origin_collection_id')
                ->label('Origen')
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
            Select::make('editorial_status')
                ->label('Estado editorial')
                ->options([
                    'draft' => 'Borrador',
                    'ready' => 'Lista para usar',
                    'review' => 'Revisar',
                    'archived' => 'Archivada',
                ])
                ->native(false)
                ->required(),
            Placeholder::make('usage_note')
                ->label('Uso editorial')
                ->content('Este bloque se reutiliza luego en talleres, simulacros o evaluaciones. Las preguntas y contextos se editan desde las pestañas inferiores.'),
        ]);
    }
}
