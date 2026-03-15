<?php

namespace Tests\Feature;

use Illuminate\Support\Facades\File;
use Symfony\Component\Process\Process;
use Tests\TestCase;

class WorkshopManifestExportAstTest extends TestCase
{
    public function test_manifest_export_builds_blocks_from_real_markdown_ast(): void
    {
        $repoRoot = dirname(dirname(base_path()));
        $fixtureDir = $repoRoot.'/src/content/saber/codex-ast-fixtures/ast-export';
        $fixturePath = $fixtureDir.'/taller.mdx';
        $manifestPath = storage_path('app/testing-workshops-manifest-ast.json');

        File::ensureDirectoryExists($fixtureDir);

        File::put($fixturePath, <<<'MDX'
---
title: Taller AST export
---

# Taller AST export

## 1.
<Pregunta id="S1-1">

Con base en la siguiente tabla:

| **Temperatura de ebullición (°C)** | Altura |
| --- | --- |
| 100,0 | 0 |
| 98,5 | 457 |

$$A = p^+ + n$$

![Modelo](/images/simulacros/quimica/curva-solubilidad-azucar-agua.svg)

<Opciones>
  <Opcion letra="A">**A** = p^+ + n</Opcion>
  <Opcion letra="B" correcta>Opción correcta</Opcion>
</Opciones>

<Respuesta summary="Solución">

**Respuesta: B**

La fórmula se expresa como $A = p^+ + n$.

</Respuesta>

</Pregunta>
MDX);

        try {
            $process = new Process([
                'node',
                'scripts/export-workshops-manifest.mjs',
                '--output',
                $manifestPath,
            ], $repoRoot);

            $process->setTimeout(180);
            $process->mustRun();

            $manifest = json_decode(File::get($manifestPath), true, 512, JSON_THROW_ON_ERROR);
            $workshops = collect($manifest['workshops'] ?? []);
            $entry = $workshops->firstWhere('route', '/saber/codex-ast-fixtures/ast-export/taller');

            $this->assertIsArray($entry);
            $question = $entry['questions'][0] ?? null;
            $this->assertIsArray($question);

            $stemBlocks = is_array($question['stem_blocks'] ?? null) ? $question['stem_blocks'] : [];
            $stemNodes = is_array($question['stem_nodes'] ?? null) ? $question['stem_nodes'] : [];
            $this->assertTrue(collect($stemBlocks)->contains(fn (array $block): bool => ($block['type'] ?? null) === 'table'));
            $this->assertTrue(collect($stemBlocks)->contains(fn (array $block): bool => ($block['type'] ?? null) === 'equation'));
            $this->assertTrue(collect($stemBlocks)->contains(fn (array $block): bool => ($block['type'] ?? null) === 'image'));
            $this->assertSame($stemBlocks, $stemNodes);

            $tableBlock = collect($stemBlocks)->first(fn (array $block): bool => ($block['type'] ?? null) === 'table');
            $this->assertSame('Temperatura de ebullición (°C)', $tableBlock['rows'][0][0] ?? null);
            $this->assertSame('100,0', $tableBlock['rows'][1][0] ?? null);

            $this->assertSame('A', $question['options'][0]['id'] ?? null);
            $this->assertStringContainsString('<strong>A</strong>', (string) ($question['options'][0]['text_html'] ?? ''));
            $this->assertSame('paragraph', $question['options'][0]['nodes_mobile'][0]['type'] ?? null);
            $this->assertSame('B', $question['correct_option_id'] ?? null);
            $this->assertStringContainsString('Respuesta: B', (string) ($question['feedback_html'] ?? ''));
        } finally {
            File::delete($fixturePath);
            File::delete($manifestPath);

            if (File::isDirectory($fixtureDir) && count(File::files($fixtureDir)) === 0) {
                File::deleteDirectory($fixtureDir);
            }

            $fixtureParent = dirname($fixtureDir);
            if (File::isDirectory($fixtureParent) && count(File::files($fixtureParent)) === 0 && count(File::directories($fixtureParent)) === 0) {
                File::deleteDirectory($fixtureParent);
            }
        }
    }
}
