<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

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
            'is_published' => 'boolean',
            'total_questions' => 'integer',
            'total_assets' => 'integer',
            'assets' => 'array',
            'questions' => 'array',
            'metadata' => 'array',
            'synced_at' => 'datetime',
        ];
    }
}
