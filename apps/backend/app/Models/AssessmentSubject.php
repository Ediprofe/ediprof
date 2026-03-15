<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

class AssessmentSubject extends Model
{
    use HasFactory;

    protected $fillable = [
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
        static::saving(function (self $subject): void {
            $subject->label = trim($subject->label);
            $subject->slug = Str::slug($subject->label);
        });

        static::updated(function (self $subject): void {
            if (! $subject->wasChanged('label')) {
                return;
            }

            foreach (['assessment_templates', 'assessment_questions', 'assessment_contexts', 'assessment_booklet_sections'] as $table) {
                DB::table($table)
                    ->where('subject_id', $subject->id)
                    ->update([
                        'subject_label' => $subject->label,
                        'updated_at' => now(),
                    ]);
            }
        });
    }

    public function units(): HasMany
    {
        return $this->hasMany(AssessmentUnit::class, 'subject_id');
    }

}
