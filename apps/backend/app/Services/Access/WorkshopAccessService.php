<?php

namespace App\Services\Access;

use App\Models\User;
use App\Models\Workshop;

class WorkshopAccessService
{
    public function __construct(
        private readonly CourseLibraryService $courseLibraryService
    ) {
    }

    public function canAccessWorkshop(?User $user, Workshop $workshop): bool
    {
        if ($workshop->access_tier !== 'premium') {
            return true;
        }

        if ($user === null) {
            return false;
        }

        if ($user->isAdmin()) {
            return true;
        }

        if ($user->member_status !== 'approved') {
            return false;
        }

        if ($this->courseLibraryService->userHasWorkshopAccess($user, $workshop)) {
            return true;
        }

        return false;
    }
}
