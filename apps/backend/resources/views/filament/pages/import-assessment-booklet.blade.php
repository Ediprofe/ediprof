<x-filament-panels::page>
    @php($summary = $this->previewSummary())
    @php($reviewNotes = $this->reviewNotes())

    <div class="space-y-6">
        <x-filament::section heading="Flujo recomendado" description="La idea aquí es traer un cuadernillo al banco sin perder tiempo clasificando de más y sin volver a guardar preguntas repetidas exactas.">
            <div class="mb-4 flex flex-wrap items-center gap-3">
                <x-filament::button tag="a" :href="$this->subjectAdminUrl()" color="gray" icon="heroicon-o-book-open">
                    Materias
                </x-filament::button>
                <x-filament::button tag="a" :href="$this->unitAdminUrl()" color="gray" icon="heroicon-o-squares-2x2">
                    Unidades
                </x-filament::button>
                <x-filament::button tag="a" :href="$this->originAdminUrl()" color="gray" icon="heroicon-o-folder">
                    Orígenes
                </x-filament::button>
                <p class="text-sm text-gray-500 dark:text-gray-400">
                    El origen se selecciona una vez y cada sección hereda esa fuente sin repetirla en cada pregunta.
                </p>
            </div>
            <div class="grid gap-4 md:grid-cols-4">
                <div class="rounded-xl border border-gray-200 bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Paso 1</p>
                    <p class="mt-2 text-sm font-semibold text-gray-950 dark:text-white">Crear cuadernillo</p>
                    <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">Título, tipo, origen global y notas.</p>
                </div>
                <div class="rounded-xl border border-gray-200 bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Paso 2</p>
                    <p class="mt-2 text-sm font-semibold text-gray-950 dark:text-white">Dividir por materia</p>
                    <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">Cada bloque define la materia y pega sus preguntas.</p>
                </div>
                <div class="rounded-xl border border-gray-200 bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Paso 3</p>
                    <p class="mt-2 text-sm font-semibold text-gray-950 dark:text-white">Revisar estructura</p>
                    <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">Confirmamos cuántas preguntas son nuevas, cuáles ya existen y qué estructura detectó Laravel.</p>
                </div>
                <div class="rounded-xl border border-gray-200 bg-white p-4 dark:border-gray-700 dark:bg-gray-900">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Paso 4</p>
                    <p class="mt-2 text-sm font-semibold text-gray-950 dark:text-white">Guardar solo lo nuevo</p>
                    <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">Las repetidas exactas se omiten y la clasificación fina se puede terminar después.</p>
                </div>
            </div>
        </x-filament::section>

        <form wire:submit="convertDraft" class="space-y-6">
            {{ $this->form }}

            <div class="flex flex-wrap items-center gap-3">
                <x-filament::button type="submit" icon="heroicon-o-sparkles">
                    Convertir y revisar cuadernillo
                </x-filament::button>

                @if ($summary)
                    <x-filament::button type="button" color="success" icon="heroicon-o-arrow-down-tray" wire:click="saveBookletAndOpenEdit">
                        Guardar cuadernillo y omitir repetidas exactas
                    </x-filament::button>
                @endif

                <p class="text-sm text-gray-500 dark:text-gray-400">
                    Aquí confirmamos estructura, herencia por materia y qué preguntas realmente entrarán nuevas al banco.
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
            <x-filament::section heading="Resumen del cuadernillo" description="Esto te ayuda a validar rápido si la estructura quedó fiel al material original.">
                <div class="grid gap-4 md:grid-cols-3 xl:grid-cols-6">
                    <div class="rounded-xl border border-gray-200 bg-gray-50 p-4 dark:border-gray-700 dark:bg-gray-900">
                        <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Secciones</p>
                        <p class="mt-2 text-3xl font-semibold text-gray-950 dark:text-white">{{ $summary['sections'] }}</p>
                    </div>
                    <div class="rounded-xl border border-gray-200 bg-gray-50 p-4 dark:border-gray-700 dark:bg-gray-900">
                        <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Preguntas</p>
                        <p class="mt-2 text-3xl font-semibold text-gray-950 dark:text-white">{{ $summary['questions'] }}</p>
                    </div>
                    <div class="rounded-xl border border-gray-200 bg-gray-50 p-4 dark:border-gray-700 dark:bg-gray-900">
                        <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Contextos</p>
                        <p class="mt-2 text-3xl font-semibold text-gray-950 dark:text-white">{{ $summary['contexts'] }}</p>
                    </div>
                    <div class="rounded-xl border border-gray-200 bg-gray-50 p-4 dark:border-gray-700 dark:bg-gray-900">
                        <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Enlaces</p>
                        <p class="mt-2 text-3xl font-semibold text-gray-950 dark:text-white">{{ $summary['links'] }}</p>
                    </div>
                    <div class="rounded-xl border border-emerald-200 bg-emerald-50 p-4 dark:border-emerald-500/20 dark:bg-emerald-500/10">
                        <p class="text-xs font-semibold uppercase tracking-[0.18em] text-emerald-700 dark:text-emerald-200">Nuevas</p>
                        <p class="mt-2 text-3xl font-semibold text-emerald-800 dark:text-emerald-100">{{ $summary['new_questions'] ?? 0 }}</p>
                    </div>
                    <div class="rounded-xl border border-amber-200 bg-amber-50 p-4 dark:border-amber-500/20 dark:bg-amber-500/10">
                        <p class="text-xs font-semibold uppercase tracking-[0.18em] text-amber-700 dark:text-amber-200">Repetidas exactas</p>
                        <p class="mt-2 text-3xl font-semibold text-amber-800 dark:text-amber-100">{{ $summary['exact_duplicates'] ?? 0 }}</p>
                    </div>
                    <div class="rounded-xl border border-sky-200 bg-sky-50 p-4 dark:border-sky-500/20 dark:bg-sky-500/10">
                        <p class="text-xs font-semibold uppercase tracking-[0.18em] text-sky-700 dark:text-sky-200">Parecidas sugeridas</p>
                        <p class="mt-2 text-3xl font-semibold text-sky-800 dark:text-sky-100">{{ $summary['similar_candidates'] ?? 0 }}</p>
                    </div>
                </div>
            </x-filament::section>

            @if ($reviewNotes !== [])
                <x-filament::section heading="Lectura rápida" description="Estas notas te ayudan a decidir si ya puedes guardar o si conviene ajustar algún bloque primero.">
                    <div class="space-y-3">
                        @foreach ($reviewNotes as $note)
                            <div class="rounded-xl border border-primary-200 bg-primary-50/70 px-4 py-3 text-sm text-primary-800 dark:border-primary-500/30 dark:bg-primary-500/10 dark:text-primary-100">
                                {{ $note }}
                            </div>
                        @endforeach
                    </div>
                </x-filament::section>
            @endif

            <x-filament::section heading="Detalle por sección" description="Aquí ya puedes comprobar rápidamente que cada bloque heredará la materia correcta y arranca sin forzar unidad.">
                <div class="grid gap-4 xl:grid-cols-2">
                    @foreach (($preview['sections'] ?? []) as $section)
                        <div class="rounded-2xl border border-gray-200 bg-white p-5 dark:border-gray-700 dark:bg-gray-900">
                            <div class="flex flex-wrap items-start justify-between gap-3">
                                <div>
                                    <p class="text-sm font-semibold text-gray-950 dark:text-white">
                                        {{ $section['title'] ?? $section['subject_label'] ?? 'Bloque sin título' }}
                                    </p>
                                    <p class="mt-1 text-sm text-gray-500 dark:text-gray-400">
                                        {{ $section['subject_label'] ?? 'Sin materia' }}
                                        @if (filled($section['default_unit_label'] ?? null))
                                            · Unidad por defecto: {{ $section['default_unit_label'] }}
                                        @else
                                            · Unidad diferida
                                        @endif
                                    </p>
                                </div>
                                <span class="rounded-full bg-primary-50 px-3 py-1 text-xs font-semibold text-primary-700 dark:bg-primary-500/15 dark:text-primary-200">
                                    {{ data_get($section, 'summary.questions', 0) }} pregunta(s)
                                </span>
                            </div>

                            <div class="mt-4 grid gap-3 sm:grid-cols-3 xl:grid-cols-6">
                                <div class="rounded-xl border border-gray-200 bg-gray-50 p-3 text-sm dark:border-gray-700 dark:bg-gray-800/80">
                                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Contextos</p>
                                    <p class="mt-2 text-xl font-semibold text-gray-950 dark:text-white">{{ data_get($section, 'summary.contexts', 0) }}</p>
                                </div>
                                <div class="rounded-xl border border-gray-200 bg-gray-50 p-3 text-sm dark:border-gray-700 dark:bg-gray-800/80">
                                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Preguntas</p>
                                    <p class="mt-2 text-xl font-semibold text-gray-950 dark:text-white">{{ data_get($section, 'summary.questions', 0) }}</p>
                                </div>
                                <div class="rounded-xl border border-gray-200 bg-gray-50 p-3 text-sm dark:border-gray-700 dark:bg-gray-800/80">
                                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-gray-500 dark:text-gray-400">Enlaces</p>
                                    <p class="mt-2 text-xl font-semibold text-gray-950 dark:text-white">{{ data_get($section, 'summary.links', 0) }}</p>
                                </div>
                                <div class="rounded-xl border border-emerald-200 bg-emerald-50 p-3 text-sm dark:border-emerald-500/20 dark:bg-emerald-500/10">
                                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-emerald-700 dark:text-emerald-200">Nuevas</p>
                                    <p class="mt-2 text-xl font-semibold text-emerald-800 dark:text-emerald-100">{{ data_get($section, 'summary.new_questions', 0) }}</p>
                                </div>
                                <div class="rounded-xl border border-amber-200 bg-amber-50 p-3 text-sm dark:border-amber-500/20 dark:bg-amber-500/10">
                                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-amber-700 dark:text-amber-200">Repetidas exactas</p>
                                    <p class="mt-2 text-xl font-semibold text-amber-800 dark:text-amber-100">{{ data_get($section, 'summary.exact_duplicates', 0) }}</p>
                                </div>
                                <div class="rounded-xl border border-sky-200 bg-sky-50 p-3 text-sm dark:border-sky-500/20 dark:bg-sky-500/10">
                                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-sky-700 dark:text-sky-200">Parecidas</p>
                                    <p class="mt-2 text-xl font-semibold text-sky-800 dark:text-sky-100">{{ data_get($section, 'summary.similar_candidates', 0) }}</p>
                                </div>
                            </div>
                        </div>
                    @endforeach
                </div>
            </x-filament::section>
        @endif
    </div>

    <x-filament-actions::modals />
</x-filament-panels::page>
