<?php

namespace Tests\Feature;

use App\Filament\Pages\ImportAssessmentBooklet;
use App\Filament\Resources\AssessmentBlocks\AssessmentBlockResource;
use App\Filament\Resources\AssessmentBooklets\AssessmentBookletResource;
use App\Filament\Resources\AssessmentQuestions\AssessmentQuestionResource;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ImportAssessmentBookletPageTest extends TestCase
{
    use RefreshDatabase;

    public function test_admin_can_open_the_booklet_import_page(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        $this->actingAs($admin, 'web')
            ->get(ImportAssessmentBooklet::getUrl(panel: 'admin'))
            ->assertOk()
            ->assertSee('Importar cuadernillo');
    }

    public function test_admin_can_open_the_block_booklet_and_question_bank_lists(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        $this->actingAs($admin, 'web')
            ->get(AssessmentBlockResource::getUrl('index', panel: 'admin'))
            ->assertOk()
            ->assertSee('Bloques', false);

        $this->actingAs($admin, 'web')
            ->get(AssessmentBookletResource::getUrl('index', panel: 'admin'))
            ->assertOk()
            ->assertSee('Cuadernillos');

        $this->actingAs($admin, 'web')
            ->get(AssessmentQuestionResource::getUrl('index', panel: 'admin'))
            ->assertOk()
            ->assertSee('Preguntas', false);
    }
}
