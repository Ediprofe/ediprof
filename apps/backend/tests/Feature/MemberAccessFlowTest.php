<?php

namespace Tests\Feature;

use App\Models\Course;
use App\Models\User;
use App\Models\Workshop;
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

    public function test_admin_can_request_filament_panel_handoff(): void
    {
        $admin = User::query()->create([
            'name' => 'Admin Handoff',
            'email' => 'admin-handoff@ediprofe.com',
            'password' => Hash::make('Admin12345!'),
            'role' => 'admin',
            'member_status' => 'approved',
            'auth_provider' => 'password',
        ]);

        $token = $this->loginAndGetToken($admin->email, 'Admin12345!');

        $response = $this->postJson('/api/v1/admin/panel-handoff', [
            'redirect_to' => '/admin/courses',
        ], [
            'Authorization' => "Bearer {$token}",
        ])->assertOk()
            ->assertJsonPath('ok', true);

        $url = $response->json('data.url');
        $this->assertIsString($url);
        $this->assertStringContainsString('/admin/handoff/', $url);

        $path = parse_url($url, PHP_URL_PATH);
        $this->assertIsString($path);

        $this->get($path)
            ->assertRedirect('/admin/courses');
    }

    public function test_student_cannot_request_filament_panel_handoff(): void
    {
        $student = User::query()->create([
            'name' => 'Student Handoff',
            'email' => 'student-handoff@sanjoseitagui.edu.co',
            'password' => Hash::make('Secret1234'),
            'role' => 'student',
            'member_status' => 'approved',
            'auth_provider' => 'google',
        ]);

        $token = $this->loginAndGetToken($student->email, 'Secret1234');

        $this->postJson('/api/v1/admin/panel-handoff', [], [
            'Authorization' => "Bearer {$token}",
        ])->assertForbidden();
    }

    public function test_admin_can_open_filament_course_screens(): void
    {
        $admin = User::query()->create([
            'name' => 'Panel Admin',
            'email' => 'panel-admin@ediprofe.com',
            'password' => Hash::make('Admin12345!'),
            'role' => 'admin',
            'member_status' => 'approved',
            'auth_provider' => 'password',
        ]);

        $course = Course::query()->create([
            'name' => 'ICFES 11°1',
            'slug' => 'icfes-11-1',
            'school_year' => '2026',
            'is_active' => true,
        ]);

        Workshop::query()->create([
            'external_id' => 'content:saber:demo',
            'content_external_id' => 'content:saber:demo',
            'content_type' => 'taller',
            'title' => 'Taller demo',
            'route' => '/talleres/demo',
            'area_slug' => 'quimica',
            'unidad_slug' => 'demo',
            'access_tier' => 'member',
            'is_published' => true,
            'total_questions' => 1,
            'total_assets' => 0,
            'assets' => [],
            'questions' => [],
            'metadata' => [],
            'synced_at' => now(),
        ]);

        $this->actingAs($admin)
            ->get('/admin/courses')
            ->assertOk();

        $this->actingAs($admin)
            ->get("/admin/courses/{$course->id}/edit")
            ->assertOk();

        $this->actingAs($admin)
            ->get('/admin/users')
            ->assertOk();
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
