<?php

namespace App\Services\Access;

use App\Models\User;
use App\Models\Workshop;
use Illuminate\Support\Carbon;

class WorkshopAccessService
{
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

        if ($this->hasActiveSubscription($user)) {
            return true;
        }

        if ($user->member_status !== 'approved') {
            return false;
        }

        return $this->hasActiveGrant($user, $workshop);
    }

    private function hasActiveSubscription(User $user): bool
    {
        $now = Carbon::now();

        return $user->subscriptions()
            ->whereIn('status', ['active', 'trialing'])
            ->where(function ($query) use ($now): void {
                $query
                    ->whereNull('starts_at')
                    ->orWhere('starts_at', '<=', $now);
            })
            ->where(function ($query) use ($now): void {
                $query
                    ->whereNull('ends_at')
                    ->orWhere('ends_at', '>', $now);
            })
            ->whereHas('plan', function ($query): void {
                $query->where('is_active', true);
            })
            ->exists();
    }

    private function hasActiveGrant(User $user, Workshop $workshop): bool
    {
        $now = Carbon::now();
        $grants = $user->accessGrants()
            ->where('is_active', true)
            ->where(function ($query) use ($now): void {
                $query
                    ->whereNull('starts_at')
                    ->orWhere('starts_at', '<=', $now);
            })
            ->where(function ($query) use ($now): void {
                $query
                    ->whereNull('ends_at')
                    ->orWhere('ends_at', '>', $now);
            })
            ->get(['scope', 'scope_ref']);

        foreach ($grants as $grant) {
            if ($this->grantMatchesWorkshop($grant->scope, $grant->scope_ref, $workshop)) {
                return true;
            }
        }

        return false;
    }

    private function grantMatchesWorkshop(string $scope, ?string $scopeRef, Workshop $workshop): bool
    {
        $normalizedScope = mb_strtolower(trim($scope));
        $normalizedRef = $scopeRef === null ? null : trim($scopeRef);

        if ($normalizedScope === 'global') {
            return $normalizedRef === null
                || $normalizedRef === ''
                || $normalizedRef === '*'
                || mb_strtolower($normalizedRef) === 'all';
        }

        if (in_array($normalizedScope, ['workshop', 'content'], true)) {
            $validRefs = array_filter([
                $workshop->external_id,
                $workshop->content_external_id,
                $workshop->route,
            ]);

            return $normalizedRef !== null && in_array($normalizedRef, $validRefs, true);
        }

        if ($normalizedScope === 'route') {
            return $normalizedRef !== null && $normalizedRef === $workshop->route;
        }

        if ($normalizedScope === 'area') {
            return $normalizedRef !== null
                && $workshop->area_slug !== null
                && $normalizedRef === $workshop->area_slug;
        }

        if ($normalizedScope === 'unidad') {
            return $normalizedRef !== null
                && $workshop->unidad_slug !== null
                && $normalizedRef === $workshop->unidad_slug;
        }

        if (in_array($normalizedScope, ['tier', 'access_tier'], true)) {
            return $normalizedRef !== null && $normalizedRef === $workshop->access_tier;
        }

        return false;
    }
}
