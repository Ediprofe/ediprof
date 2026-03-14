<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 12px;
            color: #111827;
        }

        h1, p {
            margin: 0 0 8px;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 16px;
        }

        th, td {
            border: 1px solid #cbd5e1;
            padding: 6px 8px;
            text-align: left;
            vertical-align: top;
        }

        th {
            background: #f8fafc;
            font-weight: 700;
        }

        .note-column {
            background: #fef3c7;
            font-weight: 700;
        }

        .meta {
            color: #475569;
        }
    </style>
</head>
<body>
    <h1>{{ $title }}</h1>
    <p class="meta"><strong>Curso:</strong> {{ $courseName }}</p>
    <p class="meta"><strong>Plantilla base:</strong> {{ $templateTitle }}</p>
    <p class="meta"><strong>Uso sugerido:</strong> {{ $usageHint ?? 'copia la columna Nota / 5 al sistema del colegio.' }}</p>

    <table>
        <thead>
            <tr>
                @foreach ($headers as $index => $header)
                    <th @class(['note-column' => $header === 'Nota / 5'])>{{ $header }}</th>
                @endforeach
            </tr>
        </thead>
        <tbody>
            @foreach ($rows as $row)
                <tr>
                    @foreach ($row as $index => $value)
                        <td @class(['note-column' => ($headers[$index] ?? null) === 'Nota / 5'])>{{ $value }}</td>
                    @endforeach
                </tr>
            @endforeach
        </tbody>
    </table>
</body>
</html>
