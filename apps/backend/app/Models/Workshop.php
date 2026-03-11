<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Workshop extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var list<string>
     */
    protected $fillable = [
        'external_id',
        'content_external_id',
        'content_type',
        'title',
        'route',
        'area_slug',
        'unidad_slug',
        'access_tier',
        'is_published',
        'total_questions',
        'total_assets',
        'assets',
        'questions',
        'metadata',
        'synced_at',
    ];

    /**
     * The attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'content_type' => 'string',
            'is_published' => 'boolean',
            'total_questions' => 'integer',
            'total_assets' => 'integer',
            'assets' => 'array',
            'questions' => 'array',
            'metadata' => 'array',
            'synced_at' => 'datetime',
        ];
    }

    /**
     * @return HasMany<CourseContent, $this>
     */
    public function courseContents(): HasMany
    {
        return $this->hasMany(CourseContent::class);
    }
}
