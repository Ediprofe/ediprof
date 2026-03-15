import { Link } from '@inertiajs/react';

import MembersLayout from '../../../Layouts/MembersLayout';
import type { MemberAssignment, NavItem } from '../../../types';

type SimulacrosIndexProps = {
    pageTitle: string;
    subtitle?: string;
    items: MemberAssignment[];
};

export default function SimulacrosIndex({ pageTitle, subtitle, items }: SimulacrosIndexProps) {
    const navigation: NavItem[] = [
        { label: 'Panel', href: '/miembros-v2' },
        { label: 'Evaluaciones', href: '/miembros-v2/evaluaciones' },
        { label: 'Talleres', href: '/miembros-v2/talleres' },
        { label: 'Simulacros', href: '/miembros-v2/simulacros', active: true },
    ];

    return (
        <MembersLayout title={pageTitle} subtitle={subtitle} navigation={navigation}>
            <section className="rounded-[28px] border border-slate-200 bg-white p-6 shadow-[0_18px_42px_-30px_rgba(15,23,42,0.35)]">
                <div className="grid gap-4">
                    {items.map((item) => (
                        <article
                            key={item.id}
                            className="grid gap-4 rounded-[24px] border border-slate-200 bg-slate-50 px-5 py-5 md:grid-cols-[minmax(0,1fr)_auto] md:items-center"
                        >
                            <div className="space-y-2">
                                <div className="flex flex-wrap items-center gap-2">
                                    <span className="rounded-full border border-fuchsia-200 bg-fuchsia-50 px-3 py-1 text-xs font-black uppercase tracking-[0.2em] text-fuchsia-700">
                                        Simulacro
                                    </span>
                                    <span className="rounded-full border border-slate-200 bg-white px-3 py-1 text-xs font-semibold text-slate-600">
                                        {item.latest_attempt?.feedback_state_label ?? item.availability.state}
                                    </span>
                                </div>
                                <h2 className="text-2xl font-black tracking-tight text-slate-950">{item.title}</h2>
                                <p className="text-sm text-slate-600">
                                    {item.stats.effective_questions} preguntas · {item.course?.name ?? 'Curso sin asignar'} · {item.feedback.policy_label}
                                </p>
                            </div>

                            <div className="flex items-center gap-3">
                                <Link
                                    href={`/miembros-v2/simulacros/${item.id}`}
                                    className="rounded-full bg-fuchsia-600 px-5 py-3 text-sm font-bold text-white no-underline shadow-lg shadow-fuchsia-500/25 transition hover:bg-fuchsia-700"
                                >
                                    Abrir simulacro
                                </Link>
                            </div>
                        </article>
                    ))}
                    {items.length === 0 ? (
                        <div className="rounded-[24px] border border-dashed border-slate-300 bg-slate-50 px-5 py-6 text-sm leading-6 text-slate-600">
                            No hay simulacros visibles en este momento.
                        </div>
                    ) : null}
                </div>
            </section>
        </MembersLayout>
    );
}
