<?php

namespace Tests\Feature;

use App\Models\Course;
use App\Models\CourseContent;
use App\Models\CourseEnrollment;
use App\Models\User;
use App\Models\Workshop;
use Database\Seeders\DatabaseSeeder;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Http;
use Tests\TestCase;

class AcademicMembersFlowTest extends TestCase
{
    use RefreshDatabase;

    public function test_google_login_creates_approved_student_for_institutional_domain(): void
    {
        config()->set('services.google.client_id', 'test-google-client-id');
        config()->set('services.google.allowed_domain', 'sanjoseitagui.edu.co');

        Http::fake([
            'https://oauth2.googleapis.com/tokeninfo*' => Http::response([
                'aud' => 'test-google-client-id',
                'sub' => 'google-subject-123',
                'email' => 'estudiante@sanjoseitagui.edu.co',
                'email_verified' => 'true',
                'hd' => 'sanjoseitagui.edu.co',
                'name' => 'Estudiante Institucional',
                'picture' => 'https://example.com/avatar.png',
            ]),
        ]);

        $response = $this->postJson('/api/v1/auth/google/login', [
            'credential' => str_repeat('x', 40),
            'device_name' => 'phpunit-google',
        ]);

        $response
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.user.email', 'estudiante@sanjoseitagui.edu.co')
            ->assertJsonPath('data.user.member_status', 'approved')
            ->assertJsonPath('data.user.auth_provider', 'google');

        $this->assertDatabaseHas('users', [
            'email' => 'estudiante@sanjoseitagui.edu.co',
            'role' => 'student',
            'member_status' => 'approved',
            'auth_provider' => 'google',
            'google_subject' => 'google-subject-123',
        ]);
    }

    public function test_google_login_rejects_non_institutional_domain(): void
    {
        config()->set('services.google.client_id', 'test-google-client-id');
        config()->set('services.google.allowed_domain', 'sanjoseitagui.edu.co');

        Http::fake([
            'https://oauth2.googleapis.com/tokeninfo*' => Http::response([
                'aud' => 'test-google-client-id',
                'sub' => 'google-subject-789',
                'email' => 'externo@gmail.com',
                'email_verified' => 'true',
                'name' => 'Usuario Externo',
            ]),
        ]);

        $this->postJson('/api/v1/auth/google/login', [
            'credential' => str_repeat('y', 40),
            'device_name' => 'phpunit-google',
        ])->assertForbidden()
            ->assertJsonPath('ok', false)
            ->assertJsonPath('error.code', 'invalid_google_domain');
    }

    public function test_database_seeder_creates_default_courses(): void
    {
        $this->seed(DatabaseSeeder::class);

        foreach ([
            'ICFES 11°1',
            'ICFES 11°2',
            'ICFES 11°3',
            'Ciencias 8°2',
            'Ciencias 8°3',
        ] as $courseName) {
            $this->assertDatabaseHas('courses', [
                'name' => $courseName,
                'is_active' => 1,
            ]);
        }
    }

    public function test_admin_can_import_students_to_a_course_from_csv(): void
    {
        $admin = $this->makeAdmin();
        $token = $this->loginAndGetToken($admin->email, 'Admin12345!');

        $course = Course::query()->create([
            'name' => 'ICFES 11°1',
            'slug' => 'icfes-11-1',
            'school_year' => '2026',
            'is_active' => true,
        ]);

        $file = UploadedFile::fake()->createWithContent(
            'grupo.csv',
            "email,name\nana@sanjoseitagui.edu.co,Ana Perez\nexterna@gmail.com,Externa\n"
        );

        $this->post('/api/v1/admin/courses/'.$course->id.'/enrollments/import', [
            'csv' => $file,
        ], [
            'Authorization' => "Bearer {$token}",
        ])->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.summary.created_users', 1)
            ->assertJsonPath('data.summary.enrolled_users', 1)
            ->assertJsonPath('data.summary.error_count', 1);

        $this->assertDatabaseHas('users', [
            'email' => 'ana@sanjoseitagui.edu.co',
            'member_status' => 'approved',
            'auth_provider' => 'google',
        ]);

        $student = User::query()->where('email', 'ana@sanjoseitagui.edu.co')->firstOrFail();
        $this->assertDatabaseHas('course_enrollments', [
            'course_id' => $course->id,
            'user_id' => $student->id,
            'status' => 'active',
            'source' => 'csv_import',
        ]);
    }

