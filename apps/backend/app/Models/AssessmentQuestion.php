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

    protected static function booted(): void
    {
        static::saving(function (self $question): void {
            $subject = $question->subject_id ? AssessmentSubject::query()->find($question->subject_id) : null;
            $unit = $question->unit_id ? AssessmentUnit::query()->find($question->unit_id) : null;
            $originCollection = $question->origin_collection_id ? AssessmentOriginCollection::query()->find($question->origin_collection_id) : null;

            $question->subject_label = $subject?->label;
            $question->unit_label = $unit?->label;
            $question->origin_label = $originCollection?->label;
        });
    }

    protected $fillable = [
        'template_id',
        'external_id',
        'order_base',
        'source_slug',
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
            'subject_id' => 'integer',
            'unit_id' => 'integer',
            'origin_collection_id' => 'integer',
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

    public function questionOptions(): HasMany
    {
        return $this->hasMany(AssessmentQuestionOption::class, 'question_id')->orderBy('order_base');
    }

    public function attemptAnswers(): HasMany
    {
        return $this->hasMany(AssessmentAttemptAnswer::class, 'question_id');
    }

    public function bookletQuestions(): HasMany
    {
        return $this->hasMany(AssessmentBookletQuestion::class, 'question_id')->orderBy('order_base');
    }

    public function booklets(): BelongsToMany
    {
        return $this->belongsToMany(
            AssessmentBooklet::class,
            'assessment_booklet_questions',
            'question_id',
            'booklet_id'
        )->withPivot(['booklet_section_id', 'order_base'])->withTimestamps();
    }

    public function bookletSections(): BelongsToMany
    {
        return $this->belongsToMany(
            AssessmentBookletSection::class,
            'assessment_booklet_questions',
            'question_id',
            'booklet_section_id'
        )->withPivot(['booklet_id', 'order_base'])->withTimestamps();
    }

    public function getSourceKeyAttribute(): string
    {
        $templateExternalId = $this->template?->external_id ?: ('template:'.$this->template_id);

        return $templateExternalId.'#question:'.trim((string) $this->external_id);
    }
}
