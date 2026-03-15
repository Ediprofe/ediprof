<?php

namespace App\Filament\Resources\AssessmentOriginCollections;

use App\Filament\Resources\AssessmentOriginCollections\Pages\CreateAssessmentOriginCollection;
use App\Filament\Resources\AssessmentOriginCollections\Pages\EditAssessmentOriginCollection;
use App\Filament\Resources\AssessmentOriginCollections\Pages\ListAssessmentOriginCollections;
use App\Filament\Resources\AssessmentOriginCollections\Schemas\AssessmentOriginCollectionForm;
use App\Filament\Resources\AssessmentOriginCollections\Tables\AssessmentOriginCollectionsTable;
use App\Models\AssessmentOriginCollection;
use BackedEnum;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Table;
use UnitEnum;

class AssessmentOriginCollectionResource extends Resource
{
    protected static ?string $model = AssessmentOriginCollection::class;

    protected static ?string $modelLabel = 'origen';

    protected static ?string $pluralModelLabel = 'orígenes';

    protected static ?string $recordTitleAttribute = 'label';

    protected static string|UnitEnum|null $navigationGroup = 'Banco académico';

    protected static ?string $navigationLabel = 'Orígenes';

    protected static ?int $navigationSort = 13;

    protected static string|BackedEnum|null $navigationIcon = Heroicon::OutlinedFolder;

    public static function form(Schema $schema): Schema
    {
        return AssessmentOriginCollectionForm::configure($schema);
    }

    public static function table(Table $table): Table
    {
        return AssessmentOriginCollectionsTable::configure($table);
    }

    public static function getPages(): array
    {
        return [
            'index' => ListAssessmentOriginCollections::route('/'),
            'create' => CreateAssessmentOriginCollection::route('/create'),
            'edit' => EditAssessmentOriginCollection::route('/{record}/edit'),
        ];
    }
}
