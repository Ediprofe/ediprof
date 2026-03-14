<?php

namespace App\Http\Controllers\Web\Admin;

use App\Http\Controllers\Controller;
use App\Models\AssessmentAssignment;
use App\Models\Course;
use App\Services\Assessments\AssessmentResultsExportService;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\StreamedResponse;

class AssessmentResultsExportController extends Controller
{
    public function assignment(
        Request $request,
        AssessmentAssignment $assignment,
        AssessmentResultsExportService $exportService,
    ): StreamedResponse {
        abort_unless($request->user()?->isAdmin(), 403);

        return $exportService->streamAssignmentCsv($assignment);
    }

    public function assignmentExcel(
        Request $request,
        AssessmentAssignment $assignment,
        AssessmentResultsExportService $exportService,
    ): \Symfony\Component\HttpFoundation\Response {
        abort_unless($request->user()?->isAdmin(), 403);

        return $exportService->downloadAssignmentExcel($assignment);
    }

    public function assignmentMinimalExcel(
        Request $request,
        AssessmentAssignment $assignment,
        AssessmentResultsExportService $exportService,
    ): \Symfony\Component\HttpFoundation\Response {
        abort_unless($request->user()?->isAdmin(), 403);

        return $exportService->downloadAssignmentMinimalExcel($assignment);
    }

    public function course(
        Request $request,
        Course $course,
        AssessmentResultsExportService $exportService,
    ): StreamedResponse {
        abort_unless($request->user()?->isAdmin(), 403);

        return $exportService->streamCourseCsv($course);
    }
}
