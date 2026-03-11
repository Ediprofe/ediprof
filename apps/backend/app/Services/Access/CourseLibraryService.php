<?php

namespace App\Services\Access;

use App\Models\Course;
use App\Models\User;
use App\Models\Workshop;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Support\Collection;

class CourseLibraryService
{
    public function userHasWorkshopAccess(User $user, Workshop $workshop): bool
    {
        if ($user->isAdmin()) {
            return true;
        }

        return $this->accessibleWorkshopsQuery($user)
            ->where('workshops.id', $workshop->id)
            ->exists();
    }

    /**
     * @return Builder<Workshop>
     */
    public function accessibleWorkshopsQuery(User $user, ?string $contentType = null): Builder
    {
        $query = Workshop::query()->whereIn('workshops.id', $this->accessibleWorkshopIdSubquery($user));

        if (filled($contentType)) {
            $query->where('workshops.content_type', $contentType);
        }

        return $query;
    }

    /**
     * @return Collection<int, Course>
     */
    public function accessibleCourses(User $user): Collection
    {
        if ($user->isAdmin()) {
            return Course::query()
                ->where('is_active', true)
                ->orderBy('name')
                ->get();
        }

        return Course::query()
            ->select('courses.*')
            ->join('course_enrollments', 'course_enrollments.course_id', '=', 'courses.id')
            ->where('courses.is_active', true)
            ->where('course_enrollments.user_id', $user->id)
            ->where('course_enrollments.status', 'active')
            ->orderBy('courses.name')
            ->distinct('courses.id')
            ->get();
    }

    /**
     * @return array<int, array{id:int,name:string}>
     */
    public function workshopCourseMap(User $user, Collection $workshops): array
    {
        if ($workshops->isEmpty()) {
            return [];
        }

        if ($user->isAdmin()) {
            return [];
        }

        $rows = Course::query()
            ->select([
                'courses.id as course_id',
                'courses.name as course_name',
                'course_contents.workshop_id as workshop_id',
            ])
            ->join('course_enrollments', 'course_enrollments.course_id', '=', 'courses.id')
            ->join('course_contents', 'course_contents.course_id', '=', 'courses.id')
            ->where('courses.is_active', true)
            ->where('course_enrollments.user_id', $user->id)
            ->where('course_enrollments.status', 'active')
            ->where('course_contents.is_active', true)
            ->whereIn('course_contents.workshop_id', $workshops->pluck('id')->all())
            ->orderBy('courses.name')
            ->get();

        $map = [];
        foreach ($rows as $row) {
            $workshopId = (int) $row->workshop_id;
            $map[$workshopId] ??= [];
            $map[$workshopId][] = [
                'id' => (int) $row->course_id,
                'name' => (string) $row->course_name,
            ];
        }

        return $map;
    }

    private function accessibleWorkshopIdSubquery(User $user)
    {
        return Course::query()
            ->select('course_contents.workshop_id')
            ->join('course_enrollments', 'course_enrollments.course_id', '=', 'courses.id')
            ->join('course_contents', 'course_contents.course_id', '=', 'courses.id')
            ->where('courses.is_active', true)
            ->where('course_enrollments.user_id', $user->id)
            ->where('course_enrollments.status', 'active')
            ->where('course_contents.is_active', true)
            ->distinct();
    }
}
