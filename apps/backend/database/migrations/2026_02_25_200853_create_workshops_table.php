<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('workshops', function (Blueprint $table): void {
            $table->id();
            $table->string('external_id')->unique();
            $table->string('content_external_id')->nullable()->index();
            $table->string('title');
            $table->string('route')->unique();
            $table->string('area_slug')->nullable()->index();
            $table->string('unidad_slug')->nullable()->index();
            $table->string('access_tier')->default('premium')->index();
            $table->boolean('is_published')->default(false)->index();
            $table->unsignedInteger('total_questions')->default(0);
            $table->unsignedInteger('total_assets')->default(0);
            $table->json('assets')->nullable();
            $table->json('questions');
            $table->json('metadata')->nullable();
            $table->timestamp('synced_at')->nullable()->index();
            $table->timestamps();

            $table->index(['area_slug', 'is_published']);
            $table->index(['access_tier', 'is_published']);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('workshops');
    }
};
