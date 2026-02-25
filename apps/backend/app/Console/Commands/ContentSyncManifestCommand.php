<?php

namespace App\Console\Commands;

use App\Services\Content\ContentManifestSyncService;
use Illuminate\Console\Command;
use Throwable;

class ContentSyncManifestCommand extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'content:sync-manifest
        {path=/tmp/ediprofe-content-manifest.json : Path to the manifest JSON file}
        {--dry-run : Validate and summarize without writing database changes}
        {--prune-missing : Delete catalog rows not present in the manifest}';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Synchronize content_catalog from a content manifest JSON.';

    /**
     * Execute the console command.
     */
    public function handle(ContentManifestSyncService $service): int
    {
        $path = (string) $this->argument('path');
        $dryRun = (bool) $this->option('dry-run');
        $pruneMissing = (bool) $this->option('prune-missing');

        try {
            $result = $service->sync($path, $dryRun, $pruneMissing);
        } catch (Throwable $exception) {
            $this->error($exception->getMessage());

            return self::FAILURE;
        }

        $this->line('Content manifest synchronization summary');
        $this->table(
            ['Metric', 'Value'],
            [
                ['Path', $result['path']],
                ['Dry run', $result['dry_run'] ? 'yes' : 'no'],
                ['Total processed', (string) $result['total']],
                ['Created', (string) $result['created']],
                ['Updated', (string) $result['updated']],
                ['Deleted', (string) $result['deleted']],
                ['Skipped', (string) $result['skipped']],
                ['Duplicates in manifest', (string) $result['duplicates']],
            ]
        );

        if ($dryRun) {
            $this->comment('Dry run mode: no database changes were applied.');
        }

        return self::SUCCESS;
    }
}
