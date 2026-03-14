<?php

namespace App\Services\Assessments;

use App\Models\AssessmentAssignment;
use App\Models\Course;
use App\Models\User;
use Illuminate\Database\Eloquent\Builder;

class AssessmentAssignmentAccessService
{
    /**
     * @return Builder<AssessmentAssignment>
     */
    public function accessibleAssignmentsQuery(User $user): Builder
    {
        $query = AssessmentAssignment::query()
            ->with(['course', 'template'])
            ->whereIn('status', [
                AssessmentAssignment::STATUS_ACTIVE,
                AssessmentAssignment::STATUS_CLOSED,
            ]);

        if ($user->isAdmin()) {
            return $query->orderByDesc('updated_at');
        }

        return $query
            ->whereIn('course_id', $this->accessibleCourseIdSubquery($user))
            ->orderByDesc('updated_at');
    }

    /**
     * @return array{
     *   can_view:bool,
     *   can_start:bool,
     *   state:string,
     *   code:string|null,
     *   message:string|null
     * }
     */
    public function availability(User $user, AssessmentAssignment $assignment): array
    {
        if ($user->isAdmin()) {
            return [
                'can_view' => true,
                'can_start' => true,
                'state' => 'admin',
                'code' => null,
                'message' => null,
            ];
        }

        $course = $assignment->course;
        if (! $course instanceof Course || ! $course->is_active) {
            return [
                'can_view' => false,
                'can_start' => false,
                'state' => 'course_inactive',
                'code' => 'course_inactive',
                'message' => 'El curso asociado no está disponible.',
            ];
        }

        $isEnrolled = $course->enrollments()
            ->where('user_id', $user->id)
            ->where('status', 'active')
            ->exists();

        if (! $isEnrolled) {
            return [
                'can_view' => false,
                'can_start' => false,
                'state' => 'access_denied',
                'code' => 'assignment_access_denied',
                'message' => 'Tu cuenta no tiene acceso a esta asignación.',
            ];
        }

        if ($assignment->status !== AssessmentAssignment::STATUS_ACTIVE) {
            return [
                'can_view' => true,
                'can_start' => false,
                'state' => $assignment->status,
                'code' => 'assignment_inactive',
                'message' => 'Esta asignación no está activa para iniciar nuevos intentos.',
            ];
        }

        if ($assignment->opens_at && $assignment->opens_at->isFuture()) {
            return [
                'can_view' => true,
                'can_start' => false,
                'state' => 'scheduled',
                'code' => 'assignment_not_open',
                'message' => 'La asignación aún no está abierta.',
            ];
        }

        if ($assignment->closes_at && $assignment->closes_at->isPast()) {
            return [
                'can_view' => true,
                'can_start' => false,
                'state' => 'closed',
                'code' => 'assignment_closed',
                'message' => 'La asignación ya cerró.',
            ];
        }

        return [
            'can_view' => true,
            'can_start' => true,
            'state' => 'active',
            'code' => null,
            'message' => null,
        ];
    }

    private function accessibleCourseIdSubquery(User $user)
    {
        return Course::query()
            ->select('courses.id')
            ->join('course_enrollments', 'course_enrollments.course_id', '=', 'courses.id')
            ->where('courses.is_active', true)
            ->where('course_enrollments.user_id', $user->id)
            ->where('course_enrollments.status', 'active')
            ->distinct();
    }
}
