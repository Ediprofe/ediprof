<?php

namespace Tests\Feature;

use App\Models\AssessmentAssignment;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentTemplate;
use App\Models\Course;
use App\Models\CourseEnrollment;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Inertia\Testing\AssertableInertia as Assert;
use Tests\TestCase;

class MembersV2WebFlowTest extends TestCase
{
    use RefreshDatabase;

    public function test_guest_is_redirected_to_members_login(): void
    {
        $this->get('/miembros-v2')
            ->assertRedirect(route('members.login'));

        $this->get(route('members.login'))
            ->assertOk()
            ->assertSee('Acceso a miembros');
    }

    public function test_enrolled_student_can_see_real_evaluations_in_members_v2(): void
    {
        $student = User::factory()->create([
            'email' => 'estudiante@sanjoseitagui.edu.co',
            'role' => 'student',
            'member_status' => 'approved',
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
            'source' => 'phpunit',
        ]);

        $template = AssessmentTemplate::query()->create([
            'external_id' => 'tpl-members-v2',
            'source_content_type' => 'simulacro',
            'source_slug' => 'quimica/11-2026-s1/taller',
            'route' => '/simulacros/quimica/2026-s1/taller',
            'title' => 'Simulacro 11 · Ciencias Naturales · S1',
            'total_questions' => 19,
            'questions_payload' => [],
        ]);

        AssessmentAssignment::query()->create([
            'external_id' => 'asg-members-v2',
            'course_id' => $course->id,
            'template_id' => $template->id,
            'title' => 'Evaluación diagnóstica web',
            'mode' => AssessmentAssignment::MODE_EVALUATION,
            'status' => AssessmentAssignment::STATUS_ACTIVE,
        ]);

        $this->actingAs($student, 'web');

        $this->get('/miembros-v2/evaluaciones')
            ->assertOk()
            ->assertInertia(fn (Assert $page) => $page
                ->component('Members/Evaluations/Index', false)
                ->where('items.0.title', 'Evaluación diagnóstica web')
                ->where('items.0.course.name', 'ICFES 11°1')
            );

        $this->get('/miembros-v2/evaluaciones/asg-members-v2')
            ->assertOk()
            ->assertInertia(fn (Assert $page) => $page
                ->component('Members/Evaluations/Show', false)
                ->where('evaluation.title', 'Evaluación diagnóstica web')
                ->where('evaluation.template.title', 'Simulacro 11 · Ciencias Naturales · S1')
            );
    }

    public function test_enrolled_student_can_see_real_workshops_and_simulacros_in_members_v2(): void
    {
        $student = User::factory()->create([
            'email' => 'estudiante-workshop-sim@sanjoseitagui.edu.co',
            'role' => 'student',
            'member_status' => 'approved',
        ]);

        $course = Course::query()->create([
            'name' => 'ICFES 11°4',
            'slug' => 'icfes-11-4',
            'school_year' => '2026',
            'is_active' => true,
        ]);

        CourseEnrollment::query()->create([
            'course_id' => $course->id,
            'user_id' => $student->id,
            'status' => 'active',
            'source' => 'phpunit',
        ]);

        $workshopTemplate = AssessmentTemplate::query()->create([
            'external_id' => 'tpl-members-v2-workshop',
            'source_content_type' => 'taller',
            'source_slug' => 'quimica/11-2026-s1/taller',
            'route' => '/simulacros/quimica/2026-s1/taller',
            'title' => 'Taller Members v2',
            'total_questions' => 4,
            'questions_payload' => [],
        ]);

        $simulacroTemplate = AssessmentTemplate::query()->create([
            'external_id' => 'tpl-members-v2-simulacro',
            'source_content_type' => 'simulacro',
            'source_slug' => 'quimica/11-2026-s1/simulacro',
            'route' => '/simulacros/quimica/2026-s1',
            'title' => 'Simulacro Members v2',
            'total_questions' => 10,
            'questions_payload' => [],
        ]);

        AssessmentAssignment::query()->create([
            'external_id' => 'asg-members-v2-workshop',
            'course_id' => $course->id,
            'template_id' => $workshopTemplate->id,
            'title' => 'Taller real web',
            'mode' => AssessmentAssignment::MODE_STUDY,
            'status' => AssessmentAssignment::STATUS_ACTIVE,
        ]);

        AssessmentAssignment::query()->create([
            'external_id' => 'asg-members-v2-simulacro',
            'course_id' => $course->id,
            'template_id' => $simulacroTemplate->id,
            'title' => 'Simulacro real web',
            'mode' => AssessmentAssignment::MODE_SIMULACRO,
            'status' => AssessmentAssignment::STATUS_ACTIVE,
        ]);

        $this->actingAs($student, 'web');

        $this->get('/miembros-v2/talleres')
            ->assertOk()
            ->assertInertia(fn (Assert $page) => $page
                ->component('Members/Workshops/Index', false)
                ->where('items.0.title', 'Taller real web')
            );

        $this->get('/miembros-v2/talleres/asg-members-v2-workshop')
            ->assertOk()
            ->assertInertia(fn (Assert $page) => $page
                ->component('Members/Workshops/Show', false)
                ->where('workshop.title', 'Taller real web')
                ->where('workshop.mode', 'study')
            );

        $this->get('/miembros-v2/simulacros')
            ->assertOk()
            ->assertInertia(fn (Assert $page) => $page
                ->component('Members/Simulacros/Index', false)
                ->where('items.0.title', 'Simulacro real web')
            );

        $this->get('/miembros-v2/simulacros/asg-members-v2-simulacro')
            ->assertOk()
            ->assertInertia(fn (Assert $page) => $page
                ->component('Members/Simulacros/Show', false)
                ->where('simulacro.title', 'Simulacro real web')
                ->where('simulacro.mode', 'simulacro')
            );
    }

