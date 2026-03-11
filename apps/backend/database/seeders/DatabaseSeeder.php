<?php

namespace Database\Seeders;

use App\Models\Course;
use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;

class DatabaseSeeder extends Seeder
{
    use WithoutModelEvents;

    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        $adminEmail = mb_strtolower(trim((string) env('SEED_ADMIN_EMAIL', 'admin@ediprofe.com')));
        $adminPassword = (string) env('SEED_ADMIN_PASSWORD', 'Admin12345!');

        User::query()->updateOrCreate(
            ['email' => $adminEmail],
            [
                'name' => 'Admin Ediprofe',
                'password' => Hash::make($adminPassword),
                'role' => 'admin',
                'member_status' => 'approved',
                'email_verified_at' => now(),
            ]
        );

        User::query()->updateOrCreate(
            ['email' => 'test@example.com'],
            [
                'name' => 'Test User',
                'password' => Hash::make('password'),
                'role' => 'student',
                'member_status' => 'approved',
                'auth_provider' => 'password',
                'email_verified_at' => now(),
            ]
        );

        collect([
            'ICFES 11°1',
            'ICFES 11°2',
            'ICFES 11°3',
            'Ciencias 8°2',
            'Ciencias 8°3',
        ])->each(function (string $name): void {
            Course::query()->updateOrCreate(
                ['slug' => Str::slug($name)],
                [
                    'name' => $name,
                    'school_year' => '2026',
                    'is_active' => true,
                    'notes' => 'Curso base sembrado por Ediprofe.',
                ]
            );
        });
    }
}
