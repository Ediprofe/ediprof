<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('assessment_booklets', function (Blueprint $table): void {
            $table->id();
            $table->string('external_id')->unique();
            $table->string('title');
            $table->string('booklet_type')->default('simulacro')->index();
            $table->foreignId('origin_collection_id')->nullable()->constrained('assessment_origin_collections')->nullOnDelete();
            $table->string('origin_label')->nullable()->index();
            $table->date('applied_on')->nullable()->index();
            $table->string('school_year')->nullable()->index();
            $table->string('editorial_status')->default('draft')->index();
            $table->boolean('is_active')->default(true)->index();
            $table->unsignedInteger('total_sections')->default(0);
            $table->unsignedInteger('total_questions')->default(0);
            $table->longText('notes')->nullable();
            $table->json('metadata')->nullable();
            $table->timestamps();
        });

        Schema::create('assessment_booklet_sections', function (Blueprint $table): void {
            $table->id();
            $table->foreignId('booklet_id')->constrained('assessment_booklets')->cascadeOnDelete();
            $table->string('external_id');
            $table->string('title');
            $table->foreignId('subject_id')->constrained('assessment_subjects')->cascadeOnDelete();
            $table->string('subject_label')->nullable()->index();
            $table->foreignId('default_unit_id')->nullable()->constrained('assessment_units')->nullOnDelete();
            $table->string('default_unit_label')->nullable()->index();
            $table->foreignId('template_id')->nullable()->constrained('assessment_templates')->nullOnDelete();
            $table->unsignedInteger('order_base')->default(1);
            $table->unsignedInteger('total_questions')->default(0);
            $table->json('metadata')->nullable();
            $table->timestamps();

            $table->unique(['booklet_id', 'external_id']);
            $table->index(['booklet_id', 'order_base']);
        });

        Schema::create('assessment_booklet_questions', function (Blueprint $table): void {
            $table->id();
            $table->foreignId('booklet_id')->constrained('assessment_booklets')->cascadeOnDelete();
            $table->foreignId('booklet_section_id')->constrained('assessment_booklet_sections')->cascadeOnDelete();
            $table->foreignId('question_id')->constrained('assessment_questions')->cascadeOnDelete();
            $table->unsignedInteger('order_base')->default(1);
            $table->timestamps();

            $table->unique(['booklet_section_id', 'question_id']);
            $table->index(['booklet_id', 'order_base']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('assessment_booklet_questions');
        Schema::dropIfExists('assessment_booklet_sections');
        Schema::dropIfExists('assessment_booklets');
    }
};