    public function test_enrolled_student_can_start_assignment_attempt_through_members_v2_web_route(): void
    {
        $student = User::factory()->create([
            'email' => 'estudiante2@sanjoseitagui.edu.co',
            'role' => 'student',
            'member_status' => 'approved',
        ]);

        $course = Course::query()->create([
            'name' => 'ICFES 11°2',
            'slug' => 'icfes-11-2',
            'school_year' => '2026',
            'is_active' => true,
        ]);

        CourseEnrollment::query()->create([
            'course_id' => $course->id,
            'user_id' => $student->id,
            'status' => 'active',
            'source' => 'phpunit',
        ]);

        $template = AssessmentTemplate::query()->create([
            'external_id' => 'tpl-members-v2-web',
            'source_content_type' => 'simulacro',
            'source_slug' => 'quimica/11-2026-s1/taller',
            'route' => '/simulacros/quimica/2026-s1/taller',
            'title' => 'Simulacro Members v2 Web',
            'total_questions' => 1,
            'questions_payload' => [],
        ]);

        AssessmentQuestion::query()->create([
            'template_id' => $template->id,
            'external_id' => 'q-web-1',
            'order_base' => 1,
            'source_slug' => 'quimica/11-2026-s1/taller#q-web-1',
            'is_active' => true,
            'meta' => [],
            'stem_mdx' => 'Pregunta web',
            'stem_html' => '<p>Pregunta web</p>',
            'stem_assets' => [],
            'stem_blocks' => [],
            'options' => [
                ['id' => 'A', 'text' => 'Correcta', 'text_html' => '<span><strong>Correcta</strong></span>', 'text_assets' => [], 'is_correct' => true],
                ['id' => 'B', 'text' => 'Incorrecta', 'text_html' => '<span>Incorrecta</span>', 'text_assets' => [], 'is_correct' => false],
            ],
            'correct_option_id' => 'A',
            'feedback_mdx' => 'Explicación',
            'feedback_html' => '<p>Explicación</p>',
            'feedback_summary' => 'Retro',
            'feedback_assets' => [],
            'feedback_blocks' => [],
            'concepts_mdx' => 'Concepto',
            'concepts_html' => '<p>Concepto</p>',
            'concepts_summary' => 'Conceptos',
            'concepts_assets' => [],
            'concepts_blocks' => [],
            'app_payload_version' => 1,
        ]);

        $assignment = AssessmentAssignment::query()->create([
            'external_id' => 'asg-members-v2-web',
            'course_id' => $course->id,
            'template_id' => $template->id,
            'title' => 'Evaluación web con intento',
            'mode' => AssessmentAssignment::MODE_EVALUATION,
            'status' => AssessmentAssignment::STATUS_ACTIVE,
            'opens_at' => now()->subMinute(),
            'closes_at' => now()->addHour(),
        ]);

        $this->actingAs($student, 'web');

        $this->postJson("/miembros-v2/evaluaciones/{$assignment->external_id}/intento", [])
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.render_contract.strategy', 'html_first')
            ->assertJsonPath('data.attempt.mode', 'evaluation')
            ->assertJsonPath('data.questions.0.id', 'q-web-1')
            ->assertJsonPath('data.questions.0.options.0.text_html', '<span><strong>Correcta</strong></span>');
    }

