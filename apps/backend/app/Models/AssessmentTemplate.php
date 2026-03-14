<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

class AssessmentTemplate extends Model
{
    use HasFactory;

    protected $fillable = [
        'external_id',
        'source_workshop_id',
        'title',
        'source_content_type',
        'default_mode',
        'route',
        'area_slug',
        'unidad_slug',
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

    public function attempts(): HasMany
    {
        return $this->hasMany(AssessmentAttempt::class, 'template_id');
    }
}
