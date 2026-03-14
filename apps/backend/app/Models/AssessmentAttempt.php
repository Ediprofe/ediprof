<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Support\Str;

class AssessmentAttempt extends Model
{
    use HasFactory;

    protected $fillable = [
        'external_id',
        'assignment_id',
        'template_id',
        'user_id',
        'mode',
        'status',
        'question_order',
        'questions_snapshot',
        'total_questions',
        'score_raw',
        'score_percent',
        'score_scale',
        'started_at',
        'submitted_at',
        'graded_at',
        'review_released_at',
        'last_activity_at',
        'settings_snapshot',
        'meta',
    ];

    protected function casts(): array
    {
        return [
            'question_order' => 'array',
            'questions_snapshot' => 'array',
            'total_questions' => 'integer',
            'score_raw' => 'integer',
            'score_percent' => 'integer',
            'score_scale' => 'decimal:2',
            'started_at' => 'datetime',
            'submitted_at' => 'datetime',
            'graded_at' => 'datetime',
            'review_released_at' => 'datetime',
            'last_activity_at' => 'datetime',
            'settings_snapshot' => 'array',
            'meta' => 'array',
        ];
    }

    protected static function booted(): void
    {
        static::creating(function (self $attempt): void {
            if (! filled($attempt->external_id)) {
                $attempt->external_id = (string) Str::ulid();
            }
        });
    }

    public function assignment(): BelongsTo
    {
        return $this->belongsTo(AssessmentAssignment::class, 'assignment_id');
    }

    public function template(): BelongsTo
    {
        return $this->belongsTo(AssessmentTemplate::class, 'template_id');
    }

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }

    public function answers(): HasMany
    {
        return $this->hasMany(AssessmentAttemptAnswer::class, 'attempt_id')->orderBy('position');
    }
}
