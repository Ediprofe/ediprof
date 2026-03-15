<?php

namespace Tests\Feature;

use App\Filament\Resources\AssessmentBlocks\AssessmentBlockResource;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentSubject;
use App\Models\AssessmentTemplate;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AssessmentBlockEditPageTest extends TestCase
{
    use RefreshDatabase;

    public function test_block_edit_page_prioritizes_editorial_sections(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);
        $subject = AssessmentSubject::query()->create([
            'label' => 'Química',
            'is_active' => true,
        ]);
        $origin = AssessmentOriginCollection::query()->create([
            'origin_type' => 'simulacro',
            'label' => 'Simulacro editorial',
            'is_active' => true,
        ]);
        $template = AssessmentTemplate::query()->create([
            'external_id' => 'template-block-edit',
            'title' => 'Bloque editorial de prueba',
            'subject_id' => $subject->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'draft',
            'access_tier' => 'private',
            'is_published' => false,
            'total_questions' => 0,
            'total_assets' => 0,
        ]);

        $this->actingAs($admin, 'web')
            ->get(AssessmentBlockResource::getUrl('edit', ['record' => $template], panel: 'admin'))
            ->assertOk()
            ->assertSee('Identidad del bloque')
            ->assertSee('Clasificación editorial')
            ->assertSee('Información técnica del sistema');
    }
}
