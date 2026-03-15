import { Head, Link } from '@inertiajs/react';

import { RichContent, RichOptionContent } from '../../../Components/RichContent';
import type { AttemptOption } from '../../../types';

type DraftPreviewContext = {
    id: string;
    title: string;
    context_html?: string;
    context_blocks?: Array<Record<string, any>>;
};

type DraftPreviewQuestion = {
    id: string;
    order: number;
    stem_html?: string;
    stem_blocks?: Array<Record<string, any>>;
    feedback_html?: string;
    feedback_blocks?: Array<Record<string, any>>;
    concepts_html?: string;
    concepts_blocks?: Array<Record<string, any>>;
    correct_option_id?: string | null;
    options: AttemptOption[];
    contexts: DraftPreviewContext[];
};

type DraftPreview = {
    id: number;
    external_id: string;
    title: string;
    status: string;
    subject_label?: string | null;
    unit_label?: string | null;
    origin_type?: string | null;
    origin_label?: string | null;
    question_count: number;
    context_count: number;
    questions: DraftPreviewQuestion[];
};

type DraftPreviewPageProps = {
    pageTitle: string;
    subtitle?: string;
    backHref: string;
    draft: DraftPreview;
};

export default function AssessmentDraftPreview({ pageTitle, subtitle, backHref, draft }: DraftPreviewPageProps) {
    return (
        <>
            <Head title={pageTitle} />

            <div className="min-h-screen bg-[radial-gradient(circle_at_top_left,_rgba(37,99,235,0.16),_transparent_32%),linear-gradient(180deg,_#f8fbff_0%,_#eef4ff_36%,_#f8fafc_100%)] text-slate-900">
                <main className="mx-auto grid max-w-7xl gap-6 px-4 py-6 sm:px-6">
                    <section className="rounded-[28px] border border-white/70 bg-white/90 px-6 py-6 shadow-[0_25px_60px_-35px_rgba(15,23,42,0.35)] sm:px-7">
                        <div className="flex flex-wrap items-start justify-between gap-4">
                            <div className="space-y-3">
                                <p className="text-sm font-black uppercase tracking-[0.24em] text-blue-600">Preview web real</p>
                                <div className="space-y-2">
                                    <h1 className="text-3xl font-black tracking-tight text-slate-950 sm:text-4xl">{draft.title}</h1>
                                    {subtitle ? <p className="max-w-3xl text-base leading-7 text-slate-600 sm:text-lg sm:leading-8">{subtitle}</p> : null}
                                </div>
                                <div className="flex flex-wrap gap-2">
                                    <span className="rounded-full border border-slate-200 bg-slate-50 px-3 py-1 text-sm font-semibold text-slate-700">
                                        {draft.external_id}
                                    </span>
                                    {draft.subject_label ? (
                                        <span className="rounded-full border border-blue-200 bg-blue-50 px-3 py-1 text-sm font-semibold text-blue-800">
                                            Materia · {draft.subject_label}
                                        </span>
                                    ) : null}
                                    {draft.unit_label ? (
                                        <span className="rounded-full border border-slate-200 bg-slate-50 px-3 py-1 text-sm font-semibold text-slate-700">
                                            Unidad · {draft.unit_label}
                                        </span>
                                    ) : null}
                                    {draft.origin_type || draft.origin_label ? (
                                        <span className="rounded-full border border-amber-200 bg-amber-50 px-3 py-1 text-sm font-semibold text-amber-800">
                                            Origen · {draft.origin_type ?? 'sin tipo'}{draft.origin_label ? ` · ${draft.origin_label}` : ''}
                                        </span>
                                    ) : null}
                                    <span className="rounded-full border border-slate-200 bg-slate-50 px-3 py-1 text-sm font-semibold text-slate-700">
                                        {draft.question_count} pregunta(s)
                                    </span>
                                    <span className="rounded-full border border-slate-200 bg-slate-50 px-3 py-1 text-sm font-semibold text-slate-700">
                                        {draft.context_count} contexto(s)
                                    </span>
                                    <span className="rounded-full border border-amber-200 bg-amber-50 px-3 py-1 text-sm font-semibold text-amber-800">
                                        {draft.status}
                                    </span>
                                </div>
                            </div>

                            <div className="flex flex-wrap gap-3">
                                <Link
                                    href={backHref}
                                    className="rounded-full border border-slate-200 bg-white px-5 py-3 text-sm font-bold text-slate-700 no-underline shadow-sm"
                                >
                                    Volver al creador IA
                                </Link>
                                <a
                                    href="/admin"
                                    className="rounded-full bg-blue-600 px-5 py-3 text-sm font-bold text-white no-underline shadow-lg shadow-blue-500/25"
                                >
                                    Volver al panel
                                </a>
                            </div>
                        </div>
                    </section>

                    {draft.questions.map((question) => (
                        <article key={question.id} className="rounded-[28px] border border-slate-200 bg-white p-6 shadow-[0_18px_42px_-30px_rgba(15,23,42,0.35)]">
                            <div className="flex flex-wrap items-center gap-3">
                                <span className="rounded-full bg-blue-50 px-4 py-2 text-sm font-black uppercase tracking-[0.2em] text-blue-700">
                                    {question.id}
                                </span>
                                <strong className="text-2xl font-black tracking-tight text-slate-950">Pregunta {question.order}</strong>
                            </div>

                            {question.contexts.length > 0 ? (
                                <div className="mt-6 grid gap-4">
                                    {question.contexts.map((context) => (
                                        <section key={`${question.id}-${context.id}`} className="rounded-3xl border border-slate-200 bg-slate-50 px-5 py-5">
                                            <p className="mb-3 text-xs font-black uppercase tracking-[0.2em] text-slate-500">
                                                {context.title}
                                            </p>
                                            <RichContent html={context.context_html} blocks={context.context_blocks} />
                                        </section>
                                    ))}
                                </div>
                            ) : null}

                            <section className="mt-6">
                                <p className="mb-3 text-xs font-black uppercase tracking-[0.2em] text-slate-500">Enunciado</p>
                                <RichContent html={question.stem_html} blocks={question.stem_blocks} />
                            </section>

                            <section className="mt-8">
                                <p className="mb-3 text-xs font-black uppercase tracking-[0.2em] text-slate-500">Opciones</p>
                                <div className="grid gap-3">
                                    {question.options.map((option) => (
                                        <div
                                            key={`${question.id}-${option.id}`}
                                            className={`rounded-3xl border px-5 py-4 ${
                                                option.is_correct
                                                    ? 'border-emerald-400 bg-emerald-50 text-emerald-900'
                                                    : 'border-slate-200 bg-white text-slate-800'
                                            }`}
                                        >
                                            <div className="flex items-start gap-3">
                                                <span className="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-100 text-sm font-black text-slate-700">
                                                    {option.id}
                                                </span>
                                                <div className="min-w-0 flex-1 text-current">
                                                    <RichOptionContent option={option} />
                                                </div>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </section>

                            {question.feedback_html || (question.feedback_blocks?.length ?? 0) > 0 ? (
                                <section className="mt-8 rounded-3xl border border-amber-200 bg-amber-50 px-5 py-5">
                                    <p className="mb-3 text-xs font-black uppercase tracking-[0.2em] text-amber-700">Retroalimentación</p>
                                    <RichContent html={question.feedback_html} blocks={question.feedback_blocks} />
                                </section>
                            ) : null}

                            {question.concepts_html || (question.concepts_blocks?.length ?? 0) > 0 ? (
                                <section className="mt-4 rounded-3xl border border-blue-200 bg-blue-50 px-5 py-5">
                                    <p className="mb-3 text-xs font-black uppercase tracking-[0.2em] text-blue-700">Conceptos relacionados</p>
                                    <RichContent html={question.concepts_html} blocks={question.concepts_blocks} />
                                </section>
                            ) : null}
                        </article>
                    ))}
                </main>
            </div>
        </>
    );
}
