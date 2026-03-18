<?php

namespace App\Filament\Resources\AssessmentQuestions\Pages;

use App\Filament\Resources\AssessmentQuestions\AssessmentQuestionResource;
use App\Filament\Resources\AssessmentQuestions\Schemas\AssessmentQuestionForm;
use App\Models\AssessmentQuestion;
use App\Services\Content\AssessmentQuestionBankCreateService;
use Filament\Resources\Pages\CreateRecord;
use Filament\Schemas\Schema;
use Illuminate\Database\Eloquent\Model;

class CreateAssessmentQuestion extends CreateRecord
{
    protected static string $resource = AssessmentQuestionResource::class;

    public function getTitle(): string
    {
        return 'Agregar pregunta';
    }

    public function getSubheading(): ?string
    {
        return 'Crea una pregunta nueva con su contexto base, sus opciones de respuesta y su clasificación editorial.';
    }

    public function form(Schema $schema): Schema
    {
        return AssessmentQuestionForm::createSchema($schema);
    }

    protected function getHeaderActions(): array
    {
        return [];
    }

    protected function handleRecordCreation(array $data): Model
    {
        return app(AssessmentQuestionBankCreateService::class)->create($data);
    }

    protected function getRedirectUrl(): string
    {
        /** @var AssessmentQuestion $record */
        $record = $this->getRecord();

        return AssessmentQuestionResource::getUrl('edit', ['record' => $record], panel: 'admin');
    }

    protected function getCreatedNotificationTitle(): ?string
    {
        return 'Pregunta agregada al banco';
    }
}
