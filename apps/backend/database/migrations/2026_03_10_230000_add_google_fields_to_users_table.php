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
        Schema::table('users', function (Blueprint $table): void {
            $table->string('auth_provider')->nullable()->after('member_status')->index();
            $table->string('google_subject')->nullable()->after('auth_provider')->unique();
            $table->string('google_avatar_url')->nullable()->after('google_subject');
            $table->timestamp('last_login_at')->nullable()->after('google_avatar_url');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('users', function (Blueprint $table): void {
            $table->dropColumn([
                'auth_provider',
                'google_subject',
                'google_avatar_url',
                'last_login_at',
            ]);
        });
    }
};
