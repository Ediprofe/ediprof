import MembersLayout from '../../../Layouts/MembersLayout';
import type { NavItem } from '../../../types';

type LoginProps = {
    pageTitle: string;
    subtitle?: string;
    google_login_available: boolean;
};

export default function Login({ pageTitle, subtitle, google_login_available }: LoginProps) {
    const navigation: NavItem[] = [];

    return (
        <MembersLayout title={pageTitle} subtitle={subtitle} navigation={navigation}>
            <section className="mx-auto grid w-full max-w-2xl gap-6">
                <article className="rounded-[28px] border border-slate-200 bg-white p-8 shadow-[0_18px_42px_-30px_rgba(15,23,42,0.35)]">
                    <p className="text-sm font-black uppercase tracking-[0.22em] text-blue-600">Acceso web</p>
                    <h2 className="mt-4 text-3xl font-black tracking-tight text-slate-950">Ingresa a tu panel de estudiante</h2>
                    <p className="mt-3 text-base leading-7 text-slate-600">
                        Esta nueva app web de miembros usará sesión de Laravel para dejar estable la navegación y preparar el camino hacia móvil.
                    </p>

                    <div className="mt-8 rounded-3xl border border-slate-200 bg-slate-50 p-5">
                        <p className="text-sm font-semibold text-slate-700">
                            Usa tu cuenta de Google para abrir evaluaciones, talleres y simulacros asociados a tus cursos.
                        </p>

                        <a
                            href={google_login_available ? '/miembros-v2/auth/google/redirect' : '#'}
                            className={`mt-5 inline-flex rounded-full px-5 py-3 text-sm font-bold no-underline transition ${
                                google_login_available
                                    ? 'bg-blue-600 text-white shadow-lg shadow-blue-500/25 hover:bg-blue-700'
                                    : 'cursor-not-allowed border border-slate-200 bg-white text-slate-400'
                            }`}
                        >
                            Continuar con Google
                        </a>

                        {!google_login_available ? (
                            <p className="mt-4 text-sm leading-6 text-amber-700">
                                Falta completar `GOOGLE_CLIENT_SECRET` y `GOOGLE_REDIRECT_URI` para habilitar el acceso web en este entorno.
                            </p>
                        ) : null}
                    </div>
                </article>
            </section>
        </MembersLayout>
    );
}
