<?php

namespace App\Filament\Resources\AssessmentUnits;

use App\Filament\Resources\AssessmentUnits\Pages\CreateAssessmentUnit;
use App\Filament\Resources\AssessmentUnits\Pages\EditAssessmentUnit;
use App\Filament\Resources\AssessmentUnits\Pages\ListAssessmentUnits;
use App\Filament\Resources\AssessmentUnits\Schemas\AssessmentUnitForm;
use App\Filament\Resources\AssessmentUnits\Tables\AssessmentUnitsTable;
use App\Models\AssessmentUnit;
use BackedEnum;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Table;
use UnitEnum;

class AssessmentUnitResource extends Resource
{
    protected static ?string $model = AssessmentUnit::class;

    protected static ?string $modelLabel = 'unidad';

    protected static ?string $pluralModelLabel = 'unidades';

    protected static ?string $recordTitleAttribute = 'label';

    protected static string|UnitEnum|null $navigationGroup = 'Banco académico';

    protected static ?string $navigationLabel = 'Unidades';

    protected static ?int $navigationSort = 12;

    protected static string|BackedEnum|null $navigationIcon = Heroicon::OutlinedRectangleStack;

    public static function form(Schema $schema): Schema
    {
        return AssessmentUnitForm::configure($schema);
    }

    public static function table(Table $table): Table
    {
        return AssessmentUnitsTable::configure($table);
    }

    public static function getPages(): array
    {
        return [
            'index' => ListAssessmentUnits::route('/'),
            'create' => CreateAssessmentUnit::route('/create'),
            'edit' => EditAssessmentUnit::route('/{record}/edit'),
        ];
    }
}
