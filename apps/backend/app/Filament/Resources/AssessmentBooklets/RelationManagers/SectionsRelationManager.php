<?php

namespace App\Filament\Resources\AssessmentBooklets\RelationManagers;

use App\Models\AssessmentBookletSection;
use App\Models\AssessmentUnit;
use Filament\Actions\EditAction;
use Filament\Forms\Components\Placeholder;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Schemas\Schema;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;

class SectionsRelationManager extends RelationManager
{
    protected static string $relationship = 'sections';

    protected static ?string $title = 'Bloques del cuadernillo';

    public function form(Schema $schema): Schema
    {
        return $schema->components([
            Placeholder::make('subject_summary')
                ->label('Materia')
                ->content(fn (?AssessmentBookletSection $record): string => $record?->subject_label ?? 'Sin materia asignada'),
            TextInput::make('title')
                ->label('Título visible')
                ->required()
                ->maxLength(255),
            Select::make('default_unit_id')
                ->label('Unidad por defecto')
                ->options(fn (?AssessmentBookletSection $record): array => AssessmentUnit::query()
                    ->where('is_active', true)
                    ->when($record?->subject_id, fn ($query, $subjectId) => $query->where('subject_id', $subjectId))
                    ->orderBy('label')
                    ->pluck('label', 'id')
                    ->all())
                ->searchable()
                ->preload()
                ->native(false)
                ->nullable()
                ->helperText('Solo se muestran unidades de la materia de esta sección. Si no aplica, puedes dejarla diferida.'),
        ]);
    }

    public function table(Table $table): Table
    {
        return $table
            ->recordTitleAttribute('title')
            ->defaultSort('order_base')
            ->columns([
                TextColumn::make('order_base')
                    ->label('#')
                    ->sortable(),
                TextColumn::make('title')
                    ->label('Bloque')
                    ->searchable()
                    ->wrap(),
                TextColumn::make('subject_label')
                    ->label('Materia')
                    ->searchable()
                    ->sortable()
                    ->placeholder('Sin materia'),
                TextColumn::make('default_unit_label')
                    ->label('Unidad por defecto')
                    ->searchable()
                    ->sortable()
                    ->placeholder('Unidad diferida'),
                TextColumn::make('template.title')
                    ->label('Plantilla base')
                    ->wrap(),
                TextColumn::make('total_questions')
                    ->label('Preguntas')
                    ->sortable(),
            ])
            ->recordActions([
                EditAction::make(),
            ])
            ->emptyStateHeading('Este cuadernillo todavía no tiene secciones.');
    }
}
