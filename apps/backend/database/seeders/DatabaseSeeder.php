<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

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
                'email_verified_at' => now(),
            ]
        );
    }
}
