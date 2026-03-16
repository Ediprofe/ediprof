<?php

namespace App\Filament\Resources\AssessmentBlocks\RelationManagers;

use App\Filament\Resources\AssessmentContexts\AssessmentContextResource;
use App\Models\AssessmentContext;
use App\Services\Content\AssessmentEditorialContentUpdateService;
use Filament\Actions\Action;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Notifications\Notification;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Illuminate\Support\Str;

class ContextsRelationManager extends RelationManager
{
    protected static string $relationship = 'contexts';

    protected static ?string $title = 'Contexto base del bloque';

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
                    ->label('Editar contexto base')
                    ->icon('heroicon-o-pencil-square')
                    ->color('primary')
                    ->slideOver()
                    ->modalWidth('6xl')
                    ->modalHeading('Editar contexto base del bloque')
                    ->modalDescription('Primero corrige la base general del bloque. La clasificación queda como apoyo editorial al final.')
                    ->modalSubmitActionLabel('Guardar contexto')
                    ->fillForm(fn (AssessmentContext $record): array => [
                        'title' => $record->title,
                        'context_mdx' => $record->context_mdx,
                        'teacher_notes' => $record->teacher_notes,
                    ])
                    ->schema([
                        Textarea::make('context_mdx')
                            ->label('Contexto (Markdown)')
                            ->rows(16)
                            ->required()
                            ->helperText('Aquí ajustas el texto base que dará sentido a las preguntas del bloque.')
                            ->columnSpanFull(),
                        TextInput::make('title')
                            ->label('Título breve del contexto')
                            ->helperText('Opcional. Sirve para identificar el bloque, pero no es lo central del trabajo editorial.')
                            ->maxLength(255)
                            ->columnSpanFull(),
                        Textarea::make('teacher_notes')
                            ->label('Notas docentes')
                            ->rows(4)
                            ->helperText('Úsalo solo si necesitas dejar observaciones internas para revisión posterior.')
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
            ->emptyStateHeading('Este bloque todavía no tiene contexto base.');
    }
}
