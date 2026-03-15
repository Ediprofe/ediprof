<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

class AssessmentTemplate extends Model
{
    use HasFactory;

    protected static function booted(): void
    {
        static::saving(function (self $template): void {
            $subject = $template->subject_id ? AssessmentSubject::query()->find($template->subject_id) : null;
            $unit = $template->unit_id ? AssessmentUnit::query()->find($template->unit_id) : null;
            $originCollection = $template->origin_collection_id ? AssessmentOriginCollection::query()->find($template->origin_collection_id) : null;

            $template->subject_label = $subject?->label;
            $template->unit_label = $unit?->label;
            $template->origin_label = $originCollection?->label;

            if ($originCollection) {
                $template->source_content_type = $originCollection->origin_type;
            }
        });
    }

    protected $fillable = [
        'external_id',
        'source_workshop_id',
        'title',
        'subject_id',
        'subject_label',
        'source_content_type',
        'default_mode',
        'route',
        'area_slug',
        'unidad_slug',
        'unit_id',
        'unit_label',
        'origin_collection_id',
        'origin_label',
        'editorial_status',
        'access_tier',
        'is_published',
        'total_questions',
        'total_assets',
        'assets',
        'asset_refs',
        'metadata',
        'synced_at',
    ];

    protected function casts(): array
    {
        return [
            'is_published' => 'boolean',
            'subject_id' => 'integer',
            'unit_id' => 'integer',
            'origin_collection_id' => 'integer',
            'total_questions' => 'integer',
            'total_assets' => 'integer',
            'assets' => 'array',
            'asset_refs' => 'array',
            'metadata' => 'array',
            'synced_at' => 'datetime',
        ];
    }

    public function sourceWorkshop(): BelongsTo
    {
        return $this->belongsTo(Workshop::class, 'source_workshop_id');
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

    public function contexts(): HasMany
    {
        return $this->hasMany(AssessmentContext::class, 'template_id')->orderBy('order_base');
    }

    public function questions(): HasMany
    {
        return $this->hasMany(AssessmentQuestion::class, 'template_id')->orderBy('order_base');
    }

    public function assignments(): HasMany
    {
        return $this->hasMany(AssessmentAssignment::class, 'template_id');
    }

    public function bookletSections(): HasMany
    {
        return $this->hasMany(AssessmentBookletSection::class, 'template_id')->orderBy('order_base');
    }

    public function attempts(): HasMany
    {
        return $this->hasMany(AssessmentAttempt::class, 'template_id');
    }
}
