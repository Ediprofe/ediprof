<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Hash;
use Tests\TestCase;

class MemberAccessFlowTest extends TestCase
{
    use RefreshDatabase;

    public function test_blocked_member_cannot_login(): void
    {
        User::query()->create([
            'name' => 'Bloqueado',
            'email' => 'bloqueado@colegio.edu.co',
            'password' => Hash::make('Secret1234'),
            'role' => 'student',
            'member_status' => 'blocked',
            'auth_provider' => 'google',
        ]);

        $this->postJson('/api/v1/auth/login', [
            'email' => 'bloqueado@colegio.edu.co',
            'password' => 'Secret1234',
        ])->assertForbidden()
            ->assertJsonPath('ok', false)
            ->assertJsonPath('error.code', 'account_blocked');
    }

    public function test_legacy_student_registration_route_is_not_available(): void
    {
        $this->postJson('/api/v1/auth/register', [
            'name' => 'Estudiante Uno',
            'email' => 'estudiante1@sanjoseitagui.edu.co',
            'password' => 'Secret1234',
            'password_confirmation' => 'Secret1234',
        ])->assertNotFound();
    }

    public function test_legacy_student_access_admin_routes_are_not_available(): void
    {
        $admin = User::query()->create([
            'name' => 'Admin',
            'email' => 'admin@ediprofe.com',
            'password' => Hash::make('Admin12345!'),
            'role' => 'admin',
            'member_status' => 'approved',
            'auth_provider' => 'password',
        ]);

        $token = $this->loginAndGetToken($admin->email, 'Admin12345!');

        $this->getJson('/api/v1/admin/students', [
            'Authorization' => "Bearer {$token}",
        ])->assertNotFound();
    }

    public function test_admin_can_still_use_local_login_for_academic_panel(): void
    {
        $admin = User::query()->create([
            'name' => 'Admin',
            'email' => 'admin-local@ediprofe.com',
            'password' => Hash::make('Admin12345!'),
            'role' => 'admin',
            'member_status' => 'approved',
            'auth_provider' => 'password',
        ]);

        $token = $this->loginAndGetToken($admin->email, 'Admin12345!');

        $this->getJson('/api/v1/admin/courses', [
            'Authorization' => "Bearer {$token}",
        ])->assertOk()
            ->assertJsonPath('ok', true);
    }

    private function loginAndGetToken(string $email, string $password): string
    {
        $response = $this->postJson('/api/v1/auth/login', [
            'email' => $email,
            'password' => $password,
            'device_name' => 'phpunit',
        ])->assertOk();

        $token = $response->json('data.token');
        $this->assertIsString($token);

        return $token;
    }
}
