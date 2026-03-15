<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class AssessmentQuestionOption extends Model
{
    use HasFactory;

    protected $fillable = [
        'question_id',
        'option_id',
        'order_base',
        'is_correct',
        'plain_text',
        'html_web',
        'nodes_mobile',
        'asset_refs',
        'metadata',
    ];

    protected function casts(): array
    {
        return [
            'order_base' => 'integer',
            'is_correct' => 'boolean',
            'nodes_mobile' => 'array',
            'asset_refs' => 'array',
            'metadata' => 'array',
        ];
    }

    public function question(): BelongsTo
    {
        return $this->belongsTo(AssessmentQuestion::class, 'question_id');
    }
}
