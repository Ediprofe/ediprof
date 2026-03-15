import { Link } from '@inertiajs/react';
import { useEffect, useMemo, useState } from 'react';

import MembersLayout from '../Layouts/MembersLayout';
import type { AttemptEvaluation, AttemptPayload, MemberAssignment, NavItem } from '../types';
import AttemptPlayer from './AttemptPlayer';

type AssignmentSection = 'evaluations' | 'workshops' | 'simulacros';

type AssignmentDetailPageProps = {
    pageTitle: string;
    subtitle?: string;
    assignment: MemberAssignment;
    section: AssignmentSection;
};

type SectionConfig = {
    backHref: string;
    backLabel: string;
    navigation: NavItem[];
};

type ModeCopy = {
    label: string;
    heading: string;
    description: string;
    startAction: string;
    continueAction: string;
    reviewAction: string;
    startError: string;
    submitError: string;
    policyNote: string;
};

function buildNavigation(section: AssignmentSection): NavItem[] {
    return [
        { label: 'Panel', href: '/miembros-v2' },
        { label: 'Evaluaciones', href: '/miembros-v2/evaluaciones', active: section === 'evaluations' },
        { label: 'Talleres', href: '/miembros-v2/talleres', active: section === 'workshops' },
        { label: 'Simulacros', href: '/miembros-v2/simulacros', active: section === 'simulacros' },
    ];
}

function getSectionConfig(section: AssignmentSection): SectionConfig {
    switch (section) {
        case 'workshops':
            return {
                backHref: '/miembros-v2/talleres',
                backLabel: 'Volver a talleres',
                navigation: buildNavigation(section),
            };
        case 'simulacros':
            return {
                backHref: '/miembros-v2/simulacros',
                backLabel: 'Volver a simulacros',
                navigation: buildNavigation(section),
            };
        default:
            return {
                backHref: '/miembros-v2/evaluaciones',
                backLabel: 'Volver a evaluaciones',
                navigation: buildNavigation(section),
            };
    }
}

function getModeCopy(mode: string): ModeCopy {
    if (mode === 'study') {
        return {
            label: 'Taller',
            heading: 'Detalle de taller',
            description: 'Vas a trabajar con verificacion inmediata y con el avance guardado en el backend academico.',
            startAction: 'Iniciar taller',
            continueAction: 'Continuar taller',
            reviewAction: 'Reabrir taller',
            startError: 'No pudimos abrir el taller.',
            submitError: 'No pudimos cerrar el taller.',
            policyNote: 'Cada respuesta se verifica al instante para que estudies desde el error sin perder tu progreso.',
        };
    }

    if (mode === 'simulacro') {
        return {
            label: 'Simulacro',
            heading: 'Detalle de simulacro',
            description: 'Aqui vas a resolver un intento estable, con entrega final y revision segun la politica definida por el docente.',
            startAction: 'Iniciar simulacro',
            continueAction: 'Continuar simulacro',
            reviewAction: 'Abrir revision',
            startError: 'No pudimos abrir el simulacro.',
            submitError: 'No pudimos entregar el simulacro.',
            policyNote: 'El orden del intento y la revision dependen de la configuracion academica guardada en backend.',
        };
    }

    return {
        label: 'Evaluacion',
        heading: 'Detalle de evaluacion',
        description: 'Esta vista ya consume la asignacion real del backend y sera la base estable del panel web del estudiante.',
        startAction: 'Iniciar evaluacion',
        continueAction: 'Continuar evaluacion',
        reviewAction: 'Abrir revision',
        startError: 'No pudimos iniciar o reanudar la evaluacion.',
        submitError: 'No pudimos entregar la evaluacion.',
        policyNote: 'La evaluacion usa el intento academico real, con resultados y retroalimentacion controlada desde el panel docente.',
    };
}

async function requestJson<T>(url: string, init: RequestInit = {}): Promise<T> {
    const csrf = document
        .querySelector('meta[name="csrf-token"]')
        ?.getAttribute('content');

    const response = await fetch(url, {
        credentials: 'same-origin',
        ...init,
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            ...(csrf ? { 'X-CSRF-TOKEN': csrf } : {}),
            ...(init.headers ?? {}),
        },
    });

    const payload = await response.json().catch(() => null);

    if (!response.ok || !payload?.ok) {
        throw new Error(payload?.error?.message ?? 'No pudimos completar la accion en la zona de miembros.');
    }

    return payload.data as T;
}

