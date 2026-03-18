<x-filament-panels::page>
    @php($summary = $this->previewSummary())
    @php($reviewNotes = $this->reviewNotes())
    @php($questionRows = $this->questionReviewRows())

    <div class="space-y-6">
        <x-filament::section heading="Flujo recomendado" description="La idea aquí es simple: traer preguntas al banco, revisar qué entendió el sistema y guardar solo las que realmente entran nuevas.">
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
                    <p class="mt-2 text-sm font-semibold text-gray-950 dark:text-white">Pega tus preguntas</p>
                    <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">Puede venir desde IA, un simulacro, una foto convertida a texto o cualquier material que ya tengas listo.</p>
                </div>
                <div class="rounded-xl border border-gray-200 bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Paso 2</p>
                    <p class="mt-2 text-sm font-semibold text-gray-950 dark:text-white">Revisa qué entendió el sistema</p>
                    <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">Aquí verificas contexto, preguntas, correcta y si alguna ya existe o se parece mucho a otra del banco.</p>
                </div>
                <div class="rounded-xl border border-gray-200 bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Paso 3</p>
                    <p class="mt-2 text-sm font-semibold text-gray-950 dark:text-white">Guarda solo lo nuevo</p>
                    <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">Las repetidas exactas se omiten para mantener el banco limpio y reusable.</p>
                </div>
            </div>
        </x-filament::section>

        <form wire:submit="convertDraft" class="space-y-6">
            {{ $this->form }}

            <div class="flex flex-wrap items-center gap-3">
                <x-filament::button type="submit" icon="heroicon-o-sparkles">
                    Revisar preguntas antes de guardar
                </x-filament::button>

                @if ($summary)
                    <x-filament::button type="button" color="success" icon="heroicon-o-arrow-down-tray" wire:click="saveDraftAndOpenPreview">
                        Guardar preguntas nuevas y abrir preview web
                    </x-filament::button>
                @endif

                @if (filled($savedPreviewUrl))
                    <x-filament::button tag="a" :href="$savedPreviewUrl" target="_blank" color="gray" icon="heroicon-o-globe-alt">
                        Abrir preview de nuevo
                    </x-filament::button>
                @endif

                <p class="text-sm text-gray-500 dark:text-gray-400">
                    Aquí decides qué entra al banco y qué ya existe. La organización interna por bloques y contexto compartido la resuelve el sistema.
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
                        <div class="rounded-xl border border-gray-200 bg-emerald-50 p-4 dark:border-emerald-500/20 dark:bg-emerald-500/10">
                            <p class="text-xs font-semibold uppercase tracking-[0.18em] text-emerald-700 dark:text-emerald-200">Preguntas nuevas</p>
                            <p class="mt-2 text-3xl font-semibold text-emerald-800 dark:text-emerald-100">{{ $summary['new_questions'] }}</p>
                        </div>
                        <div class="rounded-xl border border-gray-200 bg-amber-50 p-4 dark:border-amber-500/20 dark:bg-amber-500/10">
                            <p class="text-xs font-semibold uppercase tracking-[0.18em] text-amber-700 dark:text-amber-200">Repetidas exactas</p>
                            <p class="mt-2 text-3xl font-semibold text-amber-800 dark:text-amber-100">{{ $summary['exact_duplicates'] }}</p>
                        </div>
                        <div class="rounded-xl border border-gray-200 bg-sky-50 p-4 dark:border-sky-500/20 dark:bg-sky-500/10">
                            <p class="text-xs font-semibold uppercase tracking-[0.18em] text-sky-700 dark:text-sky-200">Con parecidas sugeridas</p>
                            <p class="mt-2 text-3xl font-semibold text-sky-800 dark:text-sky-100">{{ $summary['similar_candidates'] }}</p>
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

            <x-filament::section heading="Revisión por pregunta" description="Aquí decides con claridad qué preguntas entrarán al banco, cuáles ya existen y cuáles conviene revisar por similitud.">
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

                    <div class="space-y-4">
                        @foreach ($questionRows as $row)
                            <div class="rounded-2xl border border-gray-200 bg-white p-5 dark:border-gray-700 dark:bg-gray-900">
                                <div class="flex flex-wrap items-start justify-between gap-3">
                                    <div class="space-y-3">
                                        <div class="flex flex-wrap gap-2">
                                            <span class="rounded-full bg-gray-100 px-3 py-1 text-xs font-semibold text-gray-700 dark:bg-gray-800 dark:text-gray-200">
                                                {{ $row['id'] }} · orden {{ $row['order'] }}
                                            </span>

                                            @if ($row['save_decision'] === 'skip_duplicate')
                                                <span class="rounded-full bg-amber-50 px-3 py-1 text-xs font-semibold text-amber-700 dark:bg-amber-500/15 dark:text-amber-200">
                                                    Ya existe · se omitirá al guardar
                                                </span>
                                            @else
                                                <span class="rounded-full bg-emerald-50 px-3 py-1 text-xs font-semibold text-emerald-700 dark:bg-emerald-500/15 dark:text-emerald-200">
                                                    Nueva · se guardará en el banco
                                                </span>
                                            @endif

                                            @if ($row['duplicate_status'] === 'similar_candidates')
                                                <span class="rounded-full bg-sky-50 px-3 py-1 text-xs font-semibold text-sky-700 dark:bg-sky-500/15 dark:text-sky-200">
                                                    Revisa parecidas sugeridas
                                                </span>
                                            @endif
                                        </div>

                                        <p class="text-base font-semibold leading-7 text-gray-950 dark:text-white">
                                            {{ $row['stem_excerpt'] }}
                                        </p>

                                        <div class="flex flex-wrap gap-2 text-xs">
                                            <span class="rounded-full bg-emerald-50 px-3 py-1 font-semibold text-emerald-700 dark:bg-emerald-500/15 dark:text-emerald-200">
                                                Correcta · {{ $row['correct'] }}
                                            </span>
                                            <span class="rounded-full bg-gray-100 px-3 py-1 font-semibold text-gray-700 dark:bg-gray-800 dark:text-gray-200">
                                                {{ $row['options'] }} opción(es)
                                            </span>
                                            @forelse ($row['contexts'] as $contextId)
                                                <span class="rounded-full bg-warning-50 px-3 py-1 font-semibold text-warning-700 dark:bg-warning-500/15 dark:text-warning-200">
                                                    {{ $contextId }}
                                                </span>
                                            @empty
                                                <span class="rounded-full bg-danger-50 px-3 py-1 font-semibold text-danger-700 dark:bg-danger-500/15 dark:text-danger-200">
                                                    Sin contexto vinculado
                                                </span>
                                            @endforelse
                                        </div>
                                    </div>
                                </div>

                                @if ($row['exact_match'])
                                    <div class="mt-4 rounded-xl border border-amber-200 bg-amber-50 p-4 dark:border-amber-500/20 dark:bg-amber-500/10">
                                        <p class="text-sm font-semibold text-amber-900 dark:text-amber-100">
                                            Esta pregunta ya existe en el banco
                                        </p>
                                        <p class="mt-2 text-sm text-amber-800 dark:text-amber-200">
                                            {{ $row['exact_match']['stem_excerpt'] }}
                                        </p>
                                        <div class="mt-3 flex flex-wrap gap-2">
                                            @if (filled($row['exact_match']['block_title']))
                                                <span class="rounded-full bg-white/80 px-3 py-1 text-xs font-semibold text-amber-900 dark:bg-gray-900/60 dark:text-amber-100">
                                                    Bloque · {{ $row['exact_match']['block_title'] }}
                                                </span>
                                            @endif
                                            @if (filled($row['exact_match']['subject_label']))
                                                <span class="rounded-full bg-white/80 px-3 py-1 text-xs font-semibold text-amber-900 dark:bg-gray-900/60 dark:text-amber-100">
                                                    Materia · {{ $row['exact_match']['subject_label'] }}
                                                </span>
                                            @endif
                                            @if (filled($row['exact_match']['unit_label']))
                                                <span class="rounded-full bg-white/80 px-3 py-1 text-xs font-semibold text-amber-900 dark:bg-gray-900/60 dark:text-amber-100">
                                                    Unidad · {{ $row['exact_match']['unit_label'] }}
                                                </span>
                                            @endif
                                            @if (filled($row['exact_match']['origin_label']))
                                                <span class="rounded-full bg-white/80 px-3 py-1 text-xs font-semibold text-amber-900 dark:bg-gray-900/60 dark:text-amber-100">
                                                    Origen · {{ $row['exact_match']['origin_label'] }}
                                                </span>
                                            @endif
                                        </div>
                                        <div class="mt-3">
                                            <x-filament::button tag="a" :href="$row['exact_match']['edit_url']" color="gray" size="sm" icon="heroicon-o-arrow-top-right-on-square">
                                                Revisar pregunta existente
                                            </x-filament::button>
                                        </div>
                                    </div>
                                @endif

                                @if (count($row['similar_candidates']) > 0)
                                    <div class="mt-4 rounded-xl border border-sky-200 bg-sky-50 p-4 dark:border-sky-500/20 dark:bg-sky-500/10">
                                        <p class="text-sm font-semibold text-sky-900 dark:text-sky-100">
                                            Preguntas parecidas sugeridas
                                        </p>
                                        <div class="mt-3 space-y-3">
                                            @foreach ($row['similar_candidates'] as $candidate)
                                                <div class="rounded-lg border border-white/70 bg-white/80 p-3 dark:border-gray-800 dark:bg-gray-900/60">
                                                    <div class="flex flex-wrap items-center justify-between gap-3">
                                                        <p class="text-sm text-gray-900 dark:text-white">{{ $candidate['stem_excerpt'] }}</p>
                                                        <span class="rounded-full bg-sky-100 px-3 py-1 text-xs font-semibold text-sky-800 dark:bg-sky-500/20 dark:text-sky-100">
                                                            Similitud {{ number_format((float) $candidate['similarity'] * 100, 0) }}%
                                                        </span>
                                                    </div>
                                                    <div class="mt-2 flex flex-wrap gap-2">
                                                        @if (filled($candidate['block_title']))
                                                            <span class="rounded-full bg-gray-100 px-3 py-1 text-xs font-semibold text-gray-700 dark:bg-gray-800 dark:text-gray-200">
                                                                Bloque · {{ $candidate['block_title'] }}
                                                            </span>
                                                        @endif
                                                        @if (filled($candidate['unit_label']))
                                                            <span class="rounded-full bg-gray-100 px-3 py-1 text-xs font-semibold text-gray-700 dark:bg-gray-800 dark:text-gray-200">
                                                                Unidad · {{ $candidate['unit_label'] }}
                                                            </span>
                                                        @endif
                                                    </div>
                                                    <div class="mt-3">
                                                        <x-filament::button tag="a" :href="$candidate['edit_url']" color="gray" size="sm" icon="heroicon-o-arrow-top-right-on-square">
                                                            Revisar parecida
                                                        </x-filament::button>
                                                    </div>
                                                </div>
                                            @endforeach
                                        </div>
                                    </div>
                                @endif
                            </div>
                        @endforeach
                    </div>
                </div>
            </x-filament::section>
        @endif
    </div>

    <x-filament-actions::modals />
</x-filament-panels::page>
