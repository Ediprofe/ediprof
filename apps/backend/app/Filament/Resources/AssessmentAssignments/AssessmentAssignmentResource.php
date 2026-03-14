<?php

namespace App\Filament\Resources\AssessmentAssignments;

use App\Filament\Resources\AssessmentAssignments\Pages\CreateAssessmentAssignment;
use App\Filament\Resources\AssessmentAssignments\Pages\EditAssessmentAssignment;
use App\Filament\Resources\AssessmentAssignments\Pages\ListAssessmentAssignments;
use App\Filament\Resources\AssessmentAssignments\RelationManagers\QuestionsRelationManager;
use App\Filament\Resources\AssessmentAssignments\Schemas\AssessmentAssignmentForm;
use App\Filament\Resources\AssessmentAssignments\Tables\AssessmentAssignmentsTable;
use App\Models\AssessmentAssignment;
use BackedEnum;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Table;
use UnitEnum;

class AssessmentAssignmentResource extends Resource
{
    protected static ?string $model = AssessmentAssignment::class;

    protected static ?string $modelLabel = 'asignación';

    protected static ?string $pluralModelLabel = 'asignaciones';

    protected static ?string $recordTitleAttribute = 'title';

    protected static string|UnitEnum|null $navigationGroup = 'Académico';

    protected static ?string $navigationLabel = 'Asignaciones';

    protected static ?int $navigationSort = 15;

    protected static string|BackedEnum|null $navigationIcon = Heroicon::OutlinedRectangleStack;

    public static function form(Schema $schema): Schema
    {
        return AssessmentAssignmentForm::configure($schema);
    }

    public static function table(Table $table): Table
    {
        return AssessmentAssignmentsTable::configure($table);
    }

    public static function getRelations(): array
    {
        return [
            QuestionsRelationManager::class,
        ];
    }

    public static function getPages(): array
    {
        return [
            'index' => ListAssessmentAssignments::route('/'),
            'create' => CreateAssessmentAssignment::route('/create'),
            'edit' => EditAssessmentAssignment::route('/{record}/edit'),
        ];
    }
}
