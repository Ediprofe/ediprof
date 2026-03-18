<?php

namespace App\Filament\Resources\AssessmentQuestions\Pages;

use App\Filament\Resources\AssessmentQuestions\AssessmentQuestionResource;
use App\Models\AssessmentQuestion;
use Filament\Actions\Action;
use Filament\Resources\Pages\ListRecords;
use Filament\Schemas\Components\Tabs\Tab;
use Illuminate\Database\Eloquent\Builder;

class ListAssessmentQuestions extends ListRecords
{
    protected static string $resource = AssessmentQuestionResource::class;

    public function getTitle(): string
    {
        return 'Banco de preguntas';
    }

    public function getSubheading(): ?string
    {
        return null;
    }

    protected function getHeaderActions(): array
    {
        return [
            Action::make('createQuestion')
                ->label('Agregar pregunta')
                ->icon('heroicon-o-plus')
                ->tooltip('Crea una nueva pregunta del banco con su contexto base y sus opciones de respuesta.')
                ->url(AssessmentQuestionResource::getUrl('create', panel: 'admin')),
        ];
    }

    public function getTabs(): array
    {
        return [
            'todas' => Tab::make('Todas')
                ->badge((string) AssessmentQuestion::query()->count()),
            'listas' => Tab::make('Listas para usar')
                ->badge((string) AssessmentQuestion::query()->where('editorial_status', 'ready')->count())
                ->modifyQueryUsing(fn (Builder $query): Builder => $query->where('editorial_status', 'ready')),
            'sin-unidad' => Tab::make('Sin unidad')
                ->badge((string) AssessmentQuestion::query()->whereNull('unit_id')->count())
                ->modifyQueryUsing(fn (Builder $query): Builder => $query->whereNull('unit_id')),
            'revision' => Tab::make('En revisión')
                ->badge((string) AssessmentQuestion::query()->where('editorial_status', 'review')->count())
                ->modifyQueryUsing(fn (Builder $query): Builder => $query->where('editorial_status', 'review')),
            'borrador' => Tab::make('En borrador')
                ->badge((string) AssessmentQuestion::query()->where('editorial_status', 'draft')->count())
                ->modifyQueryUsing(fn (Builder $query): Builder => $query->where('editorial_status', 'draft')),
        ];
    }
}
