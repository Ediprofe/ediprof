<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class AssessmentBookletQuestion extends Model
{
    use HasFactory;

    protected $fillable = [
        'booklet_id',
        'booklet_section_id',
        'question_id',
        'order_base',
    ];

    protected function casts(): array
    {
        return [
            'booklet_id' => 'integer',
            'booklet_section_id' => 'integer',
            'question_id' => 'integer',
            'order_base' => 'integer',
        ];
    }

    public function booklet(): BelongsTo
    {
        return $this->belongsTo(AssessmentBooklet::class, 'booklet_id');
    }

    public function bookletSection(): BelongsTo
    {
        return $this->belongsTo(AssessmentBookletSection::class, 'booklet_section_id');
    }

    public function question(): BelongsTo
    {
        return $this->belongsTo(AssessmentQuestion::class, 'question_id');
    }
}
