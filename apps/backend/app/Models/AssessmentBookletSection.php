<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;

class AssessmentBookletSection extends Model
{
    use HasFactory;

    protected static function booted(): void
    {
        static::saving(function (self $section): void {
            $subject = $section->subject_id ? AssessmentSubject::query()->find($section->subject_id) : null;
            $unit = $section->default_unit_id ? AssessmentUnit::query()->find($section->default_unit_id) : null;

            $section->subject_label = $subject?->label;
            $section->default_unit_label = $unit?->label;
        });
    }

    protected $fillable = [
        'booklet_id',
        'external_id',
        'title',
        'subject_id',
        'subject_label',
        'default_unit_id',
        'default_unit_label',
        'template_id',
        'order_base',
        'total_questions',
        'metadata',
    ];

    protected function casts(): array
    {
        return [
            'booklet_id' => 'integer',
            'subject_id' => 'integer',
            'default_unit_id' => 'integer',
            'template_id' => 'integer',
            'order_base' => 'integer',
            'total_questions' => 'integer',
            'metadata' => 'array',
        ];
    }

    public function booklet(): BelongsTo
    {
        return $this->belongsTo(AssessmentBooklet::class, 'booklet_id');
    }

    public function subject(): BelongsTo
    {
        return $this->belongsTo(AssessmentSubject::class, 'subject_id');
    }

    public function defaultUnit(): BelongsTo
    {
        return $this->belongsTo(AssessmentUnit::class, 'default_unit_id');
    }

    public function template(): BelongsTo
    {
        return $this->belongsTo(AssessmentTemplate::class, 'template_id');
    }

    public function bookletQuestions(): HasMany
    {
        return $this->hasMany(AssessmentBookletQuestion::class, 'booklet_section_id')->orderBy('order_base');
    }

    public function questions(): BelongsToMany
    {
        return $this->belongsToMany(
            AssessmentQuestion::class,
            'assessment_booklet_questions',
            'booklet_section_id',
            'question_id'
        )->withPivot(['booklet_id', 'order_base'])->withTimestamps();
    }
}
