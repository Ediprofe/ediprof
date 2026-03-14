<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('assessment_questions', function (Blueprint $table): void {
            $table->string('topic')->nullable()->after('source_slug')->index();
            $table->string('unit_label')->nullable()->after('topic')->index();
            $table->string('subtopic')->nullable()->after('unit_label')->index();
            $table->string('origin_label')->nullable()->after('subtopic')->index();
            $table->string('editorial_status')->nullable()->after('origin_label')->index();
            $table->json('tags')->nullable()->after('editorial_status');
            $table->longText('teacher_notes')->nullable()->after('tags');
        });

        Schema::table('assessment_contexts', function (Blueprint $table): void {
            $table->string('topic')->nullable()->after('title')->index();
            $table->string('unit_label')->nullable()->after('topic')->index();
            $table->string('subtopic')->nullable()->after('unit_label')->index();
            $table->string('origin_label')->nullable()->after('subtopic')->index();
            $table->string('editorial_status')->nullable()->after('origin_label')->index();
            $table->json('tags')->nullable()->after('editorial_status');
            $table->longText('teacher_notes')->nullable()->after('tags');
        });

        Schema::table('assessment_assignment_questions', function (Blueprint $table): void {
            $table->string('selection_group_key')->nullable()->after('question_id')->index();
        });
    }

    public function down(): void
    {
        Schema::table('assessment_assignment_questions', function (Blueprint $table): void {
            $table->dropColumn('selection_group_key');
        });

        Schema::table('assessment_contexts', function (Blueprint $table): void {
            $table->dropColumn([
                'topic',
                'unit_label',
                'subtopic',
                'origin_label',
                'editorial_status',
                'tags',
                'teacher_notes',
            ]);
        });

        Schema::table('assessment_questions', function (Blueprint $table): void {
            $table->dropColumn([
                'topic',
                'unit_label',
                'subtopic',
                'origin_label',
                'editorial_status',
                'tags',
                'teacher_notes',
            ]);
        });
    }
};
