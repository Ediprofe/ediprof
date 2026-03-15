import { useEffect, useMemo, useState } from 'react';

import type { AttemptEvaluation, AttemptOption, AttemptPayload, AttemptQuestion } from '../types';

const MEMBERS_PUBLIC_ASSET_BASE_URL = String(import.meta.env.VITE_MEMBERS_PUBLIC_ASSET_BASE_URL ?? '').replace(/\/$/, '');

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

function resolveAssetUrl(src: string): string {
    const normalized = String(src || '').trim();

    if (
        normalized === '' ||
        /^https?:\/\//i.test(normalized) ||
        normalized.startsWith('data:') ||
        normalized.startsWith('blob:')
    ) {
        return normalized;
    }

    if (
        normalized.startsWith('/images/') ||
        normalized.startsWith('/ilustraciones/') ||
        normalized.startsWith('/illustrations/')
    ) {
        return MEMBERS_PUBLIC_ASSET_BASE_URL !== '' ? `${MEMBERS_PUBLIC_ASSET_BASE_URL}${normalized}` : normalized;
    }

    return normalized;
}

function rewriteHtmlAssetUrls(html: string): string {
    return String(html || '').replace(
        /\b(src|href)=["'](\/(?:images|ilustraciones|illustrations)\/[^"']+)["']/gi,
        (_match, attribute, path) => `${attribute}="${resolveAssetUrl(String(path))}"`,
    );
}

function normalizeOptionHtml(html: string): string {
    const rewritten = rewriteHtmlAssetUrls(html).trim();

    if (rewritten === '') {
        return '';
    }

    if (/^<p>[\s\S]*<\/p>$/.test(rewritten) && !rewritten.includes('</p><')) {
        return rewritten.replace(/^<p>/, '').replace(/<\/p>$/, '');
    }

    return rewritten;
}

function normalizeInlineText(value: string): string {
    return String(value || '')
        .replace(/\$([^$]+)\$/g, '$1')
        .replace(/\*\*([^*]+)\*\*/g, '$1')
        .replace(/==([^=]+)==/g, '$1')
        .replace(/~~([^~]+)~~/g, '$1')
        .replace(/\\times/g, '×')
        .replace(/\\cdot/g, '·')
        .replace(/\\rightarrow/g, '→')
        .replace(/\\left|\\right/g, '');
}

function toSuperscript(value: string): string {
    const map: Record<string, string> = {
        '0': '⁰',
        '1': '¹',
        '2': '²',
        '3': '³',
        '4': '⁴',
        '5': '⁵',
        '6': '⁶',
        '7': '⁷',
        '8': '⁸',
        '9': '⁹',
        '+': '⁺',
        '-': '⁻',
        '=': '⁼',
        '(': '⁽',
        ')': '⁾',
        'n': 'ⁿ',
        'i': 'ⁱ',
    };

    return String(value || '')
        .split('')
        .map((char) => map[char] ?? char)
        .join('');
}

function presentInlineText(value: string): string {
    return normalizeInlineText(value)
        .replace(/([A-Za-z0-9\)])\^\\?\{([^}]+)\}/g, (_match, base, exponent) => `${base}${toSuperscript(exponent)}`)
        .replace(/([A-Za-z0-9\)])\^([+\-=\d()ni]+)/g, (_match, base, exponent) => `${base}${toSuperscript(exponent)}`)
        .replace(/\s+/g, ' ')
        .trim();
}

function hasRenderableBlocks(blocks: Array<Record<string, any>> = []): boolean {
    return Array.isArray(blocks) && blocks.some((block) => block && typeof block === 'object');
}

function renderInlineNodes(inlines: Array<Record<string, any>> = [], keyPrefix = 'seg') {
    return inlines.map((segment, index) => {
        const text = String(segment?.text ?? '');
        const key = `${keyPrefix}-${index}`;

        switch (segment?.variant) {
            case 'bold':
                return <strong key={key}>{text}</strong>;
            case 'italic':
                return <em key={key}>{text}</em>;
            case 'highlight':
                return <mark key={key} className="rounded bg-amber-200/70 px-1">{text}</mark>;
            case 'strike':
                return <del key={key}>{text}</del>;
            default:
                return <span key={key}>{text}</span>;
        }
    });
}

