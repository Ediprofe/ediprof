<?php

namespace App\Filament\Resources\AssessmentQuestions;

use App\Filament\Resources\AssessmentQuestions\Pages\EditAssessmentQuestion;
use App\Filament\Resources\AssessmentQuestions\Pages\ListAssessmentQuestions;
use App\Filament\Resources\AssessmentQuestions\Schemas\AssessmentQuestionForm;
use App\Filament\Resources\AssessmentQuestions\Tables\AssessmentQuestionsTable;
use App\Models\AssessmentQuestion;
use BackedEnum;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Table;
use UnitEnum;

class AssessmentQuestionResource extends Resource
{
    protected static ?string $model = AssessmentQuestion::class;

    protected static ?string $modelLabel = 'pregunta del banco';

    protected static ?string $pluralModelLabel = 'preguntas del banco';

    protected static ?string $recordTitleAttribute = 'external_id';

    protected static string|UnitEnum|null $navigationGroup = 'Banco académico';

    protected static ?string $navigationLabel = 'Preguntas (detalle)';

    protected static ?int $navigationSort = 60;

    protected static string|BackedEnum|null $navigationIcon = Heroicon::OutlinedRectangleStack;

    public static function form(Schema $schema): Schema
    {
        return AssessmentQuestionForm::configure($schema);
    }

    public static function table(Table $table): Table
    {
        return AssessmentQuestionsTable::configure($table);
    }

    public static function getPages(): array
    {
        return [
            'index' => ListAssessmentQuestions::route('/'),
            'edit' => EditAssessmentQuestion::route('/{record}/edit'),
        ];
    }

    public static function canCreate(): bool
    {
        return false;
    }

    public static function canDelete($record): bool
    {
        return false;
    }
}
