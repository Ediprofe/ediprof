<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Support\Str;

class AssessmentAssignment extends Model
{
    use HasFactory;

    public const MODE_STUDY = 'study';

    public const MODE_SIMULACRO = 'simulacro';

    public const MODE_EVALUATION = 'evaluation';

    public const STATUS_DRAFT = 'draft';

    public const STATUS_ACTIVE = 'active';

    public const STATUS_CLOSED = 'closed';

    public const STATUS_ARCHIVED = 'archived';

    protected $fillable = [
        'external_id',
        'course_id',
        'template_id',
        'title',
        'mode',
        'status',
        'randomize_questions',
        'show_feedback_on_submit',
        'show_feedback_after_close',
        'max_attempts',
        'time_limit_minutes',
        'opens_at',
        'closes_at',
        'review_released_at',
        'settings',
    ];

    protected function casts(): array
    {
        return [
            'randomize_questions' => 'boolean',
            'show_feedback_on_submit' => 'boolean',
            'show_feedback_after_close' => 'boolean',
            'max_attempts' => 'integer',
            'time_limit_minutes' => 'integer',
            'opens_at' => 'datetime',
            'closes_at' => 'datetime',
            'review_released_at' => 'datetime',
            'settings' => 'array',
        ];
    }

    protected static function booted(): void
    {
        static::creating(function (self $assignment): void {
            if (! filled($assignment->external_id)) {
                $assignment->external_id = (string) Str::ulid();
            }
        });
    }

    public function course(): BelongsTo
    {
        return $this->belongsTo(Course::class);
    }

    public function template(): BelongsTo
    {
        return $this->belongsTo(AssessmentTemplate::class, 'template_id');
    }

    public function questions(): HasMany
    {
        return $this->hasMany(AssessmentAssignmentQuestion::class, 'assignment_id')->orderBy('order_base');
    }

    public function attempts(): HasMany
    {
        return $this->hasMany(AssessmentAttempt::class, 'assignment_id');
    }

    /**
     * @return array<string, string>
     */
    public static function modeOptions(): array
    {
        return [
            self::MODE_STUDY => 'Estudio guiado',
            self::MODE_SIMULACRO => 'Simulacro',
            self::MODE_EVALUATION => 'Evaluación',
        ];
    }

    /**
     * @return array<string, string>
     */
    public static function statusOptions(): array
    {
        return [
            self::STATUS_DRAFT => 'Borrador',
            self::STATUS_ACTIVE => 'Activa',
            self::STATUS_CLOSED => 'Cerrada',
            self::STATUS_ARCHIVED => 'Archivada',
        ];
    }
}
