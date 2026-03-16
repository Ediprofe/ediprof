<?php

namespace App\Filament\Resources\AssessmentBlocks\Pages;

use App\Filament\Resources\AssessmentBlocks\AssessmentBlockResource;
use App\Filament\Resources\AssessmentBlocks\RelationManagers\ContextsRelationManager;
use App\Filament\Resources\AssessmentBlocks\RelationManagers\QuestionsRelationManager;
use Filament\Actions\Action;
use Filament\Resources\Pages\EditRecord;
use Filament\Schemas\Components\Livewire;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;

class EditAssessmentBlock extends EditRecord
{
    protected static string $resource = AssessmentBlockResource::class;

    public function getSubheading(): ?string
    {
        return 'Trabaja el bloque como una pieza editorial: primero el contexto base y luego las preguntas que nacen de ese contexto.';
    }

    protected function getHeaderActions(): array
    {
        return [
            Action::make('previewWeb')
                ->label('Abrir preview web')
                ->icon('heroicon-o-globe-alt')
                ->url(fn (): string => route('admin.assessment_drafts.preview_web', $this->getRecord()), shouldOpenInNewTab: true),
        ];
    }

    public function content(Schema $schema): Schema
    {
        return $schema
            ->components([
                $this->getFormContentComponent(),
                Section::make('Mesa editorial del bloque')
                    ->description('Aquí trabajas el bloque de forma corrida: primero el contexto base y luego las preguntas con su parte pedagógica.')
                    ->components([
                        Livewire::make(ContextsRelationManager::class, [
                            'ownerRecord' => $this->getRecord(),
                            'pageClass' => static::class,
                        ])->key('editorial-context-base'),
                        Livewire::make(QuestionsRelationManager::class, [
                            'ownerRecord' => $this->getRecord(),
                            'pageClass' => static::class,
                        ])->key('editorial-question-list'),
                    ]),
            ]);
    }
}