    public function test_enrolled_student_can_answer_and_submit_attempt_through_members_v2_web_routes(): void
    {
        $student = User::factory()->create([
            'email' => 'estudiante3@sanjoseitagui.edu.co',
            'role' => 'student',
            'member_status' => 'approved',
        ]);

        $course = Course::query()->create([
            'name' => 'ICFES 11°3',
            'slug' => 'icfes-11-3',
            'school_year' => '2026',
            'is_active' => true,
        ]);

        CourseEnrollment::query()->create([
            'course_id' => $course->id,
            'user_id' => $student->id,
            'status' => 'active',
            'source' => 'phpunit',
        ]);

        $template = AssessmentTemplate::query()->create([
            'external_id' => 'tpl-members-v2-submit',
            'source_content_type' => 'simulacro',
            'source_slug' => 'quimica/11-2026-s1/taller',
            'route' => '/simulacros/quimica/2026-s1/taller',
            'title' => 'Simulacro Members v2 Submit',
            'total_questions' => 1,
            'questions_payload' => [],
        ]);

        AssessmentQuestion::query()->create([
            'template_id' => $template->id,
            'external_id' => 'q-web-submit',
            'order_base' => 1,
            'source_slug' => 'quimica/11-2026-s1/taller#q-web-submit',
            'is_active' => true,
            'meta' => [],
            'stem_mdx' => 'Pregunta envío',
            'stem_html' => '<p>Pregunta envío</p>',
            'stem_assets' => [],
            'stem_blocks' => [],
            'options' => [
                ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
            ],
            'correct_option_id' => 'A',
            'feedback_mdx' => 'Explicación submit',
            'feedback_html' => '<p>Explicación submit</p>',
            'feedback_summary' => 'Retro submit',
            'feedback_assets' => [],
            'feedback_blocks' => [],
            'concepts_mdx' => 'Concepto submit',
            'concepts_html' => '<p>Concepto submit</p>',
            'concepts_summary' => 'Conceptos submit',
            'concepts_assets' => [],
            'concepts_blocks' => [],
            'app_payload_version' => 1,
        ]);

        $assignment = AssessmentAssignment::query()->create([
            'external_id' => 'asg-members-v2-submit',
            'course_id' => $course->id,
            'template_id' => $template->id,
            'title' => 'Evaluación web submit',
            'mode' => AssessmentAssignment::MODE_EVALUATION,
            'status' => AssessmentAssignment::STATUS_ACTIVE,
            'show_feedback_on_submit' => true,
            'opens_at' => now()->subMinute(),
            'closes_at' => now()->addHour(),
        ]);

        $this->actingAs($student, 'web');

        $startResponse = $this->postJson("/miembros-v2/evaluaciones/{$assignment->external_id}/intento", [])
            ->assertOk()
            ->assertJsonPath('data.questions.0.id', 'q-web-submit');

        $attemptId = (string) $startResponse->json('data.attempt.id');

        $this->patchJson("/miembros-v2/intentos/{$attemptId}/preguntas/q-web-submit", [
            'option_id' => 'A',
        ])->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.question_id', 'q-web-submit')
            ->assertJsonPath('data.selected_option_id', 'A');

        $this->postJson("/miembros-v2/intentos/{$attemptId}/entregar", [])
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.attempt.submitted', true)
            ->assertJsonPath('data.attempt.can_review', true)
            ->assertJsonPath('data.attempt.score_scale', 5);
    }

    public function test_enrolled_student_can_start_and_answer_a_workshop_attempt_through_members_v2_generic_route(): void
    {
        [$student, $assignment, $questionExternalId] = $this->makeMembersV2Assignment(
            'study',
            'members-v2-study'
        );

        $this->actingAs($student, 'web');

        $startResponse = $this->postJson("/miembros-v2/asignaciones/{$assignment->external_id}/intento", [])
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.attempt.mode', 'study')
            ->assertJsonPath('data.questions.0.id', $questionExternalId);

        $attemptId = (string) $startResponse->json('data.attempt.id');

        $this->patchJson("/miembros-v2/intentos/{$attemptId}/preguntas/{$questionExternalId}", [
            'option_id' => 'A',
        ])->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.question_id', $questionExternalId)
            ->assertJsonPath('data.correct_option_id', 'A')
            ->assertJsonPath('data.is_correct', true);
    }

