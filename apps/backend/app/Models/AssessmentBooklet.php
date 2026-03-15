<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Support\Str;

class AssessmentBooklet extends Model
{
    use HasFactory;

    protected static function booted(): void
    {
        static::creating(function (self $booklet): void {
            if (! filled($booklet->external_id)) {
                $booklet->external_id = (string) Str::ulid();
            }
        });

        static::saving(function (self $booklet): void {
            $originCollection = $booklet->origin_collection_id
                ? AssessmentOriginCollection::query()->find($booklet->origin_collection_id)
                : null;

            $booklet->origin_label = $originCollection?->label;
        });
    }

    protected $fillable = [
        'external_id',
        'title',
        'booklet_type',
        'origin_collection_id',
        'origin_label',
        'applied_on',
        'school_year',
        'editorial_status',
        'is_active',
        'total_sections',
        'total_questions',
        'notes',
        'metadata',
    ];

    protected function casts(): array
    {
        return [
            'origin_collection_id' => 'integer',
            'applied_on' => 'date',
            'is_active' => 'boolean',
            'total_sections' => 'integer',
            'total_questions' => 'integer',
            'metadata' => 'array',
        ];
    }

    public function originCollection(): BelongsTo
    {
        return $this->belongsTo(AssessmentOriginCollection::class, 'origin_collection_id');
    }

    public function sections(): HasMany
    {
        return $this->hasMany(AssessmentBookletSection::class, 'booklet_id')->orderBy('order_base');
    }

    public function bookletQuestions(): HasMany
    {
        return $this->hasMany(AssessmentBookletQuestion::class, 'booklet_id')->orderBy('order_base');
    }

    public function questions(): BelongsToMany
    {
        return $this->belongsToMany(
            AssessmentQuestion::class,
            'assessment_booklet_questions',
            'booklet_id',
            'question_id'
        )->withPivot(['booklet_section_id', 'order_base'])->withTimestamps();
    }
}
