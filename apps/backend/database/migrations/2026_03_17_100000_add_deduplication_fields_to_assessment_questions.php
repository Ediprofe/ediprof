<?php

use App\Services\Content\AssessmentQuestionFingerprintService;
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('assessment_questions', function (Blueprint $table): void {
            $table->string('exact_fingerprint', 64)->nullable()->after('app_payload_version')->index();
            $table->text('search_document')->nullable()->after('exact_fingerprint');
        });

        $fingerprintService = app(AssessmentQuestionFingerprintService::class);

        DB::table('assessment_questions')
            ->select(['id'])
            ->orderBy('id')
            ->chunkById(100, function ($rows) use ($fingerprintService): void {
                $ids = collect($rows)->pluck('id')->all();

                $questions = \App\Models\AssessmentQuestion::query()
                    ->whereIn('id', $ids)
                    ->get();

                foreach ($questions as $question) {
                    DB::table('assessment_questions')
                        ->where('id', $question->id)
                        ->update([
                            'exact_fingerprint' => $fingerprintService->exactFingerprintForQuestion($question),
                            'search_document' => $fingerprintService->searchDocumentForQuestion($question),
                        ]);
                }
            });
    }

    public function down(): void
    {
        Schema::table('assessment_questions', function (Blueprint $table): void {
            $table->dropColumn(['exact_fingerprint', 'search_document']);
        });
    }
};