    public function test_student_library_is_filtered_by_course_contents(): void
    {
        $course = Course::query()->create([
            'name' => 'ICFES 11°2',
            'slug' => 'icfes-11-2',
            'school_year' => '2026',
            'is_active' => true,
        ]);

        $student = User::query()->create([
            'name' => 'María',
            'email' => 'maria@sanjoseitagui.edu.co',
            'password' => Hash::make('Secret1234'),
            'role' => 'student',
            'member_status' => 'approved',
            'auth_provider' => 'google',
        ]);

        CourseEnrollment::query()->create([
            'course_id' => $course->id,
            'user_id' => $student->id,
            'status' => 'active',
            'source' => 'manual',
        ]);

        $allowedWorkshop = $this->createPremiumWorkshop(
            'content:saber:quimica/enlace-1',
            'taller',
            '/saber/quimica/enlace-1',
            'Taller permitido'
        );

        $blockedWorkshop = $this->createPremiumWorkshop(
            'content:simulacros:quimica/enlace-2',
            'simulacro',
            '/simulacros/quimica/enlace-2',
            'Simulacro no asignado'
        );

        CourseContent::query()->create([
            'course_id' => $course->id,
            'workshop_id' => $allowedWorkshop->id,
            'is_active' => true,
        ]);

        $token = $this->loginAndGetToken($student->email, 'Secret1234');

        $this->getJson('/api/v1/me/courses', [
            'Authorization' => "Bearer {$token}",
        ])->assertOk()
            ->assertJsonPath('data.0.name', 'ICFES 11°2');

        $this->getJson('/api/v1/me/library?content_type=taller', [
            'Authorization' => "Bearer {$token}",
        ])->assertOk()
            ->assertJsonCount(1, 'data')
            ->assertJsonPath('data.0.id', $allowedWorkshop->external_id);

        $this->getJson(
            '/api/v1/workshops/'.rawurlencode($allowedWorkshop->external_id).'?published_only=false&include_answers=false&format=app',
            ['Authorization' => "Bearer {$token}"],
        )->assertOk()
            ->assertJsonPath('ok', true);

        $this->getJson(
            '/api/v1/simulacros/'.rawurlencode($blockedWorkshop->external_id).'?published_only=false&include_answers=false&format=app',
            ['Authorization' => "Bearer {$token}"],
        )->assertForbidden()
            ->assertJsonPath('error.code', 'premium_access_required');
    }

    private function makeAdmin(): User
    {
        return User::query()->create([
            'name' => 'Admin',
            'email' => 'admin@sanjoseitagui.edu.co',
            'password' => Hash::make('Admin12345!'),
            'role' => 'admin',
            'member_status' => 'approved',
            'auth_provider' => 'password',
        ]);
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

    private function createPremiumWorkshop(
        string $externalId,
        string $contentType,
        string $route,
        string $title
    ): Workshop {
        return Workshop::query()->create([
            'external_id' => $externalId,
            'content_external_id' => $externalId,
            'content_type' => $contentType,
            'route' => $route,
            'title' => $title,
            'area_slug' => 'quimica',
            'unidad_slug' => 'unidad-prueba',
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
                    'stem_blocks' => [],
                    'options' => [
                        ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                        ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
                    ],
                    'correct_option_id' => 'A',
                ],
            ],
            'metadata' => [],
        ]);
    }
}
