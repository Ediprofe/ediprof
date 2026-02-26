<?php

return [
    'paths' => ['api/*', 'sanctum/csrf-cookie'],

    'allowed_methods' => ['*'],

    'allowed_origins' => array_values(array_filter(array_map(
        static fn (?string $origin): ?string => $origin !== null ? trim($origin) : null,
        explode(',', (string) env('CORS_ALLOWED_ORIGINS', 'http://127.0.0.1:4321,http://localhost:4321,http://localhost:19006,https://ediprofe.com,https://www.ediprofe.com'))
    ))),

    'allowed_origins_patterns' => [],

    'allowed_headers' => ['*'],

    'exposed_headers' => [],

    'max_age' => 0,

    'supports_credentials' => false,
];

