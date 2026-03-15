<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        if (! Schema::hasTable('assessment_origin_collections') || ! Schema::hasColumn('assessment_origin_collections', 'subject_id')) {
            return;
        }

        foreach ([
            'assessment_origin_collections_origin_type_subject_id_index',
            'assessment_origin_collections_origin_type_subject_id_unit_id_index',
        ] as $indexName) {
            if (Schema::hasIndex('assessment_origin_collections', $indexName)) {
                Schema::table('assessment_origin_collections', function (Blueprint $table) use ($indexName): void {
                    $table->dropIndex($indexName);
                });
            }
        }

        Schema::table('assessment_origin_collections', function (Blueprint $table): void {
            $table->dropConstrainedForeignId('subject_id');
        });
    }

    public function down(): void
    {
        if (! Schema::hasTable('assessment_origin_collections') || Schema::hasColumn('assessment_origin_collections', 'subject_id')) {
            return;
        }

        Schema::table('assessment_origin_collections', function (Blueprint $table): void {
            $table->foreignId('subject_id')
                ->nullable()
                ->first()
                ->constrained('assessment_subjects')
                ->nullOnDelete();

            $table->index(['origin_type', 'subject_id']);
        });
    }
};
