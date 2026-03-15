<?php

namespace App\Filament\Resources\AssessmentBlocks;

use App\Filament\Resources\AssessmentBlocks\Pages\EditAssessmentBlock;
use App\Filament\Resources\AssessmentBlocks\Pages\ListAssessmentBlocks;
use App\Filament\Resources\AssessmentBlocks\RelationManagers\ContextsRelationManager;
use App\Filament\Resources\AssessmentBlocks\RelationManagers\QuestionsRelationManager;
use App\Filament\Resources\AssessmentBlocks\Schemas\AssessmentBlockForm;
use App\Filament\Resources\AssessmentBlocks\Tables\AssessmentBlocksTable;
use App\Models\AssessmentTemplate;
use BackedEnum;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;
use UnitEnum;

class AssessmentBlockResource extends Resource
{
    protected static ?string $model = AssessmentTemplate::class;

    protected static ?string $modelLabel = 'bloque contextual';

    protected static ?string $pluralModelLabel = 'bloques contextuales';

    protected static ?string $recordTitleAttribute = 'title';

    protected static string|UnitEnum|null $navigationGroup = 'Banco académico';

    protected static ?string $navigationLabel = 'Bloques';

    protected static ?int $navigationSort = 15;

    protected static string|BackedEnum|null $navigationIcon = Heroicon::OutlinedDocumentText;

    public static function form(Schema $schema): Schema
    {
        return AssessmentBlockForm::configure($schema);
    }

    public static function table(Table $table): Table
    {
        return AssessmentBlocksTable::configure($table);
    }

    public static function getRelations(): array
    {
        return [
            ContextsRelationManager::class,
            QuestionsRelationManager::class,
        ];
    }

    public static function getPages(): array
    {
        return [
            'index' => ListAssessmentBlocks::route('/'),
            'edit' => EditAssessmentBlock::route('/{record}/edit'),
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

    public static function getEloquentQuery(): Builder
    {
        return parent::getEloquentQuery()
            ->whereNull('route')
            ->where('access_tier', 'private');
    }
}
