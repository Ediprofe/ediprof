<?php

namespace App\Filament\Resources\AssessmentSubjects;

use App\Filament\Resources\AssessmentSubjects\Pages\CreateAssessmentSubject;
use App\Filament\Resources\AssessmentSubjects\Pages\EditAssessmentSubject;
use App\Filament\Resources\AssessmentSubjects\Pages\ListAssessmentSubjects;
use App\Filament\Resources\AssessmentSubjects\Schemas\AssessmentSubjectForm;
use App\Filament\Resources\AssessmentSubjects\Tables\AssessmentSubjectsTable;
use App\Models\AssessmentSubject;
use BackedEnum;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Table;
use UnitEnum;

class AssessmentSubjectResource extends Resource
{
    protected static ?string $model = AssessmentSubject::class;

    protected static ?string $modelLabel = 'materia';

    protected static ?string $pluralModelLabel = 'materias';

    protected static ?string $recordTitleAttribute = 'label';

    protected static string|UnitEnum|null $navigationGroup = 'Banco académico';

    protected static ?string $navigationLabel = 'Materias';

    protected static ?int $navigationSort = 11;

    protected static string|BackedEnum|null $navigationIcon = Heroicon::OutlinedBookOpen;

    public static function form(Schema $schema): Schema
    {
        return AssessmentSubjectForm::configure($schema);
    }

    public static function table(Table $table): Table
    {
        return AssessmentSubjectsTable::configure($table);
    }

    public static function getPages(): array
    {
        return [
            'index' => ListAssessmentSubjects::route('/'),
            'create' => CreateAssessmentSubject::route('/create'),
            'edit' => EditAssessmentSubject::route('/{record}/edit'),
        ];
    }
}
