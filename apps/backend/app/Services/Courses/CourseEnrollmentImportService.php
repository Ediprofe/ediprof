<?php

namespace App\Services\Courses;

use App\Models\Course;
use App\Models\CourseEnrollment;
use App\Models\User;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Str;

class CourseEnrollmentImportService
{
    /**
     * @return array{
     *   course: Course,
     *   summary: array{
     *     created_users:int,
     *     updated_users:int,
     *     enrolled_users:int,
     *     error_count:int
     *   },
     *   errors: array<int, array{line:int, message:string}>
     * }
     */
    public function importFromUploadedFile(Course $course, UploadedFile $csv): array
    {
        $contents = trim((string) file_get_contents($csv->getRealPath()));

        return $this->importFromContents($course, $contents);
    }

    /**
     * @return array{
     *   course: Course,
     *   summary: array{
     *     created_users:int,
     *     updated_users:int,
     *     enrolled_users:int,
     *     error_count:int
     *   },
     *   errors: array<int, array{line:int, message:string}>
     * }
     */
    public function importFromStoragePath(Course $course, string $path): array
    {
        $contents = trim((string) Storage::disk('local')->get($path));

        return $this->importFromContents($course, $contents);
    }

    /**
     * @return array{
     *   course: Course,
     *   summary: array{
     *     created_users:int,
     *     updated_users:int,
     *     enrolled_users:int,
     *     error_count:int
     *   },
     *   errors: array<int, array{line:int, message:string}>
     * }
     */
    public function importFromContents(Course $course, string $contents): array
    {
        $rows = $this->parseCsvContents($contents);
        $allowedDomain = mb_strtolower((string) config('services.google.allowed_domain', 'sanjoseitagui.edu.co'));

        $createdUsers = 0;
        $updatedUsers = 0;
        $enrolledUsers = 0;
        $errors = [];

        foreach ($rows as $index => $row) {
            $line = $index + 1;
            $email = mb_strtolower(trim((string) ($row['email'] ?? '')));
            $firstNames = $this->normalizeNullableNamePart($row['first_names'] ?? null);
            $lastNames = $this->normalizeNullableNamePart($row['last_names'] ?? null);
            $name = User::composeDisplayName($lastNames, $firstNames, (string) ($row['name'] ?? ''));
            $institutionalCode = $this->cleanNullableString($row['institutional_code'] ?? null);
            $documentNumber = $this->cleanNullableString($row['document_number'] ?? null);
            $gradeGroup = $this->cleanNullableString($row['grade_group'] ?? null);

            if ($email === '') {
                $errors[] = ['line' => $line, 'message' => 'Falta el correo institucional.'];
                continue;
            }

            if (! filter_var($email, FILTER_VALIDATE_EMAIL)) {
                $errors[] = ['line' => $line, 'message' => 'Correo inválido.'];
                continue;
            }

            $domain = (string) Str::of($email)->afterLast('@');
            if ($domain !== $allowedDomain) {
                $errors[] = ['line' => $line, 'message' => 'El correo no pertenece al dominio institucional permitido.'];
                continue;
            }

            $user = User::query()->whereRaw('LOWER(email) = ?', [$email])->first();
            $wasRecentlyCreated = false;

            if ($user === null) {
                $user = User::query()->create([
                    'name' => $name !== '' ? $name : Str::headline(Str::before($email, '@')),
                    'first_names' => $firstNames,
                    'last_names' => $lastNames,
                    'email' => $email,
                    'institutional_code' => $institutionalCode,
                    'document_number' => $documentNumber,
                    'grade_group' => $gradeGroup,
                    'password' => Hash::make(Str::random(40)),
                    'role' => 'student',
                    'member_status' => 'approved',
                    'auth_provider' => 'google',
                ]);
                $createdUsers += 1;
                $wasRecentlyCreated = true;
            } else {
                $user->forceFill([
                    'name' => $name !== '' ? $name : $user->name,
                    'first_names' => $firstNames ?? $user->first_names,
                    'last_names' => $lastNames ?? $user->last_names,
                    'role' => $user->isAdmin() ? 'admin' : 'student',
                    'member_status' => $user->member_status === 'blocked' ? 'blocked' : 'approved',
                    'auth_provider' => $user->auth_provider ?: 'google',
                    'institutional_code' => $institutionalCode ?? $user->institutional_code,
                    'document_number' => $documentNumber ?? $user->document_number,
                    'grade_group' => $gradeGroup ?? $user->grade_group,
                ])->save();

                if (! $wasRecentlyCreated) {
                    $updatedUsers += 1;
                }
            }

            CourseEnrollment::query()->updateOrCreate(
                [
                    'course_id' => $course->id,
                    'user_id' => $user->id,
                ],
                [
                    'status' => 'active',
                    'source' => 'csv_import',
                ],
            );

            $enrolledUsers += 1;
        }

        return [
            'course' => $course->refresh(),
            'summary' => [
                'created_users' => $createdUsers,
                'updated_users' => $updatedUsers,
                'enrolled_users' => $enrolledUsers,
                'error_count' => count($errors),
            ],
            'errors' => $errors,
        ];
    }

