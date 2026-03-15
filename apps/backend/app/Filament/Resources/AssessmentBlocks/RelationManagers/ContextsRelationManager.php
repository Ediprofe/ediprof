<?php

namespace App\Filament\Resources\AssessmentBlocks\RelationManagers;

use App\Filament\Resources\AssessmentContexts\AssessmentContextResource;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentContext;
use App\Models\AssessmentSubject;
use App\Models\AssessmentUnit;
use App\Services\Content\AssessmentEditorialContentUpdateService;
use Filament\Actions\Action;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Notifications\Notification;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Schemas\Components\Utilities\Get;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Illuminate\Support\Str;

class ContextsRelationManager extends RelationManager
{
    protected static string $relationship = 'contexts';

    protected static ?string $title = 'Contextos del bloque';

    public function table(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn ($query) => $query->withCount('questions'))
            ->defaultSort('order_base')
            ->columns([
                TextColumn::make('order_base')
                    ->label('#')
                    ->sortable(),
                TextColumn::make('title')
                    ->label('Contexto')
                    ->searchable()
                    ->wrap()
                    ->placeholder('Sin título'),
                TextColumn::make('questions_count')
                    ->label('Preguntas vinculadas')
                    ->sortable(),
                TextColumn::make('unit_label')
                    ->label('Unidad')
                    ->placeholder('Diferida'),
                TextColumn::make('context_html')
                    ->label('Preview')
                    ->state(fn (AssessmentContext $record): string => Str::limit(
                        Str::of(strip_tags((string) $record->context_html))->squish()->value(),
                        150
                    ))
                    ->wrap(),
            ])
            ->recordActions([
                Action::make('quickEditContext')
                    ->label('Editar aquí')
                    ->icon('heroicon-o-pencil-square')
                    ->color('primary')
                    ->slideOver()
                    ->modalWidth('6xl')
                    ->modalHeading('Editar contexto del bloque')
                    ->fillForm(fn (AssessmentContext $record): array => [
                        'title' => $record->title,
                        'context_mdx' => $record->context_mdx,
                        'subject_id' => $record->subject_id,
                        'unit_id' => $record->unit_id,
                        'origin_collection_id' => $record->origin_collection_id,
                        'editorial_status' => $record->editorial_status,
                        'tags' => $record->tags ?? [],
                        'teacher_notes' => $record->teacher_notes,
                    ])
                    ->schema([
                        TextInput::make('title')
                            ->label('Título del contexto')
                            ->maxLength(255)
                            ->columnSpanFull(),
                        Textarea::make('context_mdx')
                            ->label('Contexto (Markdown)')
                            ->rows(16)
                            ->required()
                            ->columnSpanFull(),
                        Select::make('subject_id')
                            ->label('Materia')
                            ->options(fn (): array => AssessmentSubject::query()->where('is_active', true)->orderBy('label')->pluck('label', 'id')->all())
                            ->searchable()
                            ->preload()
                            ->native(false)
                            ->nullable()
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
                            ->nullable(),
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
                            ->nullable(),
                        Select::make('editorial_status')
                            ->label('Estado editorial')
                            ->options([
                                'draft' => 'Borrador',
                                'ready' => 'Lista para usar',
                                'review' => 'Revisar',
                                'archived' => 'Archivada',
                            ])
                            ->native(false)
                            ->nullable(),
                        Textarea::make('teacher_notes')
                            ->label('Notas docentes')
                            ->rows(4)
                            ->columnSpanFull(),
                    ])
                    ->action(function (AssessmentContext $record, array $data): void {
                        app(AssessmentEditorialContentUpdateService::class)->updateContext($record, $data);

                        Notification::make()
                            ->title('Contexto actualizado')
                            ->body('Los cambios editoriales del contexto quedaron guardados dentro del bloque.')
                            ->success()
                            ->send();
                    }),
                Action::make('openDetail')
                    ->label('Abrir detalle')
                    ->icon('heroicon-o-arrow-top-right-on-square')
                    ->color('gray')
                    ->url(fn (AssessmentContext $record): string => AssessmentContextResource::getUrl('edit', ['record' => $record], panel: 'admin')),
            ])
            ->emptyStateHeading('Este bloque todavía no tiene contextos.');
    }
}
