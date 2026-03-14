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
        'topic',
        'unit_label',
        'subtopic',
        'origin_label',
        'editorial_status',
        'tags',
        'teacher_notes',
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
            'tags' => 'array',
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

    public function getSourceKeyAttribute(): string
    {
        $templateExternalId = $this->template?->external_id ?: ('template:'.$this->template_id);

        return $templateExternalId.'#context:'.trim((string) $this->external_id);
    }
}
