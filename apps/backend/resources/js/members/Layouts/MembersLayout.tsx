import { Head, Link, router, usePage } from '@inertiajs/react';
import type { PropsWithChildren, ReactNode } from 'react';

import type { NavItem, SharedPageProps } from '../types';

type MembersLayoutProps = PropsWithChildren<{
    title: string;
    subtitle?: string;
    navigation: NavItem[];
    headerSlot?: ReactNode;
}>;

export default function MembersLayout({ title, subtitle, navigation, headerSlot, children }: MembersLayoutProps) {
    const {
        auth: { user },
        flash,
    } = usePage<SharedPageProps>().props;

    return (
        <>
            <Head title={title} />

            <div className="min-h-screen bg-[radial-gradient(circle_at_top_left,_rgba(37,99,235,0.16),_transparent_32%),linear-gradient(180deg,_#f8fbff_0%,_#eef4ff_36%,_#f8fafc_100%)] text-slate-900">
                <header className="sticky top-0 z-40 border-b border-slate-200/80 bg-white/92 backdrop-blur">
                    <div className="mx-auto max-w-7xl px-4 py-4 sm:px-6">
                        <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
                            <div className="flex min-w-0 items-center gap-3">
                                <Link href="/miembros-v2" className="flex items-center gap-3 text-slate-950 no-underline">
                                    <span className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-gradient-to-br from-blue-600 to-indigo-500 text-2xl text-white shadow-lg shadow-blue-500/25">
                                        🎓
                                    </span>
                                    <span className="grid min-w-0 leading-none">
                                        <strong className="truncate text-xl tracking-tight">Ediprofe</strong>
                                        <span className="text-sm font-bold uppercase tracking-[0.2em] text-slate-500">Miembros</span>
                                    </span>
                                </Link>
                            </div>

                            <div className="flex flex-col gap-3 sm:flex-row sm:flex-wrap sm:items-center sm:justify-end">
                                {user ? (
                                    <div className="max-w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-left sm:max-w-md sm:text-right">
                                        <p className="truncate text-sm font-bold text-slate-950">{user.display_name || user.name}</p>
                                        <p className="truncate text-xs text-slate-500">{user.email}</p>
                                    </div>
                                ) : null}
                                {headerSlot}
                                {user ? (
                                    <button
                                        type="button"
                                        onClick={() => router.post('/miembros-v2/logout')}
                                        className="rounded-full border border-slate-200 bg-white px-4 py-2 text-sm font-semibold text-slate-700 shadow-sm transition hover:border-red-200 hover:bg-red-50 hover:text-red-700"
                                    >
                                        Cerrar sesión
                                    </button>
                                ) : null}
                            </div>
                        </div>

                        <div className="mt-4 overflow-x-auto pb-1">
                            <nav className="flex min-w-max items-center gap-3">
                                {navigation.map((item) => (
                                    <Link
                                        key={item.href}
                                        href={item.href}
                                        className={`rounded-full border px-4 py-2 text-sm font-semibold no-underline transition ${
                                            item.active
                                                ? 'border-blue-600 bg-blue-600 text-white shadow-lg shadow-blue-500/25'
                                                : 'border-slate-200 bg-slate-100/90 text-slate-700 hover:border-blue-200 hover:bg-blue-50 hover:text-blue-700'
                                        }`}
                                    >
                                        {item.label}
                                    </Link>
                                ))}
                            </nav>
                        </div>
                    </div>
                </header>

                <main className="mx-auto grid max-w-7xl gap-6 px-4 py-6 sm:px-6">
                    {flash.success ? (
                        <section className="rounded-2xl border border-emerald-200 bg-emerald-50 px-5 py-4 text-sm font-medium text-emerald-900">
                            {flash.success}
                        </section>
                    ) : null}
                    {flash.error ? (
                        <section className="rounded-2xl border border-rose-200 bg-rose-50 px-5 py-4 text-sm font-medium text-rose-900">
                            {flash.error}
                        </section>
                    ) : null}

                    <section className="rounded-[28px] border border-white/70 bg-white/88 px-6 py-6 shadow-[0_25px_60px_-35px_rgba(15,23,42,0.35)] sm:px-7">
                        <div className="space-y-3">
                            <p className="text-sm font-black uppercase tracking-[0.24em] text-blue-600">Zona de miembros</p>
                            <div className="space-y-2">
                                <h1 className="text-3xl font-black tracking-tight text-slate-950 sm:text-4xl lg:text-5xl">{title}</h1>
                                {subtitle ? <p className="max-w-3xl text-base leading-7 text-slate-600 sm:text-lg sm:leading-8">{subtitle}</p> : null}
                            </div>
                        </div>
                    </section>

                    {children}
                </main>
            </div>
        </>
    );
}
