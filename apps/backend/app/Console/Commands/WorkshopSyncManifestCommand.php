<?php

namespace App\Console\Commands;

use App\Services\Content\WorkshopManifestSyncService;
use Illuminate\Console\Command;
use Throwable;

class WorkshopSyncManifestCommand extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'workshops:sync-manifest
        {path=/tmp/ediprofe-workshops-manifest.json : Path to the workshops manifest JSON file}
        {--dry-run : Validate and summarize without writing database changes}
        {--prune-missing : Delete workshop rows not present in the manifest}';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Synchronize workshops table from a workshops manifest JSON.';

    /**
     * Execute the console command.
     */
    public function handle(WorkshopManifestSyncService $service): int
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

        $this->line('Workshop manifest synchronization summary');
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
