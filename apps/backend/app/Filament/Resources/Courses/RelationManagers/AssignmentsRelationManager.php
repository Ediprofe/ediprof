<?php

namespace App\Filament\Resources\Courses\RelationManagers;

use App\Filament\Resources\AssessmentAssignments\AssessmentAssignmentResource;
use App\Filament\Resources\AssessmentAssignments\Schemas\AssessmentAssignmentForm;
use App\Filament\Resources\AssessmentAssignments\Tables\AssessmentAssignmentsTable;
use App\Models\AssessmentAssignment;
use Filament\Actions\CreateAction;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Schemas\Schema;
use Filament\Tables\Table;

class AssignmentsRelationManager extends RelationManager
{
    protected static string $relationship = 'assignments';

    protected static ?string $title = 'Asignaciones académicas';

    public function form(Schema $schema): Schema
    {
        return AssessmentAssignmentForm::configure($schema, includeCourse: false);
    }

    public function table(Table $table): Table
    {
        return AssessmentAssignmentsTable::configure($table, includeCourse: false)
            ->headerActions([
                CreateAction::make()
                    ->label('Nueva asignación'),
            ])
            ->recordUrl(fn (AssessmentAssignment $record): string => AssessmentAssignmentResource::getUrl('edit', ['record' => $record]));
    }
}
