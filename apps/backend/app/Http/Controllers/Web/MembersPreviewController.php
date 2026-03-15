<?php

namespace App\Http\Controllers\Web;

use App\Http\Controllers\Controller;
use Inertia\Inertia;
use Inertia\Response;

class MembersPreviewController extends Controller
{
    public function dashboard(): Response
    {
        return Inertia::render('Members/Dashboard', [
            'pageTitle' => 'Panel del estudiante',
            'subtitle' => 'Preview técnico de Members v2 dentro de Laravel + Inertia + React.',
            'quickStats' => [
                ['label' => 'Evaluaciones pendientes', 'value' => 2],
                ['label' => 'Talleres activos', 'value' => 3],
                ['label' => 'Simulacros recientes', 'value' => 1],
            ],
            'highlights' => [
                [
                    'title' => 'Evaluaciones',
                    'description' => 'Flujo principal para actividades calificables, retroalimentación y resultados.',
                    'href' => route('members.preview.evaluations'),
                    'emoji' => '📝',
                ],
                [
                    'title' => 'Talleres',
                    'description' => 'Prácticas guiadas y reforzamiento con retroalimentación inmediata.',
                    'href' => route('members.preview.workshops'),
                    'emoji' => '✍️',
                ],
                [
                    'title' => 'Simulacros',
                    'description' => 'Sesiones diagnósticas y de entrenamiento con intento completo.',
                    'href' => route('members.preview.simulacros'),
                    'emoji' => '🚀',
                ],
            ],
            'timeline' => [
                ['label' => 'Primero', 'text' => 'Cerrar el flujo web del estudiante con componentes reales y navegación estable.'],
                ['label' => 'Después', 'text' => 'Consolidar login Google web con Socialite y sesiones.'],
                ['label' => 'Luego', 'text' => 'Reutilizar el mismo backend para móvil con Expo / React Native.'],
            ],
        ]);
    }

    public function evaluations(): Response
    {
        return Inertia::render('Members/Evaluations/Index', [
            'pageTitle' => 'Evaluaciones',
            'subtitle' => 'Vista inicial del catálogo web que luego reemplazará la zona de miembros en Astro.',
            'items' => [
                [
                    'id' => 'preview-eval-1',
                    'title' => 'Evaluación módulo 1',
                    'status' => 'Pendiente',
                    'mode' => 'Evaluación',
                    'questions' => 20,
                    'href' => route('members.preview.evaluations.show', 'preview-eval-1'),
                ],
                [
                    'id' => 'preview-eval-2',
                    'title' => 'Evaluación de cierre',
                    'status' => 'Retroalimentación disponible',
                    'mode' => 'Evaluación',
                    'questions' => 15,
                    'href' => route('members.preview.evaluations.show', 'preview-eval-2'),
                ],
            ],
        ]);
    }

    public function showEvaluation(string $evaluation): Response
    {
        return Inertia::render('Members/Evaluations/Show', [
            'pageTitle' => 'Abrir evaluación',
            'subtitle' => 'Shell de detalle para el flujo de lobby, intento y revisión.',
            'evaluation' => [
                'id' => $evaluation,
                'title' => 'Preview de evaluación',
                'status' => 'Disponible',
                'mode' => 'Evaluación',
                'questions' => 20,
                'attempts_used' => 0,
                'attempts_limit' => 1,
                'feedback_policy' => 'Retroalimentación al entregar o cuando el docente la libere.',
            ],
        ]);
    }

    public function workshops(): Response
    {
        return Inertia::render('Members/Workshops/Index', [
            'pageTitle' => 'Talleres',
            'subtitle' => 'Vista inicial para prácticas guiadas dentro de Members v2.',
        ]);
    }

    public function simulacros(): Response
    {
        return Inertia::render('Members/Simulacros/Index', [
            'pageTitle' => 'Simulacros',
            'subtitle' => 'Vista inicial para simulacros dentro de Members v2.',
        ]);
    }
}