function renderBlocks(blocks: Array<Record<string, any>>, keyPrefix = 'block') {
    return blocks.map((block, index) => {
        const key = `${keyPrefix}-${index}`;
        const text = String(block?.text ?? '');

        if (block?.type === 'heading') {
            const Tag = block.depth === 2 ? 'h2' : block.depth === 4 ? 'h4' : 'h3';
            return (
                <Tag key={key} className="text-xl font-black tracking-tight text-slate-950">
                    {Array.isArray(block.inlines) ? renderInlineNodes(block.inlines, `${key}-inline`) : text}
                </Tag>
            );
        }

        if (block?.type === 'paragraph') {
            return (
                <p key={key} className="text-base leading-8 text-slate-800">
                    {Array.isArray(block.inlines) && block.inlines.length > 0
                        ? renderInlineNodes(block.inlines, `${key}-inline`)
                        : text}
                </p>
            );
        }

        if (block?.type === 'image' && block.src) {
            return (
                <figure key={key} className="overflow-x-auto">
                    <img
                        src={resolveAssetUrl(String(block.src))}
                        alt={String(block.alt || 'Recurso visual')}
                        className="h-auto max-w-full rounded-2xl border border-slate-200 bg-white"
                    />
                </figure>
            );
        }

        if (block?.type === 'table' && Array.isArray(block.rows) && block.rows.length > 0) {
            const [header, ...body] = block.rows;

            return (
                <div key={key} className="overflow-x-auto rounded-2xl border border-slate-200 bg-white">
                    <table className="min-w-full border-collapse text-left text-sm">
                        <thead className="bg-slate-100 text-slate-700">
                            <tr>
                                {(header || []).map((cell: string, cellIndex: number) => (
                                    <th key={`${key}-head-${cellIndex}`} className="border-b border-slate-200 px-4 py-3 font-semibold">
                                        {cell}
                                    </th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {body.map((row: string[], rowIndex: number) => (
                                <tr key={`${key}-row-${rowIndex}`} className="odd:bg-white even:bg-slate-50">
                                    {(row || []).map((cell: string, cellIndex: number) => (
                                        <td key={`${key}-cell-${rowIndex}-${cellIndex}`} className="border-b border-slate-200 px-4 py-3 text-slate-800">
                                            {cell}
                                        </td>
                                    ))}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            );
        }

        if (block?.type === 'list' && Array.isArray(block.items) && block.items.length > 0) {
            const Tag = block.ordered ? 'ol' : 'ul';

            return (
                <Tag key={key} className="space-y-2 pl-6 text-base leading-8 text-slate-800">
                    {block.items.map((item: Record<string, any>, itemIndex: number) => (
                        <li key={`${key}-item-${itemIndex}`}>
                            {Array.isArray(item?.inlines) && item.inlines.length > 0
                                ? renderInlineNodes(item.inlines, `${key}-item-inline-${itemIndex}`)
                                : String(item?.text ?? '')}
                        </li>
                    ))}
                </Tag>
            );
        }

        if (block?.type === 'equation') {
            return (
                <pre key={key} className="overflow-x-auto rounded-2xl border border-slate-200 bg-slate-950 px-4 py-3 text-sm text-slate-100">
                    {String(block.latex ?? '')}
                </pre>
            );
        }

        if (block?.type === 'html' && block.html) {
            return <div key={key} className="prose max-w-none" dangerouslySetInnerHTML={{ __html: String(block.html) }} />;
        }

        return null;
    });
}

function RichContent({
    blocks,
    html,
}: {
    blocks?: Array<Record<string, any>>;
    html?: string;
}) {
    if (html && html.trim() !== '') {
        return (
            <div
                className="prose prose-slate max-w-none [&_.table-scroll-wrapper]:overflow-x-auto [&_.table-scroll-wrapper]:rounded-2xl [&_.table-scroll-wrapper]:border [&_.table-scroll-wrapper]:border-slate-200 [&_.table-scroll-wrapper]:bg-white [&_img]:h-auto [&_img]:max-w-full [&_img]:rounded-2xl [&_img]:border [&_img]:border-slate-200 [&_table]:w-full [&_table]:min-w-max [&_table]:border-collapse [&_td]:border [&_td]:border-slate-200 [&_td]:px-4 [&_td]:py-3 [&_th]:border [&_th]:border-slate-200 [&_th]:bg-slate-100 [&_th]:px-4 [&_th]:py-3 [&_ul]:pl-6 [&_ol]:pl-6 [&_.katex-display]:overflow-x-auto [&_.katex-display]:py-2"
                dangerouslySetInnerHTML={{ __html: rewriteHtmlAssetUrls(html) }}
            />
        );
    }

    if (hasRenderableBlocks(blocks)) {
        return <div className="space-y-4">{renderBlocks(blocks ?? [])}</div>;
    }

    return null;
}

function RichOptionContent({ option }: { option: AttemptOption }) {
    const html = normalizeOptionHtml(String(option.text_html ?? ''));

    if (html !== '') {
        return (
            <div
                className="prose prose-slate max-w-none text-inherit [&_.table-scroll-wrapper]:overflow-x-auto [&_.table-scroll-wrapper]:rounded-2xl [&_.table-scroll-wrapper]:border [&_.table-scroll-wrapper]:border-current/10 [&_.table-scroll-wrapper]:bg-white/70 [&_img]:h-auto [&_img]:max-w-full [&_img]:rounded-2xl [&_img]:border [&_img]:border-current/10 [&_img]:bg-white [&_p]:my-0 [&_strong]:text-inherit [&_em]:text-inherit [&_.katex-display]:overflow-x-auto [&_.katex-display]:py-2"
                dangerouslySetInnerHTML={{ __html: html }}
            />
        );
    }

    return <span>{presentInlineText(option.text)}</span>;
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

                {currentQuestion.context_html || hasRenderableBlocks(currentQuestion.context_blocks) ? (
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
