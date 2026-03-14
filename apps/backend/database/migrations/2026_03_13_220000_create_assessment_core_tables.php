<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('assessment_templates', function (Blueprint $table): void {
            $table->id();
            $table->string('external_id')->unique();
            $table->foreignId('source_workshop_id')->nullable()->constrained('workshops')->nullOnDelete();
            $table->string('title');
            $table->string('source_content_type')->default('taller')->index();
            $table->string('default_mode')->default('study')->index();
            $table->string('route')->nullable()->index();
            $table->string('area_slug')->nullable()->index();
            $table->string('unidad_slug')->nullable()->index();
            $table->string('access_tier')->default('premium')->index();
            $table->boolean('is_published')->default(false)->index();
            $table->unsignedInteger('total_questions')->default(0);
            $table->unsignedInteger('total_assets')->default(0);
            $table->json('assets')->nullable();
            $table->json('asset_refs')->nullable();
            $table->json('metadata')->nullable();
            $table->timestamp('synced_at')->nullable()->index();
            $table->timestamps();
        });

        Schema::create('assessment_contexts', function (Blueprint $table): void {
            $table->id();
            $table->foreignId('template_id')->constrained('assessment_templates')->cascadeOnDelete();
            $table->string('external_id');
            $table->string('title')->nullable();
            $table->unsignedInteger('order_base')->default(1);
            $table->boolean('is_active')->default(true)->index();
            $table->longText('context_mdx')->nullable();
            $table->longText('context_html')->nullable();
            $table->json('context_assets')->nullable();
            $table->json('context_blocks')->nullable();
            $table->json('metadata')->nullable();
            $table->timestamps();

            $table->unique(['template_id', 'external_id']);
            $table->index(['template_id', 'order_base']);
        });

        Schema::create('assessment_questions', function (Blueprint $table): void {
            $table->id();
            $table->foreignId('template_id')->constrained('assessment_templates')->cascadeOnDelete();
            $table->string('external_id');
            $table->unsignedInteger('order_base')->default(1);
            $table->string('source_slug')->nullable()->index();
            $table->boolean('is_active')->default(true)->index();
            $table->json('meta')->nullable();
            $table->longText('stem_mdx')->nullable();
            $table->longText('stem_html')->nullable();
            $table->json('stem_assets')->nullable();
            $table->json('stem_blocks')->nullable();
            $table->json('options');
            $table->string('correct_option_id')->nullable();
            $table->longText('feedback_mdx')->nullable();
            $table->longText('feedback_html')->nullable();
            $table->string('feedback_summary')->nullable();
            $table->json('feedback_assets')->nullable();
            $table->json('feedback_blocks')->nullable();
            $table->longText('concepts_mdx')->nullable();
            $table->longText('concepts_html')->nullable();
            $table->string('concepts_summary')->nullable();
            $table->json('concepts_assets')->nullable();
            $table->json('concepts_blocks')->nullable();
            $table->unsignedInteger('app_payload_version')->nullable();
            $table->timestamps();

            $table->unique(['template_id', 'external_id']);
            $table->index(['template_id', 'order_base']);
        });

        Schema::create('assessment_question_contexts', function (Blueprint $table): void {
            $table->id();
            $table->foreignId('question_id')->constrained('assessment_questions')->cascadeOnDelete();
            $table->foreignId('context_id')->constrained('assessment_contexts')->cascadeOnDelete();
            $table->unsignedInteger('order_base')->default(1);
            $table->timestamps();

            $table->unique(['question_id', 'context_id']);
            $table->index(['question_id', 'order_base']);
        });

        Schema::create('assessment_assignments', function (Blueprint $table): void {
            $table->id();
            $table->string('external_id')->unique();
            $table->foreignId('course_id')->constrained()->cascadeOnDelete();
            $table->foreignId('template_id')->nullable()->constrained('assessment_templates')->nullOnDelete();
            $table->string('title');
            $table->string('mode')->default('simulacro')->index();
            $table->string('status')->default('draft')->index();
            $table->boolean('randomize_questions')->default(false);
            $table->boolean('show_feedback_on_submit')->default(true);
            $table->boolean('show_feedback_after_close')->default(false);
            $table->unsignedSmallInteger('max_attempts')->nullable();
            $table->unsignedInteger('time_limit_minutes')->nullable();
            $table->timestamp('opens_at')->nullable()->index();
            $table->timestamp('closes_at')->nullable()->index();
            $table->timestamp('review_released_at')->nullable()->index();
            $table->json('settings')->nullable();
            $table->timestamps();
        });

        Schema::create('assessment_assignment_questions', function (Blueprint $table): void {
            $table->id();
            $table->foreignId('assignment_id')->constrained('assessment_assignments')->cascadeOnDelete();
            $table->foreignId('question_id')->constrained('assessment_questions')->cascadeOnDelete();
            $table->unsignedInteger('order_base')->default(1);
            $table->timestamps();

            $table->unique(['assignment_id', 'question_id']);
            $table->index(['assignment_id', 'order_base']);
        });

        Schema::create('assessment_attempts', function (Blueprint $table): void {
            $table->id();
            $table->string('external_id')->unique();
            $table->foreignId('assignment_id')->nullable()->constrained('assessment_assignments')->nullOnDelete();
            $table->foreignId('template_id')->nullable()->constrained('assessment_templates')->nullOnDelete();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->string('mode')->default('study')->index();
            $table->string('status')->default('in_progress')->index();
            $table->json('question_order');
            $table->json('questions_snapshot');
            $table->unsignedInteger('total_questions')->default(0);
            $table->unsignedInteger('score_raw')->nullable();
            $table->unsignedSmallInteger('score_percent')->nullable();
            $table->decimal('score_scale', 6, 2)->nullable();
            $table->timestamp('started_at')->nullable()->index();
            $table->timestamp('submitted_at')->nullable()->index();
            $table->timestamp('graded_at')->nullable()->index();
            $table->timestamp('review_released_at')->nullable()->index();
            $table->timestamp('last_activity_at')->nullable()->index();
            $table->json('settings_snapshot')->nullable();
            $table->json('meta')->nullable();
            $table->timestamps();

            $table->index(['user_id', 'mode', 'status']);
        });

        Schema::create('assessment_attempt_answers', function (Blueprint $table): void {
            $table->id();
            $table->foreignId('attempt_id')->constrained('assessment_attempts')->cascadeOnDelete();
            $table->foreignId('question_id')->nullable()->constrained('assessment_questions')->nullOnDelete();
            $table->string('question_external_id');
            $table->unsignedInteger('position')->default(1);
            $table->string('selected_option_id')->nullable();
            $table->boolean('is_correct')->nullable();
            $table->timestamp('answered_at')->nullable()->index();
            $table->json('meta')->nullable();
            $table->timestamps();

            $table->unique(['attempt_id', 'question_external_id']);
            $table->index(['attempt_id', 'position']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('assessment_attempt_answers');
        Schema::dropIfExists('assessment_attempts');
        Schema::dropIfExists('assessment_assignment_questions');
        Schema::dropIfExists('assessment_assignments');
        Schema::dropIfExists('assessment_question_contexts');
        Schema::dropIfExists('assessment_questions');
        Schema::dropIfExists('assessment_contexts');
        Schema::dropIfExists('assessment_templates');
    }
};
