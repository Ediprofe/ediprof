<?php

namespace Tests\Feature;

use App\Models\AssessmentContext;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentTemplate;
use App\Models\Course;
use App\Models\CourseContent;
use App\Models\CourseEnrollment;
use App\Models\User;
use App\Models\Workshop;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Hash;
use Tests\TestCase;

class AssessmentAttemptApiTest extends TestCase
{
    use RefreshDatabase;

    public function test_student_can_start_and_answer_a_study_attempt(): void
    {
        [$student, $workshop, $template] = $this->makeAssignedTemplate('taller');
        $question = $template->questions()->orderBy('order_base')->firstOrFail();
        $token = $this->loginAndGetToken($student->email, 'Secret1234');

        $startResponse = $this->postJson(
            '/api/v1/workshops/'.$workshop->external_id.'/attempts',
            ['mode' => 'study'],
            ['Authorization' => "Bearer {$token}"],
        );

        $startResponse
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.id', $template->external_id)
            ->assertJsonPath('data.attempt.mode', 'study')
            ->assertJsonPath('data.questions.0.id', 'q-1')
            ->assertJsonPath('data.questions.0.correct_option_id', null);

        $attemptId = (string) $startResponse->json('data.attempt.id');

        $answerResponse = $this->patchJson(
            '/api/v1/assessment-attempts/'.$attemptId.'/questions/'.$question->external_id,
            ['option_id' => 'B'],
            ['Authorization' => "Bearer {$token}"],
        );

        $answerResponse
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.question_id', 'q-1')
            ->assertJsonPath('data.selected_option_id', 'B')
            ->assertJsonPath('data.correct_option_id', 'B')
            ->assertJsonPath('data.is_correct', true);

        $showResponse = $this->getJson(
            '/api/v1/assessment-attempts/'.$attemptId,
            ['Authorization' => "Bearer {$token}"],
        );

        $showResponse
            ->assertOk()
            ->assertJsonPath('data.selected_by_question.q-1', 'B')
            ->assertJsonPath('data.evaluation_by_question.q-1.is_correct', true);
    }

    public function test_student_can_submit_a_simulacro_attempt_and_keep_stable_order(): void
    {
        [$student, $workshop, $template] = $this->makeAssignedTemplate('simulacro');
        $token = $this->loginAndGetToken($student->email, 'Secret1234');

        $startResponse = $this->postJson(
            '/api/v1/simulacros/'.$workshop->external_id.'/attempts',
            ['mode' => 'simulacro'],
            ['Authorization' => "Bearer {$token}"],
        );

        $startResponse
            ->assertOk()
            ->assertJsonPath('data.attempt.mode', 'simulacro');

        $attemptId = (string) $startResponse->json('data.attempt.id');
        $questionIds = array_values(array_map(
            static fn (array $question): string => (string) ($question['id'] ?? ''),
            $startResponse->json('data.questions', []),
        ));

        $this->assertSame(['q-1', 'q-2'], $questionIds);

        $this->patchJson(
            '/api/v1/assessment-attempts/'.$attemptId.'/questions/q-1',
            ['option_id' => 'A'],
            ['Authorization' => "Bearer {$token}"],
        )->assertOk()
            ->assertJsonPath('data.correct_option_id', null);

        $this->patchJson(
            '/api/v1/assessment-attempts/'.$attemptId.'/questions/q-2',
            ['option_id' => 'A'],
            ['Authorization' => "Bearer {$token}"],
        )->assertOk();

        $submitResponse = $this->postJson(
            '/api/v1/assessment-attempts/'.$attemptId.'/submit',
            [],
            ['Authorization' => "Bearer {$token}"],
        );

        $submitResponse
            ->assertOk()
            ->assertJsonPath('data.attempt.submitted', true)
            ->assertJsonPath('data.attempt.score_raw', 1)
            ->assertJsonPath('data.attempt.score_percent', 50)
            ->assertJsonPath('data.evaluation_by_question.q-1.is_correct', false)
            ->assertJsonPath('data.evaluation_by_question.q-2.is_correct', true);

        $showResponse = $this->getJson(
            '/api/v1/assessment-attempts/'.$attemptId,
            ['Authorization' => "Bearer {$token}"],
        );

        $showResponse
            ->assertOk()
            ->assertJsonPath('data.questions.0.id', 'q-1')
            ->assertJsonPath('data.questions.1.id', 'q-2')
            ->assertJsonPath('data.evaluation_by_question.q-2.correct_option_id', 'A');
    }

