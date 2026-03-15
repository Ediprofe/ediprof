<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;
use Illuminate\Support\Str;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('assessment_subjects', function (Blueprint $table): void {
            $table->id();
            $table->string('label');
            $table->string('slug')->unique();
            $table->boolean('is_active')->default(true)->index();
            $table->timestamps();
        });

        Schema::create('assessment_units', function (Blueprint $table): void {
            $table->id();
            $table->foreignId('subject_id')->constrained('assessment_subjects')->cascadeOnDelete();
            $table->string('label');
            $table->string('slug');
            $table->boolean('is_active')->default(true)->index();
            $table->timestamps();

            $table->unique(['subject_id', 'slug']);
        });

        Schema::create('assessment_origin_collections', function (Blueprint $table): void {
            $table->id();
            $table->string('origin_type')->index();
            $table->string('label');
            $table->string('slug')->index();
            $table->boolean('is_active')->default(true)->index();
            $table->timestamps();

            $table->index(['origin_type', 'slug']);
        });

        Schema::table('assessment_templates', function (Blueprint $table): void {
            $table->foreignId('subject_id')->nullable()->after('title')->constrained('assessment_subjects')->nullOnDelete();
            $table->foreignId('unit_id')->nullable()->after('unidad_slug')->constrained('assessment_units')->nullOnDelete();
            $table->foreignId('origin_collection_id')->nullable()->after('origin_label')->constrained('assessment_origin_collections')->nullOnDelete();
        });

        Schema::table('assessment_questions', function (Blueprint $table): void {
            $table->foreignId('subject_id')->nullable()->after('source_slug')->constrained('assessment_subjects')->nullOnDelete();
            $table->foreignId('unit_id')->nullable()->after('unit_label')->constrained('assessment_units')->nullOnDelete();
            $table->foreignId('origin_collection_id')->nullable()->after('origin_label')->constrained('assessment_origin_collections')->nullOnDelete();
        });

        Schema::table('assessment_contexts', function (Blueprint $table): void {
            $table->foreignId('subject_id')->nullable()->after('title')->constrained('assessment_subjects')->nullOnDelete();
            $table->foreignId('unit_id')->nullable()->after('unit_label')->constrained('assessment_units')->nullOnDelete();
            $table->foreignId('origin_collection_id')->nullable()->after('origin_label')->constrained('assessment_origin_collections')->nullOnDelete();
        });

        $this->backfillBankStructure();

        if (Schema::hasTable('assessment_bank_taxonomies')) {
            Schema::drop('assessment_bank_taxonomies');
        }
    }

    public function down(): void
    {
        Schema::table('assessment_contexts', function (Blueprint $table): void {
            $table->dropConstrainedForeignId('origin_collection_id');
            $table->dropConstrainedForeignId('unit_id');
            $table->dropConstrainedForeignId('subject_id');
        });

        Schema::table('assessment_questions', function (Blueprint $table): void {
            $table->dropConstrainedForeignId('origin_collection_id');
            $table->dropConstrainedForeignId('unit_id');
            $table->dropConstrainedForeignId('subject_id');
        });

        Schema::table('assessment_templates', function (Blueprint $table): void {
            $table->dropConstrainedForeignId('origin_collection_id');
            $table->dropConstrainedForeignId('unit_id');
            $table->dropConstrainedForeignId('subject_id');
        });

        Schema::dropIfExists('assessment_origin_collections');
        Schema::dropIfExists('assessment_units');
        Schema::dropIfExists('assessment_subjects');
    }

    private function backfillBankStructure(): void
    {
        $subjectMap = [];

        foreach ($this->distinctLabels('subject_label') as $label) {
            $subjectId = DB::table('assessment_subjects')->insertGetId([
                'label' => $label,
                'slug' => Str::slug($label),
                'is_active' => true,
                'created_at' => now(),
                'updated_at' => now(),
            ]);

            $subjectMap[$label] = $subjectId;

            foreach (['assessment_templates', 'assessment_questions', 'assessment_contexts'] as $table) {
                DB::table($table)
                    ->where('subject_label', $label)
                    ->update([
                        'subject_id' => $subjectId,
                        'updated_at' => now(),
                    ]);
            }
        }

        $unitMap = [];

        foreach ($this->distinctSubjectUnits() as $pair) {
            $subjectId = $subjectMap[$pair['subject_label']] ?? null;

            if (! $subjectId) {
                continue;
            }

            $unitId = DB::table('assessment_units')->insertGetId([
                'subject_id' => $subjectId,
                'label' => $pair['unit_label'],
                'slug' => Str::slug($pair['unit_label']),
                'is_active' => true,
                'created_at' => now(),
                'updated_at' => now(),
            ]);

            $unitMap[$pair['subject_label'].'||'.$pair['unit_label']] = $unitId;

            foreach (['assessment_templates', 'assessment_questions', 'assessment_contexts'] as $table) {
                DB::table($table)
                    ->where('subject_label', $pair['subject_label'])
                    ->where('unit_label', $pair['unit_label'])
                    ->update([
                        'unit_id' => $unitId,
                        'updated_at' => now(),
                    ]);
            }
        }

        $collectionCache = [];

        $templates = DB::table('assessment_templates')
            ->select(['id', 'source_content_type', 'origin_label', 'subject_label', 'unit_label'])
            ->whereNotNull('origin_label')
            ->get();

        foreach ($templates as $template) {
            $originType = trim((string) $template->source_content_type);
            $originLabel = trim((string) $template->origin_label);

            if ($originType === '' || $originLabel === '') {
                continue;
            }

            $cacheKey = implode('||', [
                $originType,
                $originLabel,
            ]);

            if (! isset($collectionCache[$cacheKey])) {
                $collectionCache[$cacheKey] = DB::table('assessment_origin_collections')->insertGetId([
                    'origin_type' => $originType,
                    'label' => $originLabel,
                    'slug' => Str::slug($originLabel),
                    'is_active' => true,
                    'created_at' => now(),
                    'updated_at' => now(),
                ]);
            }

            DB::table('assessment_templates')
                ->where('id', $template->id)
                ->update([
                    'origin_collection_id' => $collectionCache[$cacheKey],
                    'updated_at' => now(),
                ]);
        }

        $templateRows = DB::table('assessment_templates')
            ->select(['id', 'subject_id', 'unit_id', 'origin_collection_id'])
            ->get()
            ->keyBy('id');

        foreach (['assessment_questions', 'assessment_contexts'] as $table) {
            $rows = DB::table($table)->select(['id', 'template_id'])->get();

            foreach ($rows as $row) {
                $template = $templateRows->get($row->template_id);

                if (! $template) {
                    continue;
                }

                DB::table($table)
                    ->where('id', $row->id)
                    ->update([
                        'subject_id' => $template->subject_id,
                        'unit_id' => $template->unit_id,
                        'origin_collection_id' => $template->origin_collection_id,
                        'updated_at' => now(),
                    ]);
            }
        }
    }

    /**
     * @return array<int, string>
     */
    private function distinctLabels(string $column): array
    {
        return collect(['assessment_templates', 'assessment_questions', 'assessment_contexts'])
            ->flatMap(fn (string $table) => DB::table($table)
                ->whereNotNull($column)
                ->where($column, '!=', '')
                ->distinct()
                ->pluck($column))
            ->map(fn ($value) => trim((string) $value))
            ->filter()
            ->unique()
            ->values()
            ->all();
    }

    /**
     * @return array<int, array{subject_label:string, unit_label:string}>
     */
    private function distinctSubjectUnits(): array
    {
        return collect(['assessment_templates', 'assessment_questions', 'assessment_contexts'])
            ->flatMap(function (string $table) {
                return DB::table($table)
                    ->select(['subject_label', 'unit_label'])
                    ->whereNotNull('subject_label')
                    ->where('subject_label', '!=', '')
                    ->whereNotNull('unit_label')
                    ->where('unit_label', '!=', '')
                    ->distinct()
                    ->get();
            })
            ->map(fn ($row) => [
                'subject_label' => trim((string) $row->subject_label),
                'unit_label' => trim((string) $row->unit_label),
            ])
            ->filter(fn (array $pair) => $pair['subject_label'] !== '' && $pair['unit_label'] !== '')
            ->unique(fn (array $pair) => $pair['subject_label'].'||'.$pair['unit_label'])
            ->values()
            ->all();
    }
};
