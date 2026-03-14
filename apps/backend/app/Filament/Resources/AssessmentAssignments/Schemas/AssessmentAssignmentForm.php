<?php

namespace App\Filament\Resources\AssessmentAssignments\Schemas;

use App\Models\AssessmentAssignment;
use App\Models\AssessmentTemplate;
use App\Models\Course;
use Filament\Forms\Components\DateTimePicker;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Schema;
use Illuminate\Database\Eloquent\Builder;

class AssessmentAssignmentForm
{
    public static function configure(Schema $schema, bool $includeCourse = true): Schema
    {
        $components = [];

        if ($includeCourse) {
            $components[] = Select::make('course_id')
                ->label('Curso')
                ->relationship(
                    name: 'course',
                    titleAttribute: 'name',
                    modifyQueryUsing: fn (Builder $query) => $query->orderBy('name')
                )
                ->searchable(['name', 'slug'])
                ->preload()
                ->getOptionLabelFromRecordUsing(
                    fn (Course $record): string => "{$record->name}".($record->school_year ? " • {$record->school_year}" : '')
                )
                ->disabledOn('edit')
                ->required();
        }

        $components[] = Select::make('template_id')
            ->label('Plantilla base')
            ->relationship(
                name: 'template',
                titleAttribute: 'title',
                modifyQueryUsing: fn (Builder $query) => $query
                    ->where('is_published', true)
                    ->orderBy('source_content_type')
                    ->orderBy('title')
            )
            ->searchable(['title', 'route', 'external_id'])
            ->preload()
            ->getOptionLabelFromRecordUsing(
                fn (AssessmentTemplate $record): string => "{$record->title} • {$record->source_content_type}"
            )
            ->disabledOn('edit')
            ->helperText('La plantilla queda fija para mantener consistencia entre contextos, preguntas e intentos. Si guardas sin seleccionar preguntas adicionales, la asignación usará toda la plantilla base.')
            ->required();

        array_push(
            $components,
            TextInput::make('title')
                ->label('Título de la asignación')
                ->required()
                ->maxLength(255),
            Select::make('mode')
                ->label('Modo')
                ->options(AssessmentAssignment::modeOptions())
                ->default(AssessmentAssignment::MODE_SIMULACRO)
                ->helperText('En evaluaciones puedes dejar toda la plantilla o, después de guardar, entrar a "Preguntas de la asignación" para elegir solo un subconjunto.')
                ->required(),
            Select::make('status')
                ->label('Estado')
                ->options(AssessmentAssignment::statusOptions())
                ->default(AssessmentAssignment::STATUS_DRAFT)
                ->required(),
            Toggle::make('randomize_questions')
                ->label('Aleatorizar preguntas por estudiante')
                ->helperText('El orden se congela al iniciar el intento y no cambia aunque el estudiante recargue.')
                ->default(false),
            Toggle::make('show_feedback_on_submit')
                ->label('Mostrar retroalimentación al entregar')
                ->helperText('Si está activa, el estudiante verá la respuesta correcta y los conceptos relacionados apenas entregue.')
                ->default(true),
            Toggle::make('show_feedback_after_close')
                ->label('Mostrar retroalimentación al cerrar')
                ->helperText('Útil cuando no quieres mostrar la solución al entregar, pero sí cuando cierres la asignación.')
                ->default(false),
            TextInput::make('max_attempts')
                ->label('Máximo de intentos')
                ->numeric()
                ->minValue(1)
                ->helperText('Déjalo vacío si todavía no quieres limitar los reintentos.')
                ->nullable(),
            TextInput::make('time_limit_minutes')
                ->label('Tiempo límite (minutos)')
                ->numeric()
                ->minValue(1)
                ->nullable(),
            DateTimePicker::make('opens_at')
                ->label('Apertura'),
            DateTimePicker::make('closes_at')
                ->label('Cierre'),
            DateTimePicker::make('review_released_at')
                ->label('Liberar retroalimentación desde')
                ->helperText('Fecha opcional para habilitar la retroalimentación de forma automática, sin esperar al cierre manual.'),
        );

        return $schema->components($components);
    }
}
