<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class AssessmentContext extends Model
{
    use HasFactory;

    protected $fillable = [
        'template_id',
        'external_id',
        'title',
        'order_base',
        'is_active',
        'context_mdx',
        'context_html',
        'context_assets',
        'context_blocks',
        'metadata',
    ];

    protected function casts(): array
    {
        return [
            'order_base' => 'integer',
            'is_active' => 'boolean',
            'context_assets' => 'array',
            'context_blocks' => 'array',
            'metadata' => 'array',
        ];
    }

    public function template(): BelongsTo
    {
        return $this->belongsTo(AssessmentTemplate::class, 'template_id');
    }

    public function questions(): BelongsToMany
    {
        return $this->belongsToMany(
            AssessmentQuestion::class,
            'assessment_question_contexts',
            'context_id',
            'question_id'
        )->withPivot(['order_base'])->withTimestamps();
    }
}
