<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Support\Str;

class Course extends Model
{
    use HasFactory;

    /**
     * @var list<string>
     */
    protected $fillable = [
        'name',
        'slug',
        'school_year',
        'is_active',
        'notes',
    ];

    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'is_active' => 'boolean',
        ];
    }

    /**
     * @return HasMany<CourseEnrollment, $this>
     */
    public function enrollments(): HasMany
    {
        return $this->hasMany(CourseEnrollment::class);
    }

    /**
     * @return HasMany<CourseContent, $this>
     */
    public function contents(): HasMany
    {
        return $this->hasMany(CourseContent::class);
    }

    /**
     * @return BelongsToMany<User, $this>
     */
    public function students(): BelongsToMany
    {
        return $this->belongsToMany(User::class, 'course_enrollments')
            ->withPivot(['status', 'source'])
            ->withTimestamps();
    }

    public static function resolveUniqueSlug(string $baseSlug, ?int $ignoreId = null): string
    {
        $slug = Str::slug($baseSlug);

        if ($slug === '') {
            $slug = 'curso';
        }

        $candidate = $slug;
        $suffix = 2;

        while (static::slugExists($candidate, $ignoreId)) {
            $candidate = "{$slug}-{$suffix}";
            $suffix += 1;
        }

        return $candidate;
    }

    protected static function slugExists(string $slug, ?int $ignoreId = null): bool
    {
        return static::query()
            ->when($ignoreId !== null, fn ($builder) => $builder->where('id', '!=', $ignoreId))
            ->where('slug', $slug)
            ->exists();
    }
}
