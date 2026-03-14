<?php

namespace Tests\Feature;

use App\Models\AssessmentAssignment;
use App\Models\AssessmentAttempt;
use App\Models\AssessmentAttemptAnswer;
use App\Models\AssessmentTemplate;
use App\Models\Course;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Carbon;
use Tests\TestCase;

class AssessmentResultsExportTest extends TestCase
{
    use RefreshDatabase;

    public function test_admin_can_download_assignment_results_csv(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        [$course, $assignment] = $this->makeCourseAssignment();
        $student = User::factory()->create([
            'name' => 'AGUDELO BETANCUR, MANUELA',
            'first_names' => 'MANUELA',
            'last_names' => 'AGUDELO BETANCUR',
            'email' => 'manuelaagudelob@sanjoseitagui.edu.co',
            'institutional_code' => '150081',
            'document_number' => '1035978574',
        ]);

        $attempt = $this->makeAttempt($assignment, $student, [
            'score_raw' => 12,
            'score_percent' => 63,
            'score_scale' => 3.15,
        ]);

        AssessmentAttemptAnswer::query()->create([
            'attempt_id' => $attempt->id,
            'question_external_id' => 'q-1',
            'position' => 1,
            'selected_option_id' => 'B',
            'is_correct' => true,
            'answered_at' => Carbon::parse('2026-03-13 10:10:00'),
        ]);

        $response = $this->actingAs($admin)
            ->get(route('admin.exports.assignments.results', ['assignment' => $assignment]));

        $content = $response->streamedContent();

        $response->assertOk();
        $response->assertHeader('content-type', 'text/csv; charset=UTF-8');

        $rows = $this->parseCsvContent($content);

        $this->assertSame([
            'Apellidos',
            'Nombres',
            'Matricula',
            'Documento',
            'Correo institucional',
            'Curso',
            'Asignacion',
            'Plantilla base',
            'Modo',
            'Estado intento',
            'Respondidas',
            'Total preguntas',
            'Puntaje %',
            'Nota / 5',
            'Inicio',
            'Entrega',
            'Revision liberada',
        ], $rows[0]);
        $this->assertSame([
            'AGUDELO BETANCUR',
            'MANUELA',
            '150081',
            '1035978574',
            'manuelaagudelob@sanjoseitagui.edu.co',
            $course->name,
            $assignment->title,
            'Simulacro 11 · Ciencias Naturales · S1',
            'Evaluacion',
            'Entregado',
            '1',
            '19',
            '63',
            '3.15',
            '2026-03-13 10:00:00',
            '2026-03-13 10:15:00',
            '',
        ], $rows[1]);
    }

    public function test_admin_can_download_assignment_results_excel(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        [$course, $assignment] = $this->makeCourseAssignment();
        $student = User::factory()->create([
            'name' => 'AGUDELO BETANCUR, MANUELA',
            'first_names' => 'MANUELA',
            'last_names' => 'AGUDELO BETANCUR',
            'email' => 'manuelaagudelob@sanjoseitagui.edu.co',
            'institutional_code' => '150081',
            'document_number' => '1035978574',
        ]);

        $this->makeAttempt($assignment, $student, [
            'score_raw' => 12,
            'score_percent' => 63,
            'score_scale' => 3.15,
        ]);

        $response = $this->actingAs($admin)
            ->get(route('admin.exports.assignments.results.excel', ['assignment' => $assignment]));

        $response->assertOk();
        $response->assertHeader('content-type', 'application/vnd.ms-excel; charset=UTF-8');
        $response->assertSee('sim1', false);
        $response->assertSee($course->name, false);
        $response->assertSee('AGUDELO BETANCUR', false);
        $response->assertSee('3.15', false);
        $response->assertSee('Nota / 5', false);
        $response->assertDontSee('Puntaje %', false);
        $response->assertDontSee('Estado intento', false);
    }

    public function test_admin_can_download_assignment_minimal_excel(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        [, $assignment] = $this->makeCourseAssignment();
        $student = User::factory()->create([
            'name' => 'AGUDELO BETANCUR, MANUELA',
            'first_names' => 'MANUELA',
            'last_names' => 'AGUDELO BETANCUR',
            'email' => 'manuelaagudelob@sanjoseitagui.edu.co',
            'institutional_code' => '150081',
            'document_number' => '1035978574',
        ]);

        $this->makeAttempt($assignment, $student, [
            'score_raw' => 12,
            'score_percent' => 63,
            'score_scale' => 3.15,
        ]);

        $response = $this->actingAs($admin)
            ->get(route('admin.exports.assignments.results.excel_minimal', ['assignment' => $assignment]));

        $response->assertOk();
        $response->assertHeader('content-type', 'application/vnd.ms-excel; charset=UTF-8');
        $response->assertSee('Apellidos', false);
        $response->assertSee('Nombres', false);
        $response->assertSee('Nota / 5', false);
        $response->assertSee('AGUDELO BETANCUR', false);
        $response->assertSee('MANUELA', false);
        $response->assertSee('3.15', false);
        $response->assertDontSee('Matricula', false);
        $response->assertDontSee('Documento', false);
        $response->assertDontSee('Correo institucional', false);
    }

