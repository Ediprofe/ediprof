<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class AssessmentQuestionContext extends Model
{
    use HasFactory;

    protected $fillable = [
        'question_id',
        'context_id',
        'order_base',
    ];

    protected function casts(): array
    {
        return [
            'order_base' => 'integer',
        ];
    }

    public function question(): BelongsTo
    {
        return $this->belongsTo(AssessmentQuestion::class, 'question_id');
    }

    public function context(): BelongsTo
    {
        return $this->belongsTo(AssessmentContext::class, 'context_id');
    }
}
