<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

class AssessmentUnit extends Model
{
    use HasFactory;

    protected $fillable = [
        'subject_id',
        'label',
        'slug',
        'is_active',
    ];

    protected function casts(): array
    {
        return [
            'subject_id' => 'integer',
            'is_active' => 'boolean',
        ];
    }

    protected static function booted(): void
    {
        static::saving(function (self $unit): void {
            $unit->label = trim($unit->label);
            $unit->slug = Str::slug($unit->label);
        });

        static::updated(function (self $unit): void {
            if ($unit->wasChanged('label')) {
                foreach (['assessment_templates', 'assessment_questions', 'assessment_contexts'] as $table) {
                    DB::table($table)
                        ->where('unit_id', $unit->id)
                        ->update([
                            'unit_label' => $unit->label,
                            'updated_at' => now(),
                        ]);
                }

                DB::table('assessment_booklet_sections')
                    ->where('default_unit_id', $unit->id)
                    ->update([
                        'default_unit_label' => $unit->label,
                        'updated_at' => now(),
                    ]);
            }

            if ($unit->wasChanged('subject_id')) {
                $subject = $unit->subject;
                foreach (['assessment_templates', 'assessment_questions', 'assessment_contexts'] as $table) {
                    DB::table($table)
                        ->where('unit_id', $unit->id)
                        ->update([
                            'subject_id' => $subject?->id,
                            'subject_label' => $subject?->label,
                            'updated_at' => now(),
                        ]);
                }

                DB::table('assessment_booklet_sections')
                    ->where('default_unit_id', $unit->id)
                    ->update([
                        'subject_id' => $subject?->id,
                        'subject_label' => $subject?->label,
                        'updated_at' => now(),
                    ]);
            }
        });
    }

    public function subject(): BelongsTo
    {
        return $this->belongsTo(AssessmentSubject::class, 'subject_id');
    }
}
