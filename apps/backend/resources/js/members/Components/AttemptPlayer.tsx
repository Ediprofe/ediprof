import { useEffect, useMemo, useState } from 'react';

import type { AttemptEvaluation, AttemptPayload, AttemptQuestion } from '../types';
import { RichContent, RichOptionContent } from './RichContent';

type AttemptPlayerProps = {
    payload: AttemptPayload;
    onAnswer: (questionId: string, optionId: string) => Promise<AttemptEvaluation | null>;
    onSubmit: () => Promise<void>;
    pendingQuestionId?: string | null;
    submitting?: boolean;
    assignmentFeedbackMessage?: string;
};

function getModeLabel(mode: string): string {
    if (mode === 'study') {
        return 'Taller';
    }

    if (mode === 'simulacro') {
        return 'Simulacro';
    }

    return 'Evaluación';
}


export default function AttemptPlayer({
    payload,
    onAnswer,
    onSubmit,
    pendingQuestionId,
    submitting = false,
    assignmentFeedbackMessage,
}: AttemptPlayerProps) {
    const [currentIndex, setCurrentIndex] = useState(0);
    const questions = payload.questions ?? [];
    const currentQuestion = questions[currentIndex] ?? null;
    const selectedByQuestion = payload.selected_by_question ?? {};
    const evaluationByQuestion = payload.evaluation_by_question ?? {};

    const scoreSummary = useMemo(() => {
        const total = questions.length;
        const answered = Object.keys(selectedByQuestion).length;
        const correct = Object.values(evaluationByQuestion).filter((item) => item?.is_correct).length;
        const wrong = payload.attempt.can_review ? Math.max(answered - correct, 0) : 0;

        return { total, answered, correct, wrong };
    }, [questions.length, selectedByQuestion, evaluationByQuestion, payload.attempt.can_review]);

    useEffect(() => {
        if (questions.length === 0) {
            setCurrentIndex(0);

            return;
        }

        if (payload.attempt.can_review) {
            const firstWrongIndex = questions.findIndex((question) => evaluationByQuestion[question.id] && !evaluationByQuestion[question.id]?.is_correct);
            if (firstWrongIndex >= 0) {
                setCurrentIndex(firstWrongIndex);

                return;
            }
        }

        if (!payload.attempt.submitted) {
            const firstPendingIndex = questions.findIndex((question) => !selectedByQuestion[question.id]);
            if (firstPendingIndex >= 0) {
                setCurrentIndex(firstPendingIndex);

                return;
            }
        }

        setCurrentIndex((value) => Math.min(value, Math.max(questions.length - 1, 0)));
    }, [
        payload.attempt.id,
        payload.attempt.submitted,
        payload.attempt.can_review,
        questions,
        selectedByQuestion,
        evaluationByQuestion,
    ]);

    if (!currentQuestion) {
        return (
            <section className="rounded-[28px] border border-slate-200 bg-white p-6 text-sm text-slate-600 shadow-[0_18px_42px_-30px_rgba(15,23,42,0.35)]">
                Este intento no tiene preguntas disponibles.
            </section>
        );
    }

    const currentEvaluation = evaluationByQuestion[currentQuestion.id] ?? null;
    const selectedOptionId = selectedByQuestion[currentQuestion.id] ?? null;
    const canAnswer = !payload.attempt.submitted;
    const unansweredCount = Math.max(scoreSummary.total - scoreSummary.answered, 0);
    const isStudyMode = payload.attempt.mode === 'study';
    const showReviewForCurrentQuestion = Boolean((payload.attempt.can_review || isStudyMode) && currentEvaluation);

    async function handleSelectOption(question: AttemptQuestion, optionId: string): Promise<void> {
        const result = await onAnswer(question.id, optionId);

        if (result === null) {
            return;
        }

        if (!payload.attempt.submitted) {
            setCurrentIndex((value) => Math.min(value + 1, Math.max(questions.length - 1, 0)));
        }
    }

    async function handleSubmitClick(): Promise<void> {
        if (unansweredCount > 0) {
            const confirmed = window.confirm(
                `Todavía te faltan ${unansweredCount} pregunta${unansweredCount === 1 ? '' : 's'} por responder. ¿Quieres entregar de todas formas?`,
            );

            if (!confirmed) {
                return;
            }
        }

        await onSubmit();
    }

    return (
        <section className="grid gap-6">
            <article className="rounded-[28px] border border-slate-200 bg-white p-6 shadow-[0_18px_42px_-30px_rgba(15,23,42,0.35)]">
                <div className="flex flex-wrap items-center justify-between gap-3">
                    <div>
                        <p className="text-sm font-black uppercase tracking-[0.2em] text-blue-600">Intento activo</p>
                        <h3 className="mt-2 text-2xl font-black tracking-tight text-slate-950">{payload.title}</h3>
                    </div>
                    <div className="flex flex-wrap gap-2">
                        <span className="rounded-full border border-blue-200 bg-blue-50 px-3 py-1 text-sm font-semibold text-blue-800">
                            {getModeLabel(payload.attempt.mode)}
                        </span>
                        <span className="rounded-full border border-slate-200 bg-slate-50 px-3 py-1 text-sm font-semibold text-slate-700">
                            {scoreSummary.answered}/{scoreSummary.total} respondidas
                        </span>
                        {!payload.attempt.submitted ? (
                            <span className="rounded-full border border-amber-200 bg-amber-50 px-3 py-1 text-sm font-semibold text-amber-800">
                                {unansweredCount} pendientes
                            </span>
                        ) : null}
                        {payload.attempt.score_scale !== null && payload.attempt.score_scale !== undefined ? (
                            <span className="rounded-full border border-emerald-200 bg-emerald-50 px-3 py-1 text-sm font-semibold text-emerald-800">
                                {payload.attempt.score_scale.toFixed(1)} / 5
                            </span>
                        ) : null}
                    </div>
                </div>

                {!payload.attempt.can_review && payload.attempt.submitted ? (
                    <div className="mt-5 rounded-2xl border border-amber-200 bg-amber-50 px-4 py-4 text-sm leading-6 text-amber-900">
                        {assignmentFeedbackMessage || 'Tu intento ya fue entregado. La retroalimentación todavía no está disponible.'}
                    </div>
                ) : null}

                {payload.attempt.can_review && payload.attempt.submitted ? (
                    <div className="mt-5 rounded-2xl border border-emerald-200 bg-emerald-50 px-4 py-4 text-sm leading-6 text-emerald-900">
                        Ya puedes revisar tu resultado, la respuesta correcta y los conceptos relacionados.
                    </div>
                ) : null}

                {isStudyMode ? (
                    <div className="mt-5 rounded-2xl border border-blue-200 bg-blue-50 px-4 py-4 text-sm leading-6 text-blue-900">
                        Cada respuesta se verifica de inmediato para que puedas aprender mientras avanzas.
                    </div>
                ) : null}

                <div className="mt-6 flex flex-wrap gap-3">
                    {questions.map((question, index) => {
                        const evaluation = evaluationByQuestion[question.id];
                        const answered = Boolean(selectedByQuestion[question.id]);
                        const stateClass = evaluation
                            ? evaluation.is_correct
                                ? 'border-emerald-500 bg-emerald-50 text-emerald-700'
                                : 'border-rose-500 bg-rose-50 text-rose-700'
                            : answered
                            ? 'border-blue-500 bg-blue-50 text-blue-700'
                            : 'border-slate-200 bg-white text-slate-500';

                        return (
                            <button
                                key={question.id}
                                type="button"
                                onClick={() => setCurrentIndex(index)}
                                className={`h-11 min-w-11 shrink-0 rounded-2xl border px-3 text-sm font-bold transition ${stateClass} ${
                                    index === currentIndex ? 'shadow-lg shadow-slate-200' : ''
                                }`}
                            >
                                {index + 1}
                            </button>
                        );
                    })}
                </div>
            </article>

            <article className="rounded-[28px] border border-slate-200 bg-white p-6 shadow-[0_18px_42px_-30px_rgba(15,23,42,0.35)]">
                <div className="flex flex-wrap items-center justify-between gap-3">
                    <div>
                        <p className="text-sm font-black uppercase tracking-[0.2em] text-slate-500">Pregunta {currentIndex + 1} de {questions.length}</p>
                        <h4 className="mt-2 text-2xl font-black tracking-tight text-slate-950">
                            {isStudyMode ? 'Responde y verifica al instante' : 'Selecciona la mejor respuesta'}
                        </h4>
                    </div>
                    {showReviewForCurrentQuestion ? (
                        <span
                            className={`rounded-full px-3 py-1 text-sm font-semibold ${
                                currentEvaluation.is_correct
                                    ? 'border border-emerald-200 bg-emerald-50 text-emerald-800'
                                    : 'border border-rose-200 bg-rose-50 text-rose-800'
                            }`}
                        >
                            {currentEvaluation.is_correct ? 'Respuesta correcta' : isStudyMode ? 'Corrige este punto' : 'Revisión disponible'}
                        </span>
                    ) : null}
                </div>

                {currentQuestion.context_html || (currentQuestion.context_blocks?.length ?? 0) > 0 ? (
                    <div className="mt-6 rounded-3xl border border-slate-200 bg-slate-50 px-5 py-5">
                        <p className="mb-3 text-xs font-black uppercase tracking-[0.2em] text-slate-500">Contexto</p>
                        <RichContent blocks={currentQuestion.context_blocks} html={currentQuestion.context_html} />
                    </div>
                ) : null}

                <div className="mt-6">
                    <RichContent blocks={currentQuestion.stem_blocks} html={currentQuestion.stem_html} />
                </div>

                <div className="mt-8 grid gap-3">
                    {(currentQuestion.options ?? []).map((option) => {
                        const isSelected = selectedOptionId === option.id;
                        const isCorrectOption = currentEvaluation?.correct_option_id === option.id;
                        const isWrongSelected = Boolean(
                            payload.attempt.can_review &&
                                isSelected &&
                                currentEvaluation &&
                                currentEvaluation.correct_option_id &&
                                currentEvaluation.correct_option_id !== option.id,
                        );

                        const classes = payload.attempt.can_review
                            ? isCorrectOption
                                ? 'border-emerald-400 bg-emerald-50 text-emerald-900'
                                : isWrongSelected
                                ? 'border-rose-400 bg-rose-50 text-rose-900'
                                : isSelected
                                ? 'border-blue-400 bg-blue-50 text-blue-900'
                                : 'border-slate-200 bg-white text-slate-800'
                            : isSelected
                            ? 'border-blue-500 bg-blue-50 text-blue-900'
                            : 'border-slate-200 bg-white text-slate-800 hover:border-blue-200 hover:bg-blue-50';

                        return (
                            <button
                                key={option.id}
                                type="button"
                                disabled={!canAnswer || pendingQuestionId === currentQuestion.id}
                                onClick={() => void handleSelectOption(currentQuestion, option.id)}
                                className={`rounded-3xl border px-5 py-4 text-left text-base font-medium leading-7 transition ${classes} disabled:cursor-wait disabled:opacity-80`}
                            >
                                <div className="flex items-start gap-3">
                                    <span className="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-100 text-sm font-black text-slate-700">
                                        {option.id}
                                    </span>
                                    <div className="min-w-0 flex-1 text-current">
                                        <RichOptionContent option={option} />
                                    </div>
                                </div>
                            </button>
                        );
                    })}
                </div>

                {showReviewForCurrentQuestion ? (
                    <div className="mt-8 grid gap-4">
                        <section className="rounded-3xl border border-slate-200 bg-slate-50 px-5 py-5">
                            <p className="text-xs font-black uppercase tracking-[0.2em] text-slate-500">Retroalimentación</p>
                            <div className="mt-3">
                                <RichContent
                                    blocks={currentEvaluation.feedback_blocks}
                                    html={currentEvaluation.feedback_html}
                                />
                            </div>
                        </section>

                        <section className="rounded-3xl border border-slate-200 bg-slate-50 px-5 py-5">
                            <p className="text-xs font-black uppercase tracking-[0.2em] text-slate-500">Conceptos relacionados</p>
                            <div className="mt-3">
                                <RichContent
                                    blocks={currentEvaluation.concepts_blocks}
                                    html={currentEvaluation.concepts_html}
                                />
                            </div>
                        </section>
                    </div>
                ) : null}

                <div className="mt-8 flex flex-wrap items-center justify-between gap-3">
                    <div className="flex gap-3">
                        <button
                            type="button"
                            onClick={() => setCurrentIndex((value) => Math.max(value - 1, 0))}
                            disabled={currentIndex === 0}
                            className="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 disabled:cursor-not-allowed disabled:opacity-50"
                        >
                            Anterior
                        </button>
                        <button
                            type="button"
                            onClick={() => setCurrentIndex((value) => Math.min(value + 1, questions.length - 1))}
                            disabled={currentIndex === questions.length - 1}
                            className="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 disabled:cursor-not-allowed disabled:opacity-50"
                        >
                            Siguiente
                        </button>
                    </div>

                    {!payload.attempt.submitted && !isStudyMode ? (
                        <button
                            type="button"
                            onClick={() => void handleSubmitClick()}
                            disabled={submitting}
                            className="rounded-full bg-blue-600 px-5 py-3 text-sm font-bold text-white shadow-lg shadow-blue-500/25 transition hover:bg-blue-700 disabled:cursor-wait disabled:opacity-70"
                        >
                            {submitting ? 'Entregando…' : 'Entregar evaluación'}
                        </button>
                    ) : null}
                </div>
            </article>
        </section>
    );
}
