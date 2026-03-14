<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class AssessmentAttemptAnswer extends Model
{
    use HasFactory;

    protected $fillable = [
        'attempt_id',
        'question_id',
        'question_external_id',
        'position',
        'selected_option_id',
        'is_correct',
        'answered_at',
        'meta',
    ];

    protected function casts(): array
    {
        return [
            'position' => 'integer',
            'is_correct' => 'boolean',
            'answered_at' => 'datetime',
            'meta' => 'array',
        ];
    }

    public function attempt(): BelongsTo
    {
        return $this->belongsTo(AssessmentAttempt::class, 'attempt_id');
    }

    public function question(): BelongsTo
    {
        return $this->belongsTo(AssessmentQuestion::class, 'question_id');
    }
}