    /**
     * @return array<int, array{
     *   email:string,
     *   name:string,
     *   first_names:?string,
     *   last_names:?string,
     *   institutional_code:?string,
     *   document_number:?string,
     *   grade_group:?string
     * }>
     */
    protected function parseCsvContents(string $contents): array
    {
        $contents = trim($contents);

        if ($contents === '') {
            return [];
        }

        $lines = preg_split('/\r\n|\n|\r/', preg_replace('/^\xEF\xBB\xBF/', '', $contents) ?: '');

        if (! is_array($lines) || $lines === []) {
            return [];
        }

        $rows = [];
        $delimiter = $this->detectDelimiter((string) $lines[0]);
        $header = array_map(
            fn ($value) => $this->normalizeHeader((string) $value),
            str_getcsv((string) $lines[0], $delimiter)
        );
        $hasHeader = in_array('email', $header, true)
            || in_array('correo', $header, true)
            || in_array('correo electronico', $header, true);

        $emailIndex = 0;
        $nameIndex = 1;
        $firstNamesIndex = null;
        $lastNamesIndex = null;
        $institutionalCodeIndex = null;
        $documentNumberIndex = null;
        $gradeGroupIndex = null;
        $startIndex = 0;

        if ($hasHeader) {
            $startIndex = 1;
            $emailIndex = array_search('email', $header, true);

            if ($emailIndex === false) {
                $emailIndex = array_search('correo', $header, true);
            }

            if ($emailIndex === false) {
                $emailIndex = array_search('correo electronico', $header, true);
            }

            $nameIndex = array_search('name', $header, true);

            if ($nameIndex === false) {
                $nameIndex = array_search('nombre', $header, true);
            }

            if ($nameIndex === false) {
                $nameIndex = array_search('nombre usuario', $header, true);
            }

            if ($nameIndex === false) {
                $nameIndex = 1;
            }

            $firstNamesIndex = array_search('nombres', $header, true);

            if ($firstNamesIndex === false) {
                $firstNamesIndex = array_search('nombre', $header, true);
            }

            $lastNamesIndex = array_search('apellidos', $header, true);
            $institutionalCodeIndex = array_search('matricula', $header, true);
            $documentNumberIndex = array_search('documento', $header, true);
            $gradeGroupIndex = array_search('grupo', $header, true);

            $firstNamesIndex = $firstNamesIndex === false ? null : $firstNamesIndex;
            $lastNamesIndex = $lastNamesIndex === false ? null : $lastNamesIndex;
            $institutionalCodeIndex = $institutionalCodeIndex === false ? null : $institutionalCodeIndex;
            $documentNumberIndex = $documentNumberIndex === false ? null : $documentNumberIndex;
            $gradeGroupIndex = $gradeGroupIndex === false ? null : $gradeGroupIndex;
        }

        for ($i = $startIndex; $i < count($lines); $i += 1) {
            $line = trim((string) $lines[$i]);

            if ($line === '') {
                continue;
            }

            $columns = str_getcsv($line, $delimiter);

            if (! is_array($columns)) {
                continue;
            }

            $rawName = trim((string) ($columns[$nameIndex] ?? ''));
            $parsedName = User::splitAcademicName($rawName);
            $firstNames = $this->normalizeNullableNamePart(
                $firstNamesIndex !== null ? ($columns[$firstNamesIndex] ?? null) : $parsedName['first_names']
            );
            $lastNames = $this->normalizeNullableNamePart(
                $lastNamesIndex !== null ? ($columns[$lastNamesIndex] ?? null) : $parsedName['last_names']
            );

            $rows[] = [
                'email' => trim((string) ($columns[$emailIndex] ?? '')),
                'name' => User::composeDisplayName($lastNames, $firstNames, $parsedName['display_name']),
                'first_names' => $firstNames,
                'last_names' => $lastNames,
                'institutional_code' => $this->cleanNullableString(
                    $institutionalCodeIndex !== null ? ($columns[$institutionalCodeIndex] ?? null) : null
                ),
                'document_number' => $this->cleanNullableString(
                    $documentNumberIndex !== null ? ($columns[$documentNumberIndex] ?? null) : null
                ),
                'grade_group' => $this->cleanNullableString(
                    $gradeGroupIndex !== null ? ($columns[$gradeGroupIndex] ?? null) : null
                ),
            ];
        }

        return $rows;
    }

    protected function normalizeHeader(string $value): string
    {
        return Str::of($value)
            ->lower()
            ->ascii()
            ->replaceMatches('/\s+/', ' ')
            ->trim()
            ->value();
    }

    protected function detectDelimiter(string $headerLine): string
    {
        $commaCount = substr_count($headerLine, ',');
        $semicolonCount = substr_count($headerLine, ';');

        return $semicolonCount > $commaCount ? ';' : ',';
    }

    protected function cleanNullableString(mixed $value): ?string
    {
        $value = trim((string) $value);

        return $value !== '' ? $value : null;
    }

    protected function normalizeNullableNamePart(mixed $value): ?string
    {
        $value = User::normalizeAcademicNamePart((string) $value);

        return $value !== '' ? $value : null;
    }
}