export default function AssignmentDetailPage({
    pageTitle,
    subtitle,
    assignment,
    section,
}: AssignmentDetailPageProps) {
    const [attemptPayload, setAttemptPayload] = useState<AttemptPayload | null>(null);
    const [loadingAttempt, setLoadingAttempt] = useState(false);
    const [submittingAttempt, setSubmittingAttempt] = useState(false);
    const [pendingQuestionId, setPendingQuestionId] = useState<string | null>(null);
    const [errorMessage, setErrorMessage] = useState<string | null>(null);

    const sectionConfig = useMemo(() => getSectionConfig(section), [section]);
    const modeCopy = useMemo(() => getModeCopy(assignment.mode), [assignment.mode]);
    const canOpenActivity = assignment.availability.can_start || Boolean(assignment.latest_attempt);

    const primaryActionLabel = useMemo(() => {
        if (!canOpenActivity) {
            return 'No disponible';
        }

        if (assignment.latest_attempt?.can_review) {
            return modeCopy.reviewAction;
        }

        if (assignment.latest_attempt) {
            return modeCopy.continueAction;
        }

        return modeCopy.startAction;
    }, [assignment.latest_attempt, canOpenActivity, modeCopy]);

    async function loadAttempt(attemptId: string): Promise<void> {
        setLoadingAttempt(true);
        setErrorMessage(null);

        try {
            const data = await requestJson<AttemptPayload>(`/miembros-v2/intentos/${attemptId}`);
            setAttemptPayload(data);
        } catch (error) {
            setErrorMessage(error instanceof Error ? error.message : 'No pudimos cargar el intento.');
        } finally {
            setLoadingAttempt(false);
        }
    }

    async function startOrResumeAttempt(): Promise<void> {
        setLoadingAttempt(true);
        setErrorMessage(null);

        try {
            const data = await requestJson<AttemptPayload>(`/miembros-v2/asignaciones/${assignment.id}/intento`, {
                method: 'POST',
                body: JSON.stringify({}),
            });
            setAttemptPayload(data);
        } catch (error) {
            setErrorMessage(error instanceof Error ? error.message : modeCopy.startError);
        } finally {
            setLoadingAttempt(false);
        }
    }

    async function handleAnswer(questionId: string, optionId: string): Promise<AttemptEvaluation | null> {
        if (!attemptPayload) {
            return null;
        }

        setPendingQuestionId(questionId);
        setErrorMessage(null);

        try {
            const data = await requestJson<AttemptEvaluation>(
                `/miembros-v2/intentos/${attemptPayload.attempt.id}/preguntas/${questionId}`,
                {
                    method: 'PATCH',
                    body: JSON.stringify({ option_id: optionId }),
                },
            );

            setAttemptPayload((current) => {
                if (!current) {
                    return current;
                }

                return {
                    ...current,
                    selected_by_question: {
                        ...current.selected_by_question,
                        [questionId]: optionId,
                    },
                    evaluation_by_question:
                        data && data.is_correct !== null
                            ? {
                                  ...current.evaluation_by_question,
                                  [questionId]: data,
                              }
                            : current.evaluation_by_question,
                };
            });

            return data;
        } catch (error) {
            setErrorMessage(error instanceof Error ? error.message : 'No pudimos guardar la respuesta.');
            return null;
        } finally {
            setPendingQuestionId(null);
        }
    }

    async function handleSubmit(): Promise<void> {
        if (!attemptPayload) {
            return;
        }

        setSubmittingAttempt(true);
        setErrorMessage(null);

        try {
            const data = await requestJson<AttemptPayload>(`/miembros-v2/intentos/${attemptPayload.attempt.id}/entregar`, {
                method: 'POST',
                body: JSON.stringify({}),
            });
            setAttemptPayload(data);
        } catch (error) {
            setErrorMessage(error instanceof Error ? error.message : modeCopy.submitError);
        } finally {
            setSubmittingAttempt(false);
        }
    }

    useEffect(() => {
        if (assignment.latest_attempt?.id) {
            void loadAttempt(assignment.latest_attempt.id);
        }
    }, [assignment.latest_attempt?.id]);

    return (
        <MembersLayout title={pageTitle} subtitle={subtitle} navigation={sectionConfig.navigation}>
            <section className="grid gap-6 xl:grid-cols-[minmax(0,1.35fr)_minmax(320px,0.85fr)]">
                <article className="rounded-[28px] border border-slate-200 bg-white p-6 shadow-[0_18px_42px_-30px_rgba(15,23,42,0.35)]">
                    <p className="text-sm font-black uppercase tracking-[0.22em] text-blue-600">{modeCopy.heading}</p>
                    <h2 className="mt-4 text-2xl font-black tracking-tight text-slate-950 sm:text-3xl">{assignment.title}</h2>
                    <p className="mt-3 max-w-2xl text-base leading-7 text-slate-600">{modeCopy.description}</p>

                    <div className="mt-6 grid gap-4 md:grid-cols-2">
                        <div className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-4">
                            <p className="text-xs font-black uppercase tracking-[0.2em] text-slate-500">Modo</p>
                            <p className="mt-2 text-xl font-bold text-slate-950">{modeCopy.label}</p>
                        </div>
                        <div className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-4">
                            <p className="text-xs font-black uppercase tracking-[0.2em] text-slate-500">Estado</p>
                            <p className="mt-2 text-xl font-bold text-slate-950">
                                {assignment.latest_attempt?.feedback_state_label ?? assignment.availability.state}
                            </p>
                        </div>
                        <div className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-4">
                            <p className="text-xs font-black uppercase tracking-[0.2em] text-slate-500">Preguntas</p>
                            <p className="mt-2 text-xl font-bold text-slate-950">{assignment.stats.effective_questions}</p>
                        </div>
                        <div className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-4">
                            <p className="text-xs font-black uppercase tracking-[0.2em] text-slate-500">Intentos</p>
                            <p className="mt-2 text-xl font-bold text-slate-950">
                                {assignment.attempts.used} / {assignment.attempts.limit ?? '∞'}
                            </p>
                        </div>
                    </div>

                    <div className="mt-6 rounded-2xl border border-slate-200 bg-slate-50 px-4 py-4 text-sm leading-7 text-slate-700">
                        <p>
                            <strong>Curso:</strong> {assignment.course?.name ?? 'Sin curso'}
                        </p>
                        <p>
                            <strong>Plantilla base:</strong> {assignment.template?.title ?? 'Sin plantilla sincronizada'}
                        </p>
                        <p>
                            <strong>Disponibilidad:</strong> {assignment.availability.message ?? 'La actividad esta disponible para tu cuenta.'}
                        </p>
                        <p>
                            <strong>Retroalimentacion:</strong> {assignment.feedback.policy_label}
                        </p>
                        {assignment.latest_attempt ? (
                            <p>
                                <strong>Ultimo intento:</strong> {assignment.latest_attempt.status} ·{' '}
                                {assignment.latest_attempt.score_scale !== null
                                    ? `${assignment.latest_attempt.score_scale.toFixed(1)} / 5`
                                    : 'Sin calificacion todavia'}
                            </p>
                        ) : null}
                    </div>

                    <div className="mt-6 flex flex-wrap gap-3">
                        <button
                            type="button"
                            onClick={() => void startOrResumeAttempt()}
                            disabled={loadingAttempt || !canOpenActivity}
                            className="rounded-full bg-blue-600 px-5 py-3 text-sm font-bold text-white shadow-lg shadow-blue-500/25 transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-60"
                        >
                            {loadingAttempt ? 'Cargando…' : primaryActionLabel}
                        </button>
                        <Link
                            href={sectionConfig.backHref}
                            className="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-bold text-slate-700 no-underline"
                        >
                            {sectionConfig.backLabel}
                        </Link>
                    </div>
                </article>

                <aside className="rounded-[28px] border border-slate-200 bg-white p-6 shadow-[0_18px_42px_-30px_rgba(15,23,42,0.35)]">
                    <p className="text-sm font-black uppercase tracking-[0.22em] text-amber-600">Politica de revision</p>
                    <p className="mt-4 text-base leading-7 text-slate-700">{assignment.feedback.message}</p>

                    <div className="mt-6 rounded-2xl border border-amber-200 bg-amber-50 px-4 py-4 text-sm leading-6 text-amber-900">
                        {modeCopy.policyNote}
                    </div>
                </aside>
            </section>

            {errorMessage ? (
                <section className="rounded-2xl border border-rose-200 bg-rose-50 px-5 py-4 text-sm font-medium text-rose-900">
                    {errorMessage}
                </section>
            ) : null}

            {attemptPayload ? (
                <AttemptPlayer
                    payload={attemptPayload}
                    onAnswer={handleAnswer}
                    onSubmit={handleSubmit}
                    pendingQuestionId={pendingQuestionId}
                    submitting={submittingAttempt}
                    assignmentFeedbackMessage={assignment.feedback.message}
                />
            ) : null}
        </MembersLayout>
    );
}
