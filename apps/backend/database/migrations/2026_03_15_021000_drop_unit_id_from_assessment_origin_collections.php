<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        if (! Schema::hasTable('assessment_origin_collections') || ! Schema::hasColumn('assessment_origin_collections', 'unit_id')) {
            return;
        }

        if (Schema::hasIndex('assessment_origin_collections', 'assessment_origin_collections_origin_type_subject_id_unit_id_index')) {
            Schema::table('assessment_origin_collections', function (Blueprint $table): void {
                $table->dropIndex('assessment_origin_collections_origin_type_subject_id_unit_id_index');
            });
        }

        Schema::table('assessment_origin_collections', function (Blueprint $table): void {
            $table->dropConstrainedForeignId('unit_id');
        });
    }

    public function down(): void
    {
        if (! Schema::hasTable('assessment_origin_collections') || Schema::hasColumn('assessment_origin_collections', 'unit_id')) {
            return;
        }

        Schema::table('assessment_origin_collections', function (Blueprint $table): void {
            $table->foreignId('unit_id')
                ->nullable()
                ->after('subject_id')
                ->constrained('assessment_units')
                ->nullOnDelete();

            $table->index(['origin_type', 'subject_id', 'unit_id']);
        });
    }
};
