<?php

namespace Tests\Feature;

use App\Models\ApiToken;
use App\Models\Plan;
use App\Models\Subscription;
use App\Models\User;
use App\Models\Workshop;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class WorkshopCatalogApiTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_returns_only_published_workshops_by_default(): void
    {
        $published = $this->createWorkshop('ws:published', true, 'free');
        $this->createWorkshop('ws:draft', false, 'free');

        $response = $this->getJson('/api/v1/workshops');

        $response
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('meta.total', 1)
            ->assertJsonPath('data.0.id', $published->external_id);
    }

    public function test_it_marks_premium_workshops_as_not_accessible_without_auth(): void
    {
        $free = $this->createWorkshop('ws:free', true, 'free');
        $premium = $this->createWorkshop('ws:premium', true, 'premium');

        $response = $this->getJson('/api/v1/workshops');

        $response->assertOk();

        $items = collect($response->json('data'));
        $freeItem = $items->firstWhere('id', $free->external_id);
        $premiumItem = $items->firstWhere('id', $premium->external_id);

        $this->assertNotNull($freeItem);
        $this->assertNotNull($premiumItem);
        $this->assertTrue((bool) $freeItem['can_access']);
        $this->assertFalse((bool) $premiumItem['can_access']);
    }

    public function test_it_marks_premium_workshops_as_accessible_with_active_subscription_token(): void
    {
        $user = User::factory()->create();
        $plainToken = $this->issueToken($user);

        $plan = Plan::query()->create([
            'code' => 'premium-mensual',
            'name' => 'Premium Mensual',
            'description' => 'Acceso premium',
            'price_cents' => 19900,
            'currency' => 'COP',
            'billing_interval' => 'monthly',
            'is_active' => true,
            'metadata' => [],
        ]);

        Subscription::query()->create([
            'user_id' => $user->id,
            'plan_id' => $plan->id,
            'status' => 'active',
            'provider' => 'manual',
            'provider_subscription_id' => 'sub-catalog-1',
            'starts_at' => now()->subDay(),
            'ends_at' => now()->addDays(15),
            'trial_ends_at' => null,
            'canceled_at' => null,
            'metadata' => [],
        ]);

        $premium = $this->createWorkshop('ws:premium:sub', true, 'premium');

        $response = $this
            ->withHeaders(['Authorization' => 'Bearer '.$plainToken])
            ->getJson('/api/v1/workshops');

        $response->assertOk();

        $premiumItem = collect($response->json('data'))->firstWhere('id', $premium->external_id);

        $this->assertNotNull($premiumItem);
        $this->assertTrue((bool) $premiumItem['can_access']);
    }

    private function createWorkshop(string $externalId, bool $published, string $tier): Workshop
    {
        return Workshop::query()->create([
            'external_id' => $externalId,
            'content_external_id' => $externalId,
            'title' => 'Taller '.str_replace(':', ' ', $externalId),
            'route' => '/saber/quimica/'.$externalId,
            'area_slug' => 'quimica',
            'unidad_slug' => 'la-materia',
            'access_tier' => $tier,
            'is_published' => $published,
            'total_questions' => 1,
            'total_assets' => 0,
            'assets' => [],
            'questions' => [
                [
                    'id' => '1',
                    'order' => 1,
                    'meta' => [],
                    'stem_mdx' => 'Pregunta',
                    'stem_assets' => [],
                    'options' => [
                        ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retro',
                    'feedback_assets' => [],
                ],
            ],
            'metadata' => [],
            'synced_at' => now(),
        ]);
    }

    private function issueToken(User $user): string
    {
        $plainToken = 'ep_test_'.bin2hex(random_bytes(16));

        ApiToken::query()->create([
            'user_id' => $user->id,
            'name' => 'mobile-test',
            'token_hash' => hash('sha256', $plainToken),
            'expires_at' => now()->addDays(30),
            'last_used_at' => null,
            'revoked_at' => null,
            'metadata' => [],
        ]);

        return $plainToken;
    }
}
