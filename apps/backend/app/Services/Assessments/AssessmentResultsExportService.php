<?php

namespace App\Services\Assessments;

use App\Models\AssessmentAssignment;
use App\Models\AssessmentAttempt;
use App\Models\Course;
use App\Models\User;
use Illuminate\Support\Collection;
use Illuminate\Support\Str;
use Symfony\Component\HttpFoundation\StreamedResponse;
use Symfony\Component\HttpFoundation\Response;

class AssessmentResultsExportService
{
    /**
     * @return array<int, string>
     */
    public function headers(): array
    {
        return [
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
        ];
    }

    public function streamAssignmentCsv(AssessmentAssignment $assignment): StreamedResponse
    {
        return $this->streamCsv(
            $this->assignmentFilename($assignment),
            $this->assignmentRows($assignment),
        );
    }

    public function downloadAssignmentExcel(AssessmentAssignment $assignment): Response
    {
        return $this->downloadAssignmentSheet(
            $assignment,
            $this->assignmentGradebookHeaders(),
            $this->assignmentGradebookRows($assignment),
            $this->assignmentExcelFilename($assignment),
            'copia la columna Nota / 5 al sistema del colegio.'
        );
    }

    public function downloadAssignmentMinimalExcel(AssessmentAssignment $assignment): Response
    {
        return $this->downloadAssignmentSheet(
            $assignment,
            $this->assignmentMinimalHeaders(),
            $this->assignmentMinimalRows($assignment),
            $this->assignmentMinimalExcelFilename($assignment),
            'usa esta lista corta cuando solo necesites comparar apellidos, nombres y pegar la nota.'
        );
    }

    /**
     * @param  array<int, string>  $headers
     * @param  Collection<int, array<int, string>>  $rows
     */
    protected function downloadAssignmentSheet(
        AssessmentAssignment $assignment,
        array $headers,
        Collection $rows,
        string $filename,
        string $usageHint,
    ): Response {
        return response()->view('admin.exports.assignment-gradebook', [
            'title' => $assignment->title,
            'courseName' => $assignment->course?->name ?? '',
            'templateTitle' => $assignment->template?->title ?? '',
            'headers' => $headers,
            'rows' => $rows,
            'usageHint' => $usageHint,
        ], 200, [
            'Content-Type' => 'application/vnd.ms-excel; charset=UTF-8',
            'Content-Disposition' => sprintf('attachment; filename="%s"', $filename),
            'Cache-Control' => 'no-store, no-cache',
        ]);
    }

    public function streamCourseCsv(Course $course): StreamedResponse
    {
        return $this->streamCsv(
            $this->courseFilename($course),
            $this->courseRows($course),
        );
    }

    /**
     * @return Collection<int, array<int, string>>
     */
    public function assignmentRows(AssessmentAssignment $assignment): Collection
    {
        return $this->buildRows(
            $this->baseAttemptQuery()
                ->where('assignment_id', $assignment->id)
                ->get()
        );
    }

    /**
     * @return array<int, string>
     */
    public function assignmentGradebookHeaders(): array
    {
        return [
            'N°',
            'Apellidos',
            'Nombres',
            'Matricula',
            'Documento',
            'Correo institucional',
            'Nota / 5',
        ];
    }

    /**
     * @return Collection<int, array<int, string>>
     */
    public function assignmentGradebookRows(AssessmentAssignment $assignment): Collection
    {
        return $this->sortedAttempts(
            $this->baseAttemptQuery()
                ->where('assignment_id', $assignment->id)
                ->get()
        )->values()->map(fn (AssessmentAttempt $attempt, int $index): array => [
            (string) ($index + 1),
            $this->exportLastNames($attempt->user),
            $this->exportFirstNames($attempt->user),
            (string) ($attempt->user?->institutional_code ?? ''),
            (string) ($attempt->user?->document_number ?? ''),
            (string) ($attempt->user?->email ?? ''),
            $attempt->score_scale === null ? '' : number_format((float) $attempt->score_scale, 2, '.', ''),
        ]);
    }

    /**
     * @return array<int, string>
     */
    public function assignmentMinimalHeaders(): array
    {
        return [
            'Apellidos',
            'Nombres',
            'Nota / 5',
        ];
    }

    /**
     * @return Collection<int, array<int, string>>
     */
    public function assignmentMinimalRows(AssessmentAssignment $assignment): Collection
    {
        return $this->sortedAttempts(
            $this->baseAttemptQuery()
                ->where('assignment_id', $assignment->id)
                ->get()
        )->values()->map(fn (AssessmentAttempt $attempt): array => [
            $this->exportLastNames($attempt->user),
            $this->exportFirstNames($attempt->user),
            $attempt->score_scale === null ? '' : number_format((float) $attempt->score_scale, 2, '.', ''),
        ]);
    }

    /**
     * @return Collection<int, array<int, string>>
     */
    public function courseRows(Course $course): Collection
    {
        return $this->buildRows(
            $this->baseAttemptQuery()
                ->whereHas('assignment', fn ($query) => $query->where('course_id', $course->id))
                ->get()
        );
    }