    /**
     * @return array{0:User,1:Workshop,2:AssessmentTemplate}
     */
    private function makeAssignedTemplate(string $contentType = 'taller'): array
    {
        $student = User::factory()->create([
            'name' => 'ESTUDIANTE DE PRUEBA',
            'email' => 'estudiante@sanjoseitagui.edu.co',
            'password' => Hash::make('Secret1234'),
            'role' => 'student',
            'member_status' => 'approved',
            'auth_provider' => 'google',
        ]);

        $course = Course::query()->create([
            'name' => 'ICFES 11°1',
            'slug' => 'icfes-11-1',
            'school_year' => '2026',
            'is_active' => true,
        ]);

        CourseEnrollment::query()->create([
            'course_id' => $course->id,
            'user_id' => $student->id,
            'status' => 'active',
            'source' => 'seed',
        ]);

        $workshop = Workshop::query()->create([
            'external_id' => 'content:'.$contentType.':quimica/demo/taller',
            'content_external_id' => 'content:'.$contentType.':quimica/demo/taller',
            'content_type' => $contentType === 'simulacro' ? 'simulacro' : 'taller',
            'title' => $contentType === 'simulacro' ? 'Simulacro demo' : 'Taller demo',
            'route' => '/'.$contentType.'/quimica/demo/taller',
            'area_slug' => 'quimica',
            'unidad_slug' => 'demo',
            'access_tier' => 'premium',
            'is_published' => true,
            'total_questions' => 2,
            'total_assets' => 0,
            'assets' => [],
            'questions' => [],
            'metadata' => [],
            'synced_at' => now(),
        ]);

        CourseContent::query()->create([
            'course_id' => $course->id,
            'workshop_id' => $workshop->id,
            'is_active' => true,
        ]);

        $template = AssessmentTemplate::query()->create([
            'external_id' => $workshop->external_id,
            'source_workshop_id' => $workshop->id,
            'title' => $workshop->title,
            'source_content_type' => $workshop->content_type,
            'default_mode' => $contentType === 'simulacro' ? 'simulacro' : 'study',
            'route' => $workshop->route,
            'area_slug' => $workshop->area_slug,
            'unidad_slug' => $workshop->unidad_slug,
            'access_tier' => 'premium',
            'is_published' => true,
            'total_questions' => 2,
            'total_assets' => 0,
            'assets' => [],
            'asset_refs' => [],
            'metadata' => [],
            'synced_at' => now(),
        ]);

        $context = AssessmentContext::query()->create([
            'template_id' => $template->id,
            'external_id' => 'ctx-1',
            'title' => 'Contexto compartido',
            'order_base' => 1,
            'is_active' => true,
            'context_mdx' => 'Contexto de la pregunta',
            'context_html' => '<p>Contexto de la pregunta</p>',
            'context_assets' => [],
            'context_blocks' => [],
            'metadata' => [],
        ]);

        $questionOne = AssessmentQuestion::query()->create([
            'template_id' => $template->id,
            'external_id' => 'q-1',
            'order_base' => 1,
            'source_slug' => $workshop->route.'#pregunta-q-1',
            'is_active' => true,
            'meta' => [],
            'stem_mdx' => 'Primera pregunta',
            'stem_html' => '<p>Primera pregunta</p>',
            'stem_assets' => [],
            'stem_blocks' => [],
            'options' => [
                ['id' => 'A', 'text' => 'Incorrecta', 'is_correct' => false],
                ['id' => 'B', 'text' => 'Correcta', 'is_correct' => true],
            ],
            'correct_option_id' => 'B',
            'feedback_mdx' => 'Explicación 1',
            'feedback_html' => '<p>Explicación 1</p>',
            'feedback_summary' => 'Respuesta',
            'feedback_assets' => [],
            'feedback_blocks' => [],
            'concepts_mdx' => 'Concepto 1',
            'concepts_html' => '<p>Concepto 1</p>',
            'concepts_summary' => 'Conceptos relacionados',
            'concepts_assets' => [],
            'concepts_blocks' => [],
            'app_payload_version' => 1,
        ]);

        $questionTwo = AssessmentQuestion::query()->create([
            'template_id' => $template->id,
            'external_id' => 'q-2',
            'order_base' => 2,
            'source_slug' => $workshop->route.'#pregunta-q-2',
            'is_active' => true,
            'meta' => [],
            'stem_mdx' => 'Segunda pregunta',
            'stem_html' => '<p>Segunda pregunta</p>',
            'stem_assets' => [],
            'stem_blocks' => [],
            'options' => [
                ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
            ],
            'correct_option_id' => 'A',
            'feedback_mdx' => 'Explicación 2',
            'feedback_html' => '<p>Explicación 2</p>',
            'feedback_summary' => 'Respuesta',
            'feedback_assets' => [],
            'feedback_blocks' => [],
            'concepts_mdx' => 'Concepto 2',
            'concepts_html' => '<p>Concepto 2</p>',
            'concepts_summary' => 'Conceptos relacionados',
            'concepts_assets' => [],
            'concepts_blocks' => [],
            'app_payload_version' => 1,
        ]);

        $questionOne->contexts()->attach($context->id, ['order_base' => 1]);
        $questionTwo->contexts()->attach($context->id, ['order_base' => 1]);

        return [$student, $workshop, $template];
    }

    private function loginAndGetToken(string $email, string $password): string
    {
        $response = $this->postJson('/api/v1/auth/login', [
            'email' => $email,
            'password' => $password,
            'device_name' => 'phpunit-device',
        ]);

        $response->assertOk();

        $token = $response->json('data.token');
        $this->assertIsString($token);

        return $token;
    }
}
