<?php

namespace App\Http\Controllers\Web;

use App\Http\Controllers\Controller;
use App\Models\AssessmentAssignment;
use App\Models\Course;
use App\Models\User;
use App\Services\Assessments\AssessmentAssignmentAccessService;
use App\Services\Members\MemberAssignmentPresenter;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Http\Request;
use Inertia\Inertia;
use Inertia\Response;

class MembersController extends Controller
{
    public function dashboard(
        Request $request,
        AssessmentAssignmentAccessService $accessService,
        MemberAssignmentPresenter $presenter,
    ): Response {
        /** @var User $user */
        $user = $request->user();
        $assignments = $this->loadAssignments($user, $accessService, $presenter);

        $evaluations = $assignments->where('mode', AssessmentAssignment::MODE_EVALUATION)->values();
        $workshops = $assignments->where('mode', AssessmentAssignment::MODE_STUDY)->values();
        $simulacros = $assignments->where('mode', AssessmentAssignment::MODE_SIMULACRO)->values();

        return Inertia::render('Members/Dashboard', [
            'pageTitle' => 'Panel del estudiante',
            'subtitle' => 'Desde aquí vas a entrar a tus evaluaciones, talleres y simulacros sin depender del frontend anterior.',
            'quickStats' => [
                ['label' => 'Evaluaciones', 'value' => $evaluations->count()],
                ['label' => 'Talleres', 'value' => $workshops->count()],
                ['label' => 'Simulacros', 'value' => $simulacros->count()],
                ['label' => 'Cursos activos', 'value' => $this->activeCourseCount($user)],
            ],
            'nextActions' => $evaluations
                ->take(3)
                ->map(fn (array $item): array => $this->summarizeAssignment($item))
                ->all(),
            'sections' => [
                [
                    'title' => 'Evaluaciones',
                    'description' => 'Actividades calificables con intentos, resultados y retroalimentación controlada.',
                    'href' => route('members.evaluations'),
                    'count' => $evaluations->count(),
                    'emoji' => '📝',
                ],
                [
                    'title' => 'Talleres',
                    'description' => 'Prácticas guiadas para reforzar conceptos con revisión continua.',
                    'href' => route('members.workshops'),
                    'count' => $workshops->count(),
                    'emoji' => '✍️',
                ],
                [
                    'title' => 'Simulacros',
                    'description' => 'Entrenamientos diagnósticos con el mismo backend que luego servirá al móvil.',
                    'href' => route('members.simulacros'),
                    'count' => $simulacros->count(),
                    'emoji' => '🚀',
                ],
            ],
        ]);
    }

    public function evaluations(
        Request $request,
        AssessmentAssignmentAccessService $accessService,
        MemberAssignmentPresenter $presenter,
    ): Response {
        /** @var User $user */
        $user = $request->user();

        $items = $this->loadAssignments($user, $accessService, $presenter, AssessmentAssignment::MODE_EVALUATION)
            ->values()
            ->all();

        return Inertia::render('Members/Evaluations/Index', [
            'pageTitle' => 'Evaluaciones',
            'subtitle' => 'Listado real de evaluaciones disponibles para tu cuenta en esta nueva app web.',
            'items' => $items,
        ]);
    }

    public function showEvaluation(
        Request $request,
        string $evaluation,
        AssessmentAssignmentAccessService $accessService,
        MemberAssignmentPresenter $presenter,
    ): Response {
        /** @var User $user */
        $user = $request->user();

        $assignment = $this->resolveAssignmentByMode($user, $accessService, $evaluation, AssessmentAssignment::MODE_EVALUATION);

        $item = $presenter->present($assignment, $user);

        abort_unless((bool) $item['availability']['can_view'], 403, $item['availability']['message'] ?? 'Tu cuenta no tiene acceso a esta evaluación.');

        return Inertia::render('Members/Evaluations/Show', [
            'pageTitle' => 'Detalle de evaluación',
            'subtitle' => 'Esta vista ya usa el assignment real del backend y será la base del player web nuevo.',
            'evaluation' => $item,
        ]);
    }

    public function workshops(
        Request $request,
        AssessmentAssignmentAccessService $accessService,
        MemberAssignmentPresenter $presenter,
    ): Response {
        /** @var User $user */
        $user = $request->user();

        return Inertia::render('Members/Workshops/Index', [
            'pageTitle' => 'Talleres',
            'subtitle' => 'Talleres disponibles para tu cuenta en Members v2.',
            'items' => $this->loadAssignments($user, $accessService, $presenter, AssessmentAssignment::MODE_STUDY)->values()->all(),
        ]);
    }