    public function test_admin_can_download_course_results_csv_sorted_by_apellidos(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        [, $assignment] = $this->makeCourseAssignment();

        $zapata = User::factory()->create([
            'name' => 'ZAPATA LUNA, ANA',
            'first_names' => 'ANA',
            'last_names' => 'ZAPATA LUNA',
            'email' => 'anazapata@sanjoseitagui.edu.co',
            'institutional_code' => '300001',
            'document_number' => '300001',
        ]);

        $agudelo = User::factory()->create([
            'name' => 'AGUDELO BETANCUR, MANUELA',
            'first_names' => 'MANUELA',
            'last_names' => 'AGUDELO BETANCUR',
            'email' => 'manuelaagudelob@sanjoseitagui.edu.co',
            'institutional_code' => '150081',
            'document_number' => '1035978574',
        ]);

        $this->makeAttempt($assignment, $zapata, [
            'score_raw' => 10,
            'score_percent' => 53,
            'score_scale' => 2.65,
        ]);

        $this->makeAttempt($assignment, $agudelo, [
            'score_raw' => 18,
            'score_percent' => 95,
            'score_scale' => 4.75,
        ]);

        $response = $this->actingAs($admin)
            ->get(route('admin.exports.courses.results', ['course' => $assignment->course]));

        $rows = $this->parseCsvContent($response->streamedContent());

        $response->assertOk();

        $this->assertSame('AGUDELO BETANCUR', $rows[1][0]);
        $this->assertSame('ZAPATA LUNA', $rows[2][0]);
    }

    /**
     * @return array{0: Course, 1: AssessmentAssignment}
     */
    protected function makeCourseAssignment(): array
    {
        $course = Course::query()->create([
            'name' => 'ICFES 11°1',
            'slug' => 'icfes-11-1',
            'school_year' => '2026',
            'is_active' => true,
        ]);

        $template = AssessmentTemplate::query()->create([
            'external_id' => 'tmpl-simulacro-11-s1',
            'title' => 'Simulacro 11 · Ciencias Naturales · S1',
            'source_content_type' => 'simulacro',
            'default_mode' => AssessmentAssignment::MODE_EVALUATION,
            'route' => '/simulacros/quimica/2026-s1/taller',
            'access_tier' => 'premium',
            'is_published' => true,
            'total_questions' => 19,
            'total_assets' => 0,
        ]);

        $assignment = AssessmentAssignment::query()->create([
            'external_id' => 'assign-sim-11-1',
            'course_id' => $course->id,
            'template_id' => $template->id,
            'title' => 'sim1',
            'mode' => AssessmentAssignment::MODE_EVALUATION,
            'status' => AssessmentAssignment::STATUS_ACTIVE,
            'randomize_questions' => true,
            'show_feedback_on_submit' => false,
            'show_feedback_after_close' => false,
            'max_attempts' => 1,
            'time_limit_minutes' => 20,
        ]);

        return [$course, $assignment];
    }

    /**
     * @param  array<string, mixed>  $overrides
     */
    protected function makeAttempt(AssessmentAssignment $assignment, User $student, array $overrides = []): AssessmentAttempt
    {
        $defaults = [
            'assignment_id' => $assignment->id,
            'template_id' => $assignment->template_id,
            'user_id' => $student->id,
            'mode' => $assignment->mode,
            'status' => 'submitted',
            'question_order' => ['S1-1', 'S1-2'],
            'questions_snapshot' => [],
            'total_questions' => 19,
            'score_raw' => 0,
            'score_percent' => 0,
            'score_scale' => 0,
            'started_at' => Carbon::parse('2026-03-13 10:00:00'),
            'submitted_at' => Carbon::parse('2026-03-13 10:15:00'),
            'graded_at' => Carbon::parse('2026-03-13 10:15:00'),
            'last_activity_at' => Carbon::parse('2026-03-13 10:15:00'),
        ];

        return AssessmentAttempt::query()->create(array_merge($defaults, $overrides));
    }

    /**
     * @return array<int, array<int, string>>
     */
    protected function parseCsvContent(string $content): array
    {
        $normalized = str_starts_with($content, "\xEF\xBB\xBF")
            ? substr($content, 3)
            : $content;
        $lines = preg_split('/\r\n|\n|\r/', trim($normalized)) ?: [];

        return array_values(array_map(
            fn (string $line): array => str_getcsv($line, ';'),
            array_filter($lines, fn (string $line): bool => $line !== '')
        ));
    }
}