    protected function streamCsv(string $filename, Collection $rows): StreamedResponse
    {
        return response()->streamDownload(function () use ($rows): void {
            $output = fopen('php://output', 'wb');

            if ($output === false) {
                throw new \RuntimeException('Could not open the CSV output stream.');
            }

            fwrite($output, "\xEF\xBB\xBF");
            fputcsv($output, $this->headers(), ';');

            foreach ($rows as $row) {
                fputcsv($output, $row, ';');
            }

            fclose($output);
        }, $filename, [
            'Content-Type' => 'text/csv; charset=UTF-8',
            'Cache-Control' => 'no-store, no-cache',
        ]);
    }

    protected function assignmentFilename(AssessmentAssignment $assignment): string
    {
        $slug = Str::slug($assignment->title ?: 'asignacion');

        return sprintf(
            'resultados-%s-%s.csv',
            $slug !== '' ? $slug : 'asignacion',
            now()->format('Ymd-His'),
        );
    }

    protected function assignmentExcelFilename(AssessmentAssignment $assignment): string
    {
        $slug = Str::slug($assignment->title ?: 'asignacion');

        return sprintf(
            'notas-%s-%s.xls',
            $slug !== '' ? $slug : 'asignacion',
            now()->format('Ymd-His'),
        );
    }

    protected function assignmentMinimalExcelFilename(AssessmentAssignment $assignment): string
    {
        $slug = Str::slug($assignment->title ?: 'asignacion');

        return sprintf(
            'notas-minimas-%s-%s.xls',
            $slug !== '' ? $slug : 'asignacion',
            now()->format('Ymd-His'),
        );
    }

    protected function courseFilename(Course $course): string
    {
        $slug = Str::slug($course->name ?: 'curso');

        return sprintf(
            'consolidado-%s-%s.csv',
            $slug !== '' ? $slug : 'curso',
            now()->format('Ymd-His'),
        );
    }

    protected function baseAttemptQuery()
    {
        return AssessmentAttempt::query()
            ->with([
                'user',
                'assignment.course',
                'assignment.template',
            ])
            ->withCount('answers');
    }

    /**
     * @param  Collection<int, AssessmentAttempt>  $attempts
     * @return Collection<int, array<int, string>>
     */
    protected function buildRows(Collection $attempts): Collection
    {
        return $this->sortedAttempts($attempts)
            ->values()
            ->map(fn (AssessmentAttempt $attempt): array => [
                $this->exportLastNames($attempt->user),
                $this->exportFirstNames($attempt->user),
                (string) ($attempt->user?->institutional_code ?? ''),
                (string) ($attempt->user?->document_number ?? ''),
                (string) ($attempt->user?->email ?? ''),
                (string) ($attempt->assignment?->course?->name ?? ''),
                (string) ($attempt->assignment?->title ?? ''),
                (string) ($attempt->assignment?->template?->title ?? ''),
                $this->modeLabel((string) $attempt->mode),
                $this->attemptStatusLabel((string) $attempt->status),
                (string) ($attempt->answers_count ?? 0),
                (string) $attempt->total_questions,
                $attempt->score_percent === null ? '' : (string) $attempt->score_percent,
                $attempt->score_scale === null ? '' : number_format((float) $attempt->score_scale, 2, '.', ''),
                $attempt->started_at?->format('Y-m-d H:i:s') ?? '',
                $attempt->submitted_at?->format('Y-m-d H:i:s') ?? '',
                $attempt->review_released_at?->format('Y-m-d H:i:s') ?? '',
            ]);
    }

    /**
     * @param  Collection<int, AssessmentAttempt>  $attempts
     * @return Collection<int, AssessmentAttempt>
     */
    protected function sortedAttempts(Collection $attempts): Collection
    {
        return $attempts->sortBy(fn (AssessmentAttempt $attempt): string => implode('|', [
            $this->sortLastNames($attempt->user),
            $this->sortFirstNames($attempt->user),
            (string) ($attempt->user?->institutional_code ?? ''),
            (string) ($attempt->assignment?->title ?? ''),
            (string) ($attempt->submitted_at?->format('Y-m-d H:i:s') ?? ''),
        ]));
    }

    protected function exportLastNames(?User $user): string
    {
        if ($user === null) {
            return '';
        }

        if (filled($user->last_names)) {
            return (string) $user->last_names;
        }

        $split = User::splitAcademicName($user->name);

        return (string) ($split['last_names'] ?? '');
    }

    protected function exportFirstNames(?User $user): string
    {
        if ($user === null) {
            return '';
        }

        if (filled($user->first_names)) {
            return (string) $user->first_names;
        }

        $split = User::splitAcademicName($user->name);

        return (string) ($split['first_names'] ?? $user->name ?? '');
    }

    protected function sortLastNames(?User $user): string
    {
        return mb_strtoupper($this->exportLastNames($user));
    }

    protected function sortFirstNames(?User $user): string
    {
        return mb_strtoupper($this->exportFirstNames($user));
    }

    protected function modeLabel(string $mode): string
    {
        return match ($mode) {
            AssessmentAssignment::MODE_STUDY => 'Estudio guiado',
            AssessmentAssignment::MODE_SIMULACRO => 'Simulacro',
            AssessmentAssignment::MODE_EVALUATION => 'Evaluacion',
            default => $mode,
        };
    }

    protected function attemptStatusLabel(string $status): string
    {
        return match ($status) {
            'in_progress' => 'En progreso',
            'submitted' => 'Entregado',
            'graded' => 'Calificado',
            'released' => 'Revision liberada',
            default => $status,
        };
    }
}
