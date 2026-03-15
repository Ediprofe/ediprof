<x-filament-panels::page>
    @php($summary = $this->previewSummary())
    @php($reviewNotes = $this->reviewNotes())
    @php($questionRows = $this->questionReviewRows())

    <div class="space-y-6">
        <x-filament::section heading="Flujo recomendado" description="La idea aquí es simple: pegar un bloque contextual, ubicarlo en el banco y validar la vista real. Filament no intenta ser el renderer final.">
            <div class="mb-4 flex flex-wrap items-center gap-3">
                <x-filament::button
                    tag="a"
                    :href="$this->subjectAdminUrl()"
                    color="gray"
                    icon="heroicon-o-book-open"
                >
                    Materias
                </x-filament::button>
                <x-filament::button
                    tag="a"
                    :href="$this->unitAdminUrl()"
                    color="gray"
                    icon="heroicon-o-squares-2x2"
                >
                    Unidades
                </x-filament::button>
                <x-filament::button
                    tag="a"
                    :href="$this->originAdminUrl()"
                    color="gray"
                    icon="heroicon-o-folder"
                >
                    Orígenes
                </x-filament::button>
                <p class="text-sm text-gray-500 dark:text-gray-400">
                    Desde ahí defines y renombras la organización real del banco, sin volver al texto libre.
                </p>
            </div>
            <div class="grid gap-4 md:grid-cols-3">
                <div class="rounded-xl border border-gray-200 bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Paso 1</p>
                    <p class="mt-2 text-sm font-semibold text-gray-950 dark:text-white">Pega un bloque contextual</p>
                    <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">Aquí necesitamos contexto + pregunta(s), no ítems aislados.</p>
                </div>
                <div class="rounded-xl border border-gray-200 bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Paso 2</p>
                    <p class="mt-2 text-sm font-semibold text-gray-950 dark:text-white">Confirma si Laravel entendió el bloque</p>
                    <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">Revisamos estructura, contexto, correcta y organización mínima del banco.</p>
                </div>
                <div class="rounded-xl border border-gray-200 bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Paso 3</p>
                    <p class="mt-2 text-sm font-semibold text-gray-950 dark:text-white">Guarda el bloque y revisa la vista real</p>
                    <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">La apariencia final siempre la validamos en el renderer web real, no dentro de Filament.</p>
                </div>
            </div>
        </x-filament::section>

        <form wire:submit="convertDraft" class="space-y-6">
            {{ $this->form }}

            <div class="flex flex-wrap items-center gap-3">
                <x-filament::button type="submit" icon="heroicon-o-sparkles">
                    Convertir y revisar bloque
                </x-filament::button>

                @if ($summary)
                    <x-filament::button type="button" color="success" icon="heroicon-o-arrow-down-tray" wire:click="saveDraftAndOpenPreview">
                        Guardar bloque y abrir preview web
                    </x-filament::button>
                @endif

                @if (filled($savedPreviewUrl))
                    <x-filament::button tag="a" :href="$savedPreviewUrl" target="_blank" color="gray" icon="heroicon-o-globe-alt">
                        Abrir preview de nuevo
                    </x-filament::button>
                @endif

                <p class="text-sm text-gray-500 dark:text-gray-400">
                    Aquí solo tomamos decisiones de estructura y organización editorial. La parte visual se juzga en la vista real.
                </p>
            </div>
        </form>

        @if (filled($parserError))
            <x-filament::section>
                <div class="rounded-xl border border-danger-300/70 bg-danger-50 p-4 text-sm text-danger-700 dark:border-danger-500/40 dark:bg-danger-950/40 dark:text-danger-200">
                    {{ $parserError }}
                </div>
            </x-filament::section>
        @endif

        @if ($summary)
            <x-filament::section heading="Lo que Laravel entendió" description="Esto sí debería ayudarte a decidir si el borrador quedó bien separado antes de guardarlo.">
                    <div class="grid gap-4 md:grid-cols-3">
                        <div class="rounded-xl border border-gray-200 bg-gray-50 p-4 dark:border-gray-700 dark:bg-gray-900">
                            <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Contextos</p>
                        <p class="mt-2 text-3xl font-semibold text-gray-950 dark:text-white">{{ $summary['contexts'] }}</p>
                    </div>
                    <div class="rounded-xl border border-gray-200 bg-gray-50 p-4 dark:border-gray-700 dark:bg-gray-900">
                        <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Preguntas</p>
                        <p class="mt-2 text-3xl font-semibold text-gray-950 dark:text-white">{{ $summary['questions'] }}</p>
                    </div>
                        <div class="rounded-xl border border-gray-200 bg-gray-50 p-4 dark:border-gray-700 dark:bg-gray-900">
                            <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Enlaces contexto/pregunta</p>
                            <p class="mt-2 text-3xl font-semibold text-gray-950 dark:text-white">{{ $summary['links'] }}</p>
                        </div>
                    </div>
                    <div class="mt-4 flex flex-wrap gap-2">
                        @if (filled(data_get($preview, 'organization.subject_label')))
                            <span class="rounded-full bg-primary-50 px-3 py-1 text-xs font-semibold text-primary-700 dark:bg-primary-500/15 dark:text-primary-200">
                                Materia · {{ data_get($preview, 'organization.subject_label') }}
                            </span>
                        @endif
                        @if (filled(data_get($preview, 'organization.unit_label')))
                            <span class="rounded-full bg-gray-100 px-3 py-1 text-xs font-semibold text-gray-700 dark:bg-gray-800 dark:text-gray-200">
                                Unidad · {{ data_get($preview, 'organization.unit_label') }}
                            </span>
                        @endif
                        @if (filled(data_get($preview, 'organization.origin_type')) || filled(data_get($preview, 'organization.origin_label')))
                            <span class="rounded-full bg-warning-50 px-3 py-1 text-xs font-semibold text-warning-700 dark:bg-warning-500/15 dark:text-warning-200">
                                Origen · {{ data_get($preview, 'organization.origin_type') ?: 'sin tipo' }}{{ filled(data_get($preview, 'organization.origin_label')) ? ' · '.data_get($preview, 'organization.origin_label') : '' }}
                            </span>
                        @endif
                    </div>
            </x-filament::section>

            @if ($reviewNotes !== [])
                <x-filament::section heading="Lectura rápida" description="Este bloque sí está pensado para ayudarte a decidir el siguiente paso sin leer cosas técnicas.">
                    <div class="space-y-3">
                        @foreach ($reviewNotes as $note)
                            <div class="rounded-xl border border-primary-200 bg-primary-50/70 px-4 py-3 text-sm text-primary-800 dark:border-primary-500/30 dark:bg-primary-500/10 dark:text-primary-100">
                                {{ $note }}
                            </div>
                        @endforeach
                    </div>
                </x-filament::section>
            @endif

            @php($signals = $this->detectedSignals())
            @if ($signals !== [])
                <x-filament::section heading="Checklist de validación" description="Antes de guardar, aquí confirmamos que Laravel entendió la estructura útil del borrador.">
                    <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
                        @foreach ($signals as $signal)
                            <div class="rounded-xl border border-gray-200 bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
                                <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">{{ $signal['label'] }}</p>
                                <p class="mt-2 text-2xl font-semibold text-gray-950 dark:text-white">{{ $signal['value'] }}</p>
                            </div>
                        @endforeach
                    </div>
                </x-filament::section>
            @endif

            <x-filament::section heading="Control rápido por pregunta" description="Aquí verificamos si cada pregunta quedó lista dentro del bloque: correcta, opciones y contexto asociado.">
                <div class="space-y-5">
                    @if (count($preview['contexts'] ?? []) > 0)
                        <div class="rounded-2xl border border-gray-200 bg-white p-5 dark:border-gray-700 dark:bg-gray-900">
                            <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Contextos compartidos</p>
                            <div class="mt-3 flex flex-wrap gap-2">
                                @foreach (($preview['contexts'] ?? []) as $context)
                                    <span class="rounded-full bg-primary-50 px-3 py-1 text-xs font-semibold text-primary-700 dark:bg-primary-500/15 dark:text-primary-200">
                                        {{ $context['external_id'] ?? 'sin-id' }} · {{ $context['title'] ?? 'Sin título' }}
                                    </span>
                                @endforeach
                            </div>
                        </div>
                    @endif

                    <div class="overflow-hidden rounded-2xl border border-gray-200 bg-white dark:border-gray-700 dark:bg-gray-900">
                        <div class="grid grid-cols-[minmax(0,1.2fr)_auto_auto_minmax(0,1.4fr)] gap-3 border-b border-gray-200 px-4 py-3 text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:border-gray-700 dark:text-gray-400">
                            <span>Pregunta</span>
                            <span>Correcta</span>
                            <span>Opciones</span>
                            <span>Contexto(s)</span>
                        </div>
                        @foreach ($questionRows as $row)
                            <div class="grid grid-cols-[minmax(0,1.2fr)_auto_auto_minmax(0,1.4fr)] gap-3 border-b border-gray-100 px-4 py-4 text-sm text-gray-700 last:border-b-0 dark:border-gray-800 dark:text-gray-200">
                                <div>
                                    <p class="font-semibold text-gray-950 dark:text-white">{{ $row['id'] }}</p>
                                    <p class="text-xs text-gray-500 dark:text-gray-400">Orden {{ $row['order'] }}</p>
                                </div>
                                <span class="inline-flex items-center rounded-full bg-emerald-50 px-3 py-1 text-xs font-semibold text-emerald-700 dark:bg-emerald-500/15 dark:text-emerald-200">
                                    {{ $row['correct'] }}
                                </span>
                                <span class="inline-flex items-center rounded-full bg-gray-100 px-3 py-1 text-xs font-semibold text-gray-700 dark:bg-gray-800 dark:text-gray-200">
                                    {{ $row['options'] }}
                                </span>
                                <div class="flex flex-wrap gap-2">
                                    @forelse ($row['contexts'] as $contextId)
                                        <span class="rounded-full bg-warning-50 px-3 py-1 text-xs font-semibold text-warning-700 dark:bg-warning-500/15 dark:text-warning-200">
                                            {{ $contextId }}
                                        </span>
                                    @empty
                                        <span class="text-xs text-danger-600 dark:text-danger-300">Sin contexto vinculado</span>
                                    @endforelse
                                </div>
                            </div>
                        @endforeach
                    </div>
                </div>
            </x-filament::section>
        @endif
    </div>

    <x-filament-actions::modals />
</x-filament-panels::page>
