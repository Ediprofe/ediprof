<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('assessment_templates', function (Blueprint $table): void {
            $table->string('subject_label')->nullable()->after('title')->index();
            $table->string('unit_label')->nullable()->after('unidad_slug')->index();
            $table->string('origin_label')->nullable()->after('unit_label')->index();
            $table->string('editorial_status')->nullable()->after('origin_label')->index();
        });

        Schema::table('assessment_questions', function (Blueprint $table): void {
            $table->string('subject_label')->nullable()->after('source_slug')->index();
        });

        Schema::table('assessment_contexts', function (Blueprint $table): void {
            $table->string('subject_label')->nullable()->after('title')->index();
        });
    }

    public function down(): void
    {
        Schema::table('assessment_contexts', function (Blueprint $table): void {
            $table->dropColumn('subject_label');
        });

        Schema::table('assessment_questions', function (Blueprint $table): void {
            $table->dropColumn('subject_label');
        });

        Schema::table('assessment_templates', function (Blueprint $table): void {
            $table->dropColumn([
                'subject_label',
                'unit_label',
                'origin_label',
                'editorial_status',
            ]);
        });
    }
};