    public function test_enrolled_student_can_start_and_submit_a_simulacro_attempt_through_members_v2_generic_route(): void
    {
        [$student, $assignment, $questionExternalId] = $this->makeMembersV2Assignment(
            'simulacro',
            'members-v2-simulacro',
            true
        );

        $this->actingAs($student, 'web');

        $startResponse = $this->postJson("/miembros-v2/asignaciones/{$assignment->external_id}/intento", [])
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.attempt.mode', 'simulacro')
            ->assertJsonPath('data.questions.0.id', $questionExternalId);

        $attemptId = (string) $startResponse->json('data.attempt.id');

        $this->patchJson("/miembros-v2/intentos/{$attemptId}/preguntas/{$questionExternalId}", [
            'option_id' => 'A',
        ])->assertOk()
            ->assertJsonPath('data.correct_option_id', null);

        $this->postJson("/miembros-v2/intentos/{$attemptId}/entregar", [])
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.attempt.submitted', true)
            ->assertJsonPath('data.attempt.can_review', true)
            ->assertJsonPath('data.attempt.score_scale', 5);
    }

    /**
     * @return array{0: User, 1: AssessmentAssignment, 2: string}
     */
    private function makeMembersV2Assignment(
        string $mode,
        string $suffix,
        bool $showFeedbackOnSubmit = false,
    ): array {
        $student = User::factory()->create([
            'email' => "{$suffix}@sanjoseitagui.edu.co",
            'role' => 'student',
            'member_status' => 'approved',
        ]);

        $course = Course::query()->create([
            'name' => 'Curso '.$suffix,
            'slug' => 'curso-'.$suffix,
            'school_year' => '2026',
            'is_active' => true,
        ]);

        CourseEnrollment::query()->create([
            'course_id' => $course->id,
            'user_id' => $student->id,
            'status' => 'active',
            'source' => 'phpunit',
        ]);

        $questionExternalId = 'q-'.$suffix;

        $template = AssessmentTemplate::query()->create([
            'external_id' => 'tpl-'.$suffix,
            'source_content_type' => $mode === AssessmentAssignment::MODE_SIMULACRO ? 'simulacro' : 'taller',
            'source_slug' => 'quimica/11-2026-s1/'.$suffix,
            'route' => '/simulacros/quimica/2026-s1/'.$suffix,
            'title' => 'Template '.$suffix,
            'total_questions' => 1,
            'questions_payload' => [],
        ]);

        AssessmentQuestion::query()->create([
            'template_id' => $template->id,
            'external_id' => $questionExternalId,
            'order_base' => 1,
            'source_slug' => $template->source_slug.'#'.$questionExternalId,
            'is_active' => true,
            'meta' => [],
            'stem_mdx' => 'Pregunta '.$suffix,
            'stem_html' => '<p>Pregunta '.$suffix.'</p>',
            'stem_assets' => [],
            'stem_blocks' => [],
            'options' => [
                ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
            ],
            'correct_option_id' => 'A',
            'feedback_mdx' => 'Explicacion '.$suffix,
            'feedback_html' => '<p>Explicacion '.$suffix.'</p>',
            'feedback_summary' => 'Retro '.$suffix,
            'feedback_assets' => [],
            'feedback_blocks' => [],
            'concepts_mdx' => 'Concepto '.$suffix,
            'concepts_html' => '<p>Concepto '.$suffix.'</p>',
            'concepts_summary' => 'Conceptos '.$suffix,
            'concepts_assets' => [],
            'concepts_blocks' => [],
            'app_payload_version' => 1,
        ]);

        $assignment = AssessmentAssignment::query()->create([
            'external_id' => 'asg-'.$suffix,
            'course_id' => $course->id,
            'template_id' => $template->id,
            'title' => 'Assignment '.$suffix,
            'mode' => $mode,
            'status' => AssessmentAssignment::STATUS_ACTIVE,
            'show_feedback_on_submit' => $showFeedbackOnSubmit,
            'opens_at' => now()->subMinute(),
            'closes_at' => now()->addHour(),
        ]);

        return [$student, $assignment, $questionExternalId];
    }
}
