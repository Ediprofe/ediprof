<?php

namespace Tests\Feature;

use App\Models\AssessmentQuestion;
use App\Models\AssessmentQuestionOption;
use App\Models\AssessmentTemplate;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Inertia\Testing\AssertableInertia as Assert;
use Tests\TestCase;

class AssessmentDraftPreviewControllerTest extends TestCase
{
    use RefreshDatabase;

    public function test_admin_can_open_canonical_web_preview_for_a_draft_template(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        $template = AssessmentTemplate::query()->create([
            'external_id' => 'ai-draft-preview-test',
            'title' => 'Preview de prueba',
            'source_content_type' => 'ai_draft',
            'default_mode' => 'study',
            'access_tier' => 'private',
            'is_published' => false,
            'total_questions' => 1,
            'total_assets' => 0,
        ]);

        $question = AssessmentQuestion::query()->create([
            'template_id' => $template->id,
            'external_id' => '95',
            'order_base' => 1,
            'is_active' => true,
            'editorial_status' => 'draft',
            'stem_mdx' => '¿Cuál inferencia es válida?',
            'stem_html' => '<p>¿Cuál inferencia es válida?</p>',
            'options' => [],
            'correct_option_id' => 'B',
        ]);

        AssessmentQuestionOption::query()->create([
            'question_id' => $question->id,
            'option_id' => 'B',
            'order_base' => 2,
            'is_correct' => true,
            'plain_text' => 'La muestra M3 tiene más componentes.',
            'html_web' => '<p>La muestra <strong>M3</strong> tiene más componentes.</p>',
            'nodes_mobile' => [],
            'asset_refs' => [],
        ]);

        $this->actingAs($admin)
            ->get(route('admin.assessment_drafts.preview_web', $template))
            ->assertOk()
            ->assertInertia(fn (Assert $page) => $page
                ->component('Admin/AssessmentDrafts/Preview', false)
                ->where('draft.title', 'Preview de prueba')
                ->where('draft.questions.0.id', '95')
                ->where('draft.questions.0.options.0.id', 'B')
                ->where('draft.questions.0.options.0.text_html', '<p>La muestra <strong>M3</strong> tiene más componentes.</p>')
            );
    }
}
