import { Link } from '@inertiajs/react';

import MembersLayout from '../../Layouts/MembersLayout';
import type { DashboardSection, NavItem, NextAction, QuickStat } from '../../types';

type DashboardProps = {
    pageTitle: string;
    subtitle?: string;
    quickStats: QuickStat[];
    nextActions: NextAction[];
    sections: DashboardSection[];
};

export default function Dashboard({ pageTitle, subtitle, quickStats, nextActions, sections }: DashboardProps) {
    const navigation: NavItem[] = [
        { label: 'Panel', href: '/miembros-v2', active: true },
        { label: 'Evaluaciones', href: '/miembros-v2/evaluaciones' },
        { label: 'Talleres', href: '/miembros-v2/talleres' },
        { label: 'Simulacros', href: '/miembros-v2/simulacros' },
    ];

    return (
        <MembersLayout title={pageTitle} subtitle={subtitle} navigation={navigation}>
            <section className="grid gap-6 lg:grid-cols-[minmax(0,2fr)_minmax(320px,1fr)]">
                <div className="grid gap-6">
                    <div className="grid gap-4 md:grid-cols-3">
                        {quickStats.map((stat) => (
                            <article
                                key={stat.label}
                                className="rounded-[24px] border border-slate-200 bg-white px-6 py-5 shadow-[0_14px_36px_-28px_rgba(15,23,42,0.35)]"
                            >
                                <p className="text-sm font-bold uppercase tracking-[0.18em] text-slate-500">{stat.label}</p>
                                <p className="mt-3 text-4xl font-black tracking-tight text-slate-950">{stat.value}</p>
                            </article>
                        ))}
                    </div>

                    <section className="rounded-[28px] border border-slate-200 bg-white p-6 shadow-[0_18px_42px_-30px_rgba(15,23,42,0.35)]">
                        <div className="mb-5 flex flex-wrap items-center justify-between gap-3">
                            <div>
                                <p className="text-sm font-black uppercase tracking-[0.22em] text-blue-600">Próximo por hacer</p>
                                <h2 className="text-2xl font-black tracking-tight text-slate-950">Evaluaciones más cercanas en tu cuenta</h2>
                            </div>
                            <span className="rounded-full border border-slate-200 bg-slate-50 px-3 py-1 text-sm font-semibold text-slate-600">
                                Datos reales desde Laravel
                            </span>
                        </div>

                        <div className="grid gap-4">
                            {nextActions.length === 0 ? (
                                <div className="rounded-[24px] border border-dashed border-slate-300 bg-slate-50 px-5 py-6 text-sm leading-6 text-slate-600">
                                    Todavía no hay evaluaciones activas para tu cuenta. Cuando el docente publique una, aparecerá aquí.
                                </div>
                            ) : null}

                            {nextActions.map((card) => (
                                <Link
                                    key={card.id}
                                    href={card.href}
                                    className="group rounded-[24px] border border-slate-200 bg-gradient-to-br from-white to-slate-50 px-5 py-5 no-underline shadow-[0_14px_36px_-30px_rgba(15,23,42,0.4)] transition hover:-translate-y-0.5 hover:border-blue-200 hover:shadow-[0_18px_40px_-28px_rgba(37,99,235,0.35)]"
                                >
                                    <div className="flex flex-wrap items-center gap-2">
                                        <span className="rounded-full border border-blue-200 bg-blue-50 px-3 py-1 text-xs font-black uppercase tracking-[0.2em] text-blue-700">
                                            Evaluación
                                        </span>
                                        <span className="rounded-full border border-slate-200 bg-white px-3 py-1 text-xs font-semibold text-slate-600">
                                            {card.status}
                                        </span>
                                    </div>
                                    <h3 className="mt-4 text-xl font-bold tracking-tight text-slate-950">{card.title}</h3>
                                    <p className="mt-2 text-sm leading-6 text-slate-600">{card.questions} preguntas configuradas en esta evaluación.</p>
                                    <p className="mt-4 text-sm font-semibold text-blue-600">Abrir sección →</p>
                                </Link>
                            ))}
                        </div>
                    </section>
                </div>

                <aside className="grid gap-6">
                    <section className="rounded-[28px] border border-slate-200 bg-white p-6 shadow-[0_18px_42px_-30px_rgba(15,23,42,0.35)]">
                        <p className="text-sm font-black uppercase tracking-[0.2em] text-emerald-600">Secciones</p>
                        <div className="mt-5 space-y-4">
                            {sections.map((item) => (
                                <Link
                                    key={item.title}
                                    href={item.href}
                                    className="block rounded-2xl border border-slate-200 bg-slate-50 px-4 py-4 no-underline transition hover:border-blue-200 hover:bg-blue-50"
                                >
                                    <div className="flex items-center justify-between gap-3">
                                        <p className="text-base font-bold text-slate-950">
                                            <span className="mr-2">{item.emoji}</span>
                                            {item.title}
                                        </p>
                                        <span className="rounded-full border border-slate-200 bg-white px-3 py-1 text-xs font-bold text-slate-600">
                                            {item.count}
                                        </span>
                                    </div>
                                    <p className="mt-2 text-sm leading-6 text-slate-700">{item.description}</p>
                                </Link>
                            ))}
                        </div>
                    </section>
                </aside>
            </section>
        </MembersLayout>
    );
}
