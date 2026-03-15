<?php

namespace App\Filament\Resources\AssessmentBooklets;

use App\Filament\Resources\AssessmentBooklets\Pages\EditAssessmentBooklet;
use App\Filament\Resources\AssessmentBooklets\Pages\ListAssessmentBooklets;
use App\Filament\Resources\AssessmentBooklets\RelationManagers\QuestionsRelationManager;
use App\Filament\Resources\AssessmentBooklets\RelationManagers\SectionsRelationManager;
use App\Filament\Resources\AssessmentBooklets\Schemas\AssessmentBookletForm;
use App\Filament\Resources\AssessmentBooklets\Tables\AssessmentBookletsTable;
use App\Models\AssessmentBooklet;
use BackedEnum;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Table;
use UnitEnum;

class AssessmentBookletResource extends Resource
{
    protected static ?string $model = AssessmentBooklet::class;

    protected static ?string $modelLabel = 'cuadernillo';

    protected static ?string $pluralModelLabel = 'cuadernillos';

    protected static ?string $recordTitleAttribute = 'title';

    protected static string|UnitEnum|null $navigationGroup = 'Banco académico';

    protected static ?string $navigationLabel = 'Cuadernillos';

    protected static ?int $navigationSort = 20;

    protected static string|BackedEnum|null $navigationIcon = Heroicon::OutlinedDocumentDuplicate;

    public static function form(Schema $schema): Schema
    {
        return AssessmentBookletForm::configure($schema);
    }

    public static function table(Table $table): Table
    {
        return AssessmentBookletsTable::configure($table);
    }

    public static function getRelations(): array
    {
        return [
            SectionsRelationManager::class,
            QuestionsRelationManager::class,
        ];
    }

    public static function getPages(): array
    {
        return [
            'index' => ListAssessmentBooklets::route('/'),
            'edit' => EditAssessmentBooklet::route('/{record}/edit'),
        ];
    }

    public static function canCreate(): bool
    {
        return false;
    }
}