    public function showWorkshop(
        Request $request,
        string $workshop,
        AssessmentAssignmentAccessService $accessService,
        MemberAssignmentPresenter $presenter,
    ): Response {
        /** @var User $user */
        $user = $request->user();

        $assignment = $this->resolveAssignmentByMode($user, $accessService, $workshop, AssessmentAssignment::MODE_STUDY);
        $item = $presenter->present($assignment, $user);

        abort_unless((bool) $item['availability']['can_view'], 403, $item['availability']['message'] ?? 'Tu cuenta no tiene acceso a este taller.');

        return Inertia::render('Members/Workshops/Show', [
            'pageTitle' => 'Detalle de taller',
            'subtitle' => 'Este taller ya funciona sobre la misma base web nueva y comparte el intento real del backend.',
            'workshop' => $item,
        ]);
    }

    public function simulacros(
        Request $request,
        AssessmentAssignmentAccessService $accessService,
        MemberAssignmentPresenter $presenter,
    ): Response {
        /** @var User $user */
        $user = $request->user();

        return Inertia::render('Members/Simulacros/Index', [
            'pageTitle' => 'Simulacros',
            'subtitle' => 'Simulacros disponibles para tu cuenta en Members v2.',
            'items' => $this->loadAssignments($user, $accessService, $presenter, AssessmentAssignment::MODE_SIMULACRO)->values()->all(),
        ]);
    }

    public function showSimulacro(
        Request $request,
        string $simulacro,
        AssessmentAssignmentAccessService $accessService,
        MemberAssignmentPresenter $presenter,
    ): Response {
        /** @var User $user */
        $user = $request->user();

        $assignment = $this->resolveAssignmentByMode($user, $accessService, $simulacro, AssessmentAssignment::MODE_SIMULACRO);
        $item = $presenter->present($assignment, $user);

        abort_unless((bool) $item['availability']['can_view'], 403, $item['availability']['message'] ?? 'Tu cuenta no tiene acceso a este simulacro.');

        return Inertia::render('Members/Simulacros/Show', [
            'pageTitle' => 'Detalle de simulacro',
            'subtitle' => 'Este simulacro ya comparte la misma base del panel web nuevo y prepara el camino para el cliente móvil.',
            'simulacro' => $item,
        ]);
    }

    private function activeCourseCount(User $user): int
    {
        if ($user->isAdmin()) {
            return Course::query()
                ->where('is_active', true)
                ->count();
        }

        return $user->courseEnrollments()
            ->where('status', 'active')
            ->count();
    }

    /**
     * @return \Illuminate\Support\Collection<int, array<string, mixed>>
     */
    private function loadAssignments(
        User $user,
        AssessmentAssignmentAccessService $accessService,
        MemberAssignmentPresenter $presenter,
        ?string $mode = null,
    ) {
        $query = $this->baseAssignmentsQuery($user, $accessService);

        if ($mode !== null) {
            $query->where('mode', $mode);
        }

        return $query->get()
            ->map(fn (AssessmentAssignment $assignment): array => $presenter->present($assignment, $user))
            ->filter(fn (array $assignment): bool => (bool) ($assignment['availability']['can_view'] ?? false))
            ->values();
    }

    /**
     * @return Builder<AssessmentAssignment>
     */
    private function baseAssignmentsQuery(
        User $user,
        AssessmentAssignmentAccessService $accessService,
    ): Builder {
        return $accessService->accessibleAssignmentsQuery($user)
            ->withCount([
                'questions',
                'attempts as user_attempts_count' => fn ($builder) => $builder->where('user_id', $user->id),
            ])
            ->with([
                'attempts' => fn ($builder) => $builder
                    ->where('user_id', $user->id)
                    ->latest('id'),
            ]);
    }

    private function resolveAssignmentByMode(
        User $user,
        AssessmentAssignmentAccessService $accessService,
        string $identifier,
        string $mode,
    ): AssessmentAssignment {
        return $this->baseAssignmentsQuery($user, $accessService)
            ->where('mode', $mode)
            ->where(function (Builder $query) use ($identifier): void {
                $decoded = trim(rawurldecode($identifier));
                $query->where('external_id', $decoded);

                if (ctype_digit($decoded)) {
                    $query->orWhere('id', (int) $decoded);
                }
            })
            ->firstOrFail();
    }

    /**
     * @param  array<string, mixed>  $assignment
     * @return array<string, mixed>
     */
    private function summarizeAssignment(array $assignment): array
    {
        return [
            'id' => $assignment['id'],
            'title' => $assignment['title'],
            'status' => $assignment['latest_attempt']['feedback_state_label']
                ?? $assignment['availability']['state']
                ?? 'Disponible',
            'questions' => $assignment['stats']['effective_questions'] ?? 0,
            'href' => route('members.evaluations.show', $assignment['id']),
        ];
    }
}
