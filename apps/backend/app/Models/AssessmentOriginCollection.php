<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

class AssessmentOriginCollection extends Model
{
    use HasFactory;

    protected $fillable = [
        'origin_type',
        'label',
        'slug',
        'is_active',
    ];

    protected function casts(): array
    {
        return [
            'is_active' => 'boolean',
        ];
    }

    protected static function booted(): void
    {
        static::saving(function (self $collection): void {
            $collection->label = trim($collection->label);
            $collection->slug = Str::slug($collection->label);
        });

        static::updated(function (self $collection): void {
            if (! $collection->wasChanged(['label', 'origin_type'])) {
                return;
            }

            foreach (['assessment_templates', 'assessment_questions', 'assessment_contexts'] as $table) {
                $payload = [
                    'origin_label' => $collection->label,
                    'updated_at' => now(),
                ];

                if ($table === 'assessment_templates') {
                    $payload['source_content_type'] = $collection->origin_type;
                }

                DB::table($table)
                    ->where('origin_collection_id', $collection->id)
                    ->update($payload);
            }
        });
    }

}
