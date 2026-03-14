<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;

class AssessmentQuestion extends Model
{
    use HasFactory;

    protected $fillable = [
        'template_id',
        'external_id',
        'order_base',
        'source_slug',
        'topic',
        'unit_label',
        'subtopic',
        'origin_label',
        'editorial_status',
        'tags',
        'teacher_notes',
        'is_active',
        'meta',
        'stem_mdx',
        'stem_html',
        'stem_assets',
        'stem_blocks',
        'options',
        'correct_option_id',
        'feedback_mdx',
        'feedback_html',
        'feedback_summary',
        'feedback_assets',
        'feedback_blocks',
        'concepts_mdx',
        'concepts_html',
        'concepts_summary',
        'concepts_assets',
        'concepts_blocks',
        'app_payload_version',
    ];

    protected function casts(): array
    {
        return [
            'order_base' => 'integer',
            'is_active' => 'boolean',
            'tags' => 'array',
            'meta' => 'array',
            'stem_assets' => 'array',
            'stem_blocks' => 'array',
            'options' => 'array',
            'feedback_assets' => 'array',
            'feedback_blocks' => 'array',
            'concepts_assets' => 'array',
            'concepts_blocks' => 'array',
            'app_payload_version' => 'integer',
        ];
    }

    public function template(): BelongsTo
    {
        return $this->belongsTo(AssessmentTemplate::class, 'template_id');
    }

    public function contexts(): BelongsToMany
    {
        return $this->belongsToMany(
            AssessmentContext::class,
            'assessment_question_contexts',
            'question_id',
            'context_id'
        )->withPivot(['order_base'])->withTimestamps();
    }

    public function assignmentQuestions(): HasMany
    {
        return $this->hasMany(AssessmentAssignmentQuestion::class, 'question_id');
    }

    public function attemptAnswers(): HasMany
    {
        return $this->hasMany(AssessmentAttemptAnswer::class, 'question_id');
    }

    public function getSourceKeyAttribute(): string
    {
        $templateExternalId = $this->template?->external_id ?: ('template:'.$this->template_id);

        return $templateExternalId.'#question:'.trim((string) $this->external_id);
    }
}
