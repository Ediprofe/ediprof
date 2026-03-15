<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AdminPanelAccessTest extends TestCase
{
    use RefreshDatabase;

    public function test_guest_can_open_admin_login_page(): void
    {
        $this->get('/admin/login')
            ->assertOk();
    }

    public function test_student_session_is_cleared_before_admin_login_page_is_rendered(): void
    {
        $student = User::factory()->create([
            'email' => 'student-admin-panel@sanjoseitagui.edu.co',
            'role' => 'student',
            'member_status' => 'approved',
        ]);

        $this->actingAs($student, 'web');

        $this->get('/admin/login')
            ->assertOk();

        $this->assertGuest('web');
    }
}
