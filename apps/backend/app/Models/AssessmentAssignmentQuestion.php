<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class AssessmentAssignmentQuestion extends Model
{
    use HasFactory;

    protected $fillable = [
        'assignment_id',
        'question_id',
        'selection_group_key',
        'order_base',
    ];

    protected function casts(): array
    {
        return [
            'order_base' => 'integer',
        ];
    }

    public function assignment(): BelongsTo
    {
        return $this->belongsTo(AssessmentAssignment::class, 'assignment_id');
    }

    public function question(): BelongsTo
    {
        return $this->belongsTo(AssessmentQuestion::class, 'question_id');
    }
}
