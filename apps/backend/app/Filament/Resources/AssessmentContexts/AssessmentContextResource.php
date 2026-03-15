<?php

namespace App\Filament\Resources\AssessmentContexts;

use App\Filament\Resources\AssessmentContexts\Pages\EditAssessmentContext;
use App\Filament\Resources\AssessmentContexts\Pages\ListAssessmentContexts;
use App\Filament\Resources\AssessmentContexts\Schemas\AssessmentContextForm;
use App\Filament\Resources\AssessmentContexts\Tables\AssessmentContextsTable;
use App\Models\AssessmentContext;
use BackedEnum;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Table;
use UnitEnum;

class AssessmentContextResource extends Resource
{
    protected static ?string $model = AssessmentContext::class;

    protected static ?string $modelLabel = 'contexto del banco';

    protected static ?string $pluralModelLabel = 'contextos del banco';

    protected static ?string $recordTitleAttribute = 'external_id';

    protected static string|UnitEnum|null $navigationGroup = 'Banco académico';

    protected static ?string $navigationLabel = 'Contextos (detalle)';

    protected static ?int $navigationSort = 70;

    protected static string|BackedEnum|null $navigationIcon = Heroicon::OutlinedRectangleStack;

    public static function form(Schema $schema): Schema
    {
        return AssessmentContextForm::configure($schema);
    }

    public static function table(Table $table): Table
    {
        return AssessmentContextsTable::configure($table);
    }

    public static function getPages(): array
    {
        return [
            'index' => ListAssessmentContexts::route('/'),
            'edit' => EditAssessmentContext::route('/{record}/edit'),
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
