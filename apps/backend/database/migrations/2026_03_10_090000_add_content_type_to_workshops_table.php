<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('workshops', function (Blueprint $table): void {
            $table->string('content_type')->default('taller')->after('content_external_id')->index();
        });

        DB::table('workshops')
            ->whereNull('content_type')
            ->update(['content_type' => 'taller']);
    }

    public function down(): void
    {
        Schema::table('workshops', function (Blueprint $table): void {
            $table->dropIndex(['content_type']);
            $table->dropColumn('content_type');
        });
    }
};
