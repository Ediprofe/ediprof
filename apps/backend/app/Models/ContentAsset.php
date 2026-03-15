<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ContentAsset extends Model
{
    use HasFactory;

    protected $fillable = [
        'asset_key',
        'source_ref',
        'canonical_url',
        'asset_kind',
        'mime_type',
        'fallback_url',
        'width',
        'height',
        'metadata',
    ];

    protected function casts(): array
    {
        return [
            'width' => 'integer',
            'height' => 'integer',
            'metadata' => 'array',
        ];
    }
}
