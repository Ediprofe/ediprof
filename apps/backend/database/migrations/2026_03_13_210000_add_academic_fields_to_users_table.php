<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('users', function (Blueprint $table) {
            $table->string('first_names')->nullable()->after('name')->index();
            $table->string('last_names')->nullable()->after('first_names')->index();
            $table->string('institutional_code')->nullable()->after('email')->index();
            $table->string('document_number')->nullable()->after('institutional_code')->index();
            $table->string('grade_group')->nullable()->after('document_number')->index();
        });

        DB::table('users')
            ->select(['id', 'name'])
            ->orderBy('id')
            ->chunkById(200, function ($users): void {
                foreach ($users as $user) {
                    $name = trim((string) $user->name);

                    if ($name === '') {
                        continue;
                    }

                    $firstNames = $name;
                    $lastNames = null;

                    if (str_contains($name, ',')) {
                        [$lastNames, $firstNames] = array_pad(
                            array_map('trim', explode(',', $name, 2)),
                            2,
                            '',
                        );
                        $lastNames = $lastNames !== '' ? $lastNames : null;
                        $firstNames = $firstNames !== '' ? $firstNames : null;
                    }

                    DB::table('users')
                        ->where('id', $user->id)
                        ->update([
                            'first_names' => $firstNames,
                            'last_names' => $lastNames,
                        ]);
                }
            });
    }

    public function down(): void
    {
        Schema::table('users', function (Blueprint $table) {
            $table->dropIndex(['first_names']);
            $table->dropIndex(['last_names']);
            $table->dropIndex(['institutional_code']);
            $table->dropIndex(['document_number']);
            $table->dropIndex(['grade_group']);
            $table->dropColumn([
                'first_names',
                'last_names',
                'institutional_code',
                'document_number',
                'grade_group',
            ]);
        });
    }
};
