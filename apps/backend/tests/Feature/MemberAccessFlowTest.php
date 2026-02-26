<?php

namespace Tests\Feature;

use App\Models\User;
use App\Models\Workshop;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Hash;
use Tests\TestCase;

class MemberAccessFlowTest extends TestCase
{
    use RefreshDatabase;

    public function test_register_creates_pending_student_account(): void
    {
        $response = $this->postJson('/api/v1/auth/register', [
            'name' => 'Estudiante Uno',
            'email' => 'estudiante1@colegio.edu.co',
            'password' => 'Secret1234',
            'password_confirmation' => 'Secret1234',
        ]);

        $response
            ->assertCreated()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.user.role', 'student')
            ->assertJsonPath('data.user.member_status', 'pending');

        $this->assertDatabaseHas('users', [
            'email' => 'estudiante1@colegio.edu.co',
            'role' => 'student',
            'member_status' => 'pending',
        ]);
    }

    public function test_blocked_member_cannot_login(): void
    {
        User::query()->create([
            'name' => 'Bloqueado',
            'email' => 'bloqueado@colegio.edu.co',
            'password' => Hash::make('Secret1234'),
            'role' => 'student',
            'member_status' => 'blocked',
        ]);

        $response = $this->postJson('/api/v1/auth/login', [
            'email' => 'bloqueado@colegio.edu.co',
            'password' => 'Secret1234',
        ]);

        $response
            ->assertForbidden()
            ->assertJsonPath('ok', false)
            ->assertJsonPath('error.code', 'account_blocked');
    }

    public function test_admin_can_approve_student_and_unlock_premium_workshop_access(): void
    {
        $this->createPremiumWorkshop();

        $student = User::query()->create([
            'name' => 'Pendiente',
            'email' => 'pendiente@colegio.edu.co',
            'password' => Hash::make('Secret1234'),
            'role' => 'student',
            'member_status' => 'pending',
        ]);

        $admin = User::query()->create([
            'name' => 'Admin',
            'email' => 'admin@ediprofe.com',
            'password' => Hash::make('Admin12345!'),
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        $studentToken = $this->loginAndGetToken('pendiente@colegio.edu.co', 'Secret1234');
        $adminToken = $this->loginAndGetToken('admin@ediprofe.com', 'Admin12345!');

        $this->getJson(
            '/api/v1/workshops/content:saber:quimica/la-materia/taller?published_only=false&include_answers=false&format=app',
            ['Authorization' => "Bearer {$studentToken}"],
        )->assertStatus(403)
            ->assertJsonPath('error.code', 'premium_access_required');

        $this->postJson("/api/v1/admin/students/{$student->id}/approve", [], [
            'Authorization' => "Bearer {$adminToken}",
        ])->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.member_status', 'approved')
            ->assertJsonPath('data.has_school_premium_grant', true);

        $this->assertDatabaseHas('access_grants', [
            'user_id' => $student->id,
            'scope' => 'global',
            'scope_ref' => '*',
            'reason' => 'school_whitelist',
            'is_active' => 1,
        ]);

        $this->getJson(
            '/api/v1/workshops/content:saber:quimica/la-materia/taller?published_only=false&include_answers=false&format=app',
            ['Authorization' => "Bearer {$studentToken}"],
        )->assertOk()
            ->assertJsonPath('ok', true);

        $this->postJson(
            '/api/v1/workshops/content:saber:quimica/la-materia/taller/questions/1/evaluate?published_only=false&format=app',
            ['option_id' => 'A'],
            ['Authorization' => "Bearer {$studentToken}"],
        )->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.is_correct', true);
    }

    public function test_admin_can_list_pending_students(): void
    {
        User::query()->create([
            'name' => 'Estudiante Pendiente',
            'email' => 'pendiente-listado@colegio.edu.co',
            'password' => Hash::make('Secret1234'),
            'role' => 'student',
            'member_status' => 'pending',
        ]);

        User::query()->create([
            'name' => 'Admin',
            'email' => 'admin-listado@ediprofe.com',
            'password' => Hash::make('Admin12345!'),
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        $adminToken = $this->loginAndGetToken('admin-listado@ediprofe.com', 'Admin12345!');

        $this->getJson('/api/v1/admin/students?status=pending', [
            'Authorization' => "Bearer {$adminToken}",
        ])->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.0.member_status', 'pending');
    }

    public function test_admin_can_revoke_premium_access_immediately(): void
    {
        $this->createPremiumWorkshop();

        $student = User::query()->create([
            'name' => 'Aprobado',
            'email' => 'aprobado@colegio.edu.co',
            'password' => Hash::make('Secret1234'),
            'role' => 'student',
            'member_status' => 'approved',
        ]);

        $admin = User::query()->create([
            'name' => 'Admin',
            'email' => 'admin-revoke@ediprofe.com',
            'password' => Hash::make('Admin12345!'),
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        $student->accessGrants()->create([
            'scope' => 'global',
            'scope_ref' => '*',
            'reason' => 'school_whitelist',
            'starts_at' => now(),
            'ends_at' => null,
            'is_active' => true,
            'metadata' => [],
        ]);

        $studentToken = $this->loginAndGetToken('aprobado@colegio.edu.co', 'Secret1234');
        $adminToken = $this->loginAndGetToken('admin-revoke@ediprofe.com', 'Admin12345!');

        $this->getJson(
            '/api/v1/workshops/content:saber:quimica/la-materia/taller?published_only=false&include_answers=false&format=app',
            ['Authorization' => "Bearer {$studentToken}"],
        )->assertOk();

        $this->postJson("/api/v1/admin/students/{$student->id}/revoke-premium", [], [
            'Authorization' => "Bearer {$adminToken}",
        ])->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.has_school_premium_grant', false);

        $this->getJson(
            '/api/v1/workshops/content:saber:quimica/la-materia/taller?published_only=false&include_answers=false&format=app',
            ['Authorization' => "Bearer {$studentToken}"],
        )->assertStatus(403)
            ->assertJsonPath('error.code', 'premium_access_required');
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

    private function createPremiumWorkshop(): void
    {
        Workshop::query()->create([
            'external_id' => 'content:saber:quimica/la-materia/taller',
            'content_external_id' => 'content:saber:quimica/la-materia/taller',
            'route' => '/saber/quimica/la-materia/taller',
            'title' => 'Taller: La Materia',
            'area_slug' => 'quimica',
            'unidad_slug' => 'la-materia',
            'access_tier' => 'premium',
            'is_published' => true,
            'total_questions' => 1,
            'total_assets' => 0,
            'assets' => [],
            'questions' => [
                [
                    'id' => '1',
                    'order' => 1,
                    'stem_mdx' => 'Pregunta de prueba',
                    'stem_assets' => [],
                    'stem_blocks' => [
                        [
                            'type' => 'paragraph',
                            'inlines' => [
                                ['text' => 'Pregunta de prueba', 'variant' => 'plain'],
                            ],
                        ],
                    ],
                    'options' => [
                        ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                        ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Correcto',
                    'feedback_assets' => [],
                    'feedback_blocks' => [
                        [
                            'type' => 'paragraph',
                            'inlines' => [
                                ['text' => 'Correcto', 'variant' => 'plain'],
                            ],
                        ],
                    ],
                    'app_payload_version' => 1,
                ],
            ],
            'metadata' => [],
            'synced_at' => now(),
        ]);
    }
}
