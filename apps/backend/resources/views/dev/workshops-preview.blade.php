<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Preview Talleres - Backend</title>
    <style>
        :root {
            color-scheme: light dark;
            --bg: #0b1020;
            --panel: #10172d;
            --muted: #9fb0d2;
            --text: #e7ecff;
            --ok: #16c47f;
            --warn: #ffcc4d;
            --err: #ff7b7b;
            --line: #233153;
            --accent: #4f7cff;
        }
        body {
            margin: 0;
            font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
            background: linear-gradient(180deg, #091022, #0e1731 40%, #0b1020);
            color: var(--text);
        }
        .wrap {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .panel {
            background: color-mix(in oklab, var(--panel) 88%, black);
            border: 1px solid var(--line);
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 16px;
        }
        h1, h2, h3 {
            margin: 0 0 10px;
        }
        .muted {
            color: var(--muted);
            font-size: 14px;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 16px;
        }
        .row {
            display: flex;
            gap: 10px;
            align-items: center;
            flex-wrap: wrap;
        }
        input[type="text"] {
            width: 100%;
            min-width: 280px;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 8px 10px;
            background: #0a1228;
            color: var(--text);
        }
        button {
            border: 1px solid var(--accent);
            border-radius: 8px;
            padding: 8px 12px;
            background: color-mix(in oklab, var(--accent) 25%, #0a1228);
            color: #dfe7ff;
            cursor: pointer;
        }
        .tag {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 99px;
            border: 1px solid var(--line);
            font-size: 12px;
            margin-right: 6px;
        }
        .tag.ok { border-color: color-mix(in oklab, var(--ok) 50%, var(--line)); }
        .tag.warn { border-color: color-mix(in oklab, var(--warn) 50%, var(--line)); }
        .tag.err { border-color: color-mix(in oklab, var(--err) 50%, var(--line)); }
        .list {
            max-height: 340px;
            overflow: auto;
            border: 1px solid var(--line);
            border-radius: 8px;
        }
        .list a {
            display: block;
            padding: 10px;
            color: #d8e1ff;
            text-decoration: none;
            border-bottom: 1px solid #1b2848;
        }
        .list a:hover { background: #0f1a35; }
        .q {
            border: 1px solid #22325a;
            border-radius: 10px;
            padding: 12px;
            margin-bottom: 10px;
            background: #0b142b;
        }
        .opts { margin: 8px 0 0; padding: 0; list-style: none; }
        .opts li {
            padding: 6px 8px;
            border-radius: 6px;
            margin-bottom: 6px;
            background: #0e1a36;
            border: 1px solid #1e2e56;
        }
        .opts li.correct {
            border-color: color-mix(in oklab, var(--ok) 60%, #1e2e56);
            background: color-mix(in oklab, var(--ok) 10%, #0e1a36);
        }
        pre {
            overflow: auto;
            border: 1px solid #26375f;
            border-radius: 8px;
            padding: 10px;
            background: #081025;
        }
        @media (max-width: 900px) {
            .grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
<div class="wrap">
    <div class="panel">
        <h1>Preview Talleres (Local)</h1>
        <p class="muted">Vista de desarrollo para revisar payload de talleres y modo estudiante/docente sin esperar Expo.</p>
        <form method="get" action="{{ route('dev.workshops.preview') }}" class="row">
            <input type="text" name="workshop_id" value="{{ $selectedId }}" placeholder="external_id, content_external_id o route">
            <label>
                <input type="checkbox" name="include_answers" value="1" {{ $includeAnswers ? 'checked' : '' }}>
                include_answers
            </label>
            <button type="submit">Actualizar</button>
        </form>
    </div>

    <div class="grid">
        <div class="panel">
            <h2>Talleres sincronizados</h2>
            <div class="list">
                @forelse($workshops as $item)
                    <a href="{{ route('dev.workshops.preview', ['workshop_id' => $item->external_id, 'include_answers' => $includeAnswers ? 1 : 0]) }}">
                        <strong>{{ $item->title }}</strong><br>
                        <span class="muted">{{ $item->external_id }}</span><br>
                        <span class="tag {{ $item->access_tier === 'premium' ? 'warn' : 'ok' }}">{{ $item->access_tier }}</span>
                        <span class="tag {{ $item->is_published ? 'ok' : 'err' }}">{{ $item->is_published ? 'published' : 'draft' }}</span>
                    </a>
                @empty
                    <div style="padding:10px" class="muted">No hay talleres en DB. Ejecuta <code>workshops:sync-manifest</code>.</div>
                @endforelse
            </div>
        </div>

        <div>
            @if($payload)
                <div class="panel">
                    <h2>{{ $payload['title'] }}</h2>
                    <div class="row" style="margin-bottom:10px;">
                        <span class="tag">{{ $payload['id'] }}</span>
                        <span class="tag">{{ $payload['route'] }}</span>
                        <span class="tag {{ $payload['access_tier'] === 'premium' ? 'warn' : 'ok' }}">{{ $payload['access_tier'] }}</span>
                        <span class="tag {{ $payload['published'] ? 'ok' : 'err' }}">{{ $payload['published'] ? 'published' : 'draft' }}</span>
                        <span class="tag">Q: {{ $payload['stats']['total_questions'] ?? 0 }}</span>
                    </div>
                    <div class="muted">API ejemplo:</div>
                    <pre>GET {{ url('/api/v1/workshops/'.$payload['id']) }}?published_only=false&include_answers={{ $includeAnswers ? 'true' : 'false' }}</pre>
                </div>

                <div class="panel">
                    <h3>Preguntas (primeras 5)</h3>
                    @foreach(array_slice($payload['questions'] ?? [], 0, 5) as $q)
                        <div class="q">
                            <strong>#{{ $q['order'] ?? '?' }} · {{ $q['id'] ?? '' }}</strong>
                            <div class="muted">{{ $q['meta']['fuente'] ?? 'sin fuente' }} @if(!empty($q['meta']['anio'])) · {{ $q['meta']['anio'] }} @endif</div>
                            <ul class="opts">
                                @foreach($q['options'] ?? [] as $option)
                                    <li class="{{ (!empty($option['is_correct']) ? 'correct' : '') }}">
                                        <strong>{{ $option['id'] }}</strong>. {{ $option['text'] }}
                                    </li>
                                @endforeach
                            </ul>
                            @if(!empty($q['correct_option_id']))
                                <div class="muted">Correcta: {{ $q['correct_option_id'] }}</div>
                            @else
                                <div class="muted">Correcta oculta (modo estudiante)</div>
                            @endif
                        </div>
                    @endforeach
                </div>
            @else
                <div class="panel">
                    <h2>Sin taller seleccionado</h2>
                    <p class="muted">No pude resolver el identificador. Selecciona uno del panel izquierdo.</p>
                </div>
            @endif
        </div>
    </div>
</div>
</body>
</html>
