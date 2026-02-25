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
        Schema::create('content_catalog', function (Blueprint $table): void {
            $table->id();
            $table->string('external_id')->unique();
            $table->string('collection')->index();
            $table->string('title');
            $table->text('description')->nullable();
            $table->string('route')->unique();
            $table->string('site_url')->nullable();
            $table->string('content_type')->index();
            $table->string('access_tier')->index();
            $table->string('area_slug')->nullable()->index();
            $table->string('unidad_slug')->nullable()->index();
            $table->string('tema_slug')->nullable()->index();
            $table->integer('sort_order')->nullable()->index();
            $table->boolean('is_published')->default(false)->index();
            $table->json('metadata')->nullable();
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
        Schema::dropIfExists('content_catalog');
    }
};
