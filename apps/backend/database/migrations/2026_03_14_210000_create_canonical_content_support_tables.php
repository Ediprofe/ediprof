<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('assessment_question_options', function (Blueprint $table): void {
            $table->id();
            $table->foreignId('question_id')->constrained('assessment_questions')->cascadeOnDelete();
            $table->string('option_id');
            $table->unsignedInteger('order_base')->default(1);
            $table->boolean('is_correct')->default(false)->index();
            $table->text('plain_text')->nullable();
            $table->longText('html_web')->nullable();
            $table->json('nodes_mobile')->nullable();
            $table->json('asset_refs')->nullable();
            $table->json('metadata')->nullable();
            $table->timestamps();

            $table->unique(['question_id', 'option_id']);
            $table->index(['question_id', 'order_base']);
        });

        Schema::create('content_assets', function (Blueprint $table): void {
            $table->id();
            $table->string('asset_key')->unique();
            $table->text('source_ref');
            $table->text('canonical_url');
            $table->string('asset_kind')->default('asset')->index();
            $table->string('mime_type')->nullable();
            $table->text('fallback_url')->nullable();
            $table->unsignedInteger('width')->nullable();
            $table->unsignedInteger('height')->nullable();
            $table->json('metadata')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('content_assets');
        Schema::dropIfExists('assessment_question_options');
    }
};
