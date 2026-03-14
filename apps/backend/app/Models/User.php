<?php

namespace App\Models;

// use Illuminate\Contracts\Auth\MustVerifyEmail;
use Filament\Models\Contracts\FilamentUser;
use Filament\Panel;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Illuminate\Support\Str;

class User extends Authenticatable implements FilamentUser
{
    /** @use HasFactory<\Database\Factories\UserFactory> */
    use HasFactory, Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var list<string>
     */
    protected $fillable = [
        'name',
        'first_names',
        'last_names',
        'email',
        'institutional_code',
        'document_number',
        'grade_group',
        'password',
        'role',
        'member_status',
        'auth_provider',
        'google_subject',
        'google_avatar_url',
        'last_login_at',
    ];

    /**
     * The attributes that should be hidden for serialization.
     *
     * @var list<string>
     */
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'email_verified_at' => 'datetime',
            'last_login_at' => 'datetime',
            'password' => 'hashed',
        ];
    }

    public function isAdmin(): bool
    {
        return $this->role === 'admin';
    }

    public static function composeDisplayName(
        ?string $lastNames,
        ?string $firstNames,
        ?string $fallback = ''
    ): string {
        $lastNames = static::normalizeAcademicNamePart($lastNames);
        $firstNames = static::normalizeAcademicNamePart($firstNames);

        if ($lastNames !== '' && $firstNames !== '') {
            return "{$lastNames}, {$firstNames}";
        }

        if ($lastNames !== '') {
            return $lastNames;
        }

        if ($firstNames !== '') {
            return $firstNames;
        }

        return static::normalizeAcademicNamePart($fallback);
    }

    public static function splitAcademicName(?string $value): array
    {
        $value = static::normalizeAcademicFullName($value);

        if ($value === '') {
            return [
                'first_names' => null,
                'last_names' => null,
                'display_name' => '',
            ];
        }

        if (str_contains($value, ',')) {
            [$lastNames, $firstNames] = array_pad(
                array_map(
                    static fn ($part): string => static::normalizeAcademicNamePart($part),
                    explode(',', $value, 2)
                ),
                2,
                '',
            );

            return [
                'first_names' => $firstNames !== '' ? $firstNames : null,
                'last_names' => $lastNames !== '' ? $lastNames : null,
                'display_name' => static::composeDisplayName($lastNames, $firstNames, $value),
            ];
        }

        return [
            'first_names' => static::normalizeAcademicNamePart($value),
            'last_names' => null,
            'display_name' => static::normalizeAcademicNamePart($value),
        ];
    }

    public function getAcademicSortNameAttribute(): string
    {
        return static::composeDisplayName($this->last_names, $this->first_names, $this->name);
    }

    public static function normalizeAcademicFullName(?string $value): string
    {
        $value = trim((string) $value);

        if ($value === '') {
            return '';
        }

        $value = preg_replace('/\s*,\s*/u', ', ', $value) ?: $value;

        return Str::of($value)
            ->squish()
            ->value();
    }

    public static function normalizeAcademicNamePart(?string $value): string
    {
        return Str::of((string) $value)
            ->squish()
            ->trim()
            ->value();
    }

    public function canAccessPanel(Panel $panel): bool
    {
        return $this->isAdmin() && $this->member_status !== 'blocked';
    }

    /**
     * @return HasMany<ApiToken, $this>
     */
    public function apiTokens(): HasMany
    {
        return $this->hasMany(ApiToken::class);
    }

    /**
     * @return HasMany<CourseEnrollment, $this>
     */
    public function courseEnrollments(): HasMany
    {
        return $this->hasMany(CourseEnrollment::class);
    }

    /**
     * @return BelongsToMany<Course, $this>
     */
    public function courses(): BelongsToMany
    {
        return $this->belongsToMany(Course::class, 'course_enrollments')
            ->withPivot(['status', 'source'])
            ->withTimestamps();
    }
}
