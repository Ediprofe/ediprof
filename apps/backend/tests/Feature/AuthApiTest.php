<?php

namespace Tests\Feature;

use App\Models\ApiToken;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AuthApiTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_returns_bearer_token_for_valid_credentials(): void
    {
        $user = User::factory()->create([
            'email' => 'demo@ediprofe.com',
            'password' => 'secreto123',
        ]);

        $response = $this->postJson('/api/v1/auth/login', [
            'email' => 'demo@ediprofe.com',
            'password' => 'secreto123',
            'device_name' => 'iphone-docente',
            'expires_in_days' => 15,
        ]);

        $response
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.user.id', $user->id)
            ->assertJsonPath('data.token_type', 'Bearer');

        $token = (string) $response->json('data.token');
        $this->assertNotEmpty($token);

        $this->assertDatabaseHas('api_tokens', [
            'user_id' => $user->id,
            'name' => 'iphone-docente',
            'token_hash' => hash('sha256', $token),
        ]);
    }

    public function test_it_rejects_invalid_credentials(): void
    {
        User::factory()->create([
            'email' => 'demo@ediprofe.com',
            'password' => 'secreto123',
        ]);

        $response = $this->postJson('/api/v1/auth/login', [
            'email' => 'demo@ediprofe.com',
            'password' => 'incorrecta',
        ]);

        $response
            ->assertStatus(422)
            ->assertJsonPath('ok', false)
            ->assertJsonPath('error.code', 'invalid_credentials');
    }

    public function test_me_requires_bearer_token(): void
    {
        $response = $this->getJson('/api/v1/auth/me');

        $response
            ->assertStatus(401)
            ->assertJsonPath('ok', false)
            ->assertJsonPath('error.code', 'auth_required');
    }

    public function test_me_returns_user_for_valid_token(): void
    {
        $user = User::factory()->create([
            'email' => 'movil@ediprofe.com',
            'password' => 'abc123456',
        ]);

        $plainToken = 'ep_test_token_123';

        ApiToken::query()->create([
            'user_id' => $user->id,
            'name' => 'android-app',
            'token_hash' => hash('sha256', $plainToken),
            'expires_at' => now()->addDays(7),
            'last_used_at' => null,
            'revoked_at' => null,
            'metadata' => [],
        ]);

        $response = $this->withHeaders([
            'Authorization' => 'Bearer '.$plainToken,
        ])->getJson('/api/v1/auth/me');

        $response
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.user.id', $user->id)
            ->assertJsonPath('data.session.device_name', 'android-app');
    }

    public function test_logout_revokes_current_token(): void
    {
        $user = User::factory()->create();
        $plainToken = 'ep_logout_token_123';

        $apiToken = ApiToken::query()->create([
            'user_id' => $user->id,
            'name' => 'android-app',
            'token_hash' => hash('sha256', $plainToken),
            'expires_at' => now()->addDays(7),
            'last_used_at' => null,
            'revoked_at' => null,
            'metadata' => [],
        ]);

        $response = $this->withHeaders([
            'Authorization' => 'Bearer '.$plainToken,
        ])->postJson('/api/v1/auth/logout');

        $response
            ->assertOk()
            ->assertJsonPath('ok', true);

        $apiToken->refresh();
        $this->assertNotNull($apiToken->revoked_at);
    }
}
