<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class AssessmentContext extends Model
{
    use HasFactory;

    protected static function booted(): void
    {
        static::saving(function (self $context): void {
            $subject = $context->subject_id ? AssessmentSubject::query()->find($context->subject_id) : null;
            $unit = $context->unit_id ? AssessmentUnit::query()->find($context->unit_id) : null;
            $originCollection = $context->origin_collection_id ? AssessmentOriginCollection::query()->find($context->origin_collection_id) : null;

            $context->subject_label = $subject?->label;
            $context->unit_label = $unit?->label;
            $context->origin_label = $originCollection?->label;
        });
    }

    protected $fillable = [
        'template_id',
        'external_id',
        'title',
        'subject_id',
        'subject_label',
        'topic',
        'unit_id',
        'unit_label',
        'subtopic',
        'origin_collection_id',
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
            'subject_id' => 'integer',
            'unit_id' => 'integer',
            'origin_collection_id' => 'integer',
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

    public function subject(): BelongsTo
    {
        return $this->belongsTo(AssessmentSubject::class, 'subject_id');
    }

    public function unit(): BelongsTo
    {
        return $this->belongsTo(AssessmentUnit::class, 'unit_id');
    }

    public function originCollection(): BelongsTo
    {
        return $this->belongsTo(AssessmentOriginCollection::class, 'origin_collection_id');
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
