import renderMathInElement from 'katex/contrib/auto-render';
import { useEffect, useRef, useState } from 'react';

import type { AttemptOption } from '../types';

const MEMBERS_PUBLIC_ASSET_BASE_URL = String(import.meta.env.VITE_MEMBERS_PUBLIC_ASSET_BASE_URL ?? '').replace(/\/$/, '');

function useMathRenderer<TElement extends HTMLElement>(dependencies: Array<unknown>) {
    const ref = useRef<TElement | null>(null);

    useEffect(() => {
        if (!ref.current) {
            return;
        }

        renderMathInElement(ref.current, {
            delimiters: [
                { left: '$$', right: '$$', display: true },
                { left: '$', right: '$', display: false },
            ],
            throwOnError: false,
        });

        return undefined;
    }, dependencies);

    return ref;
}

function renderMathMarkup(markup: string): string {
    const normalized = String(markup || '').trim();

    if (normalized === '' || typeof document === 'undefined') {
        return normalized;
    }

    const scope = document.createElement('div');
    scope.innerHTML = normalized;

    renderMathInElement(scope, {
        delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
        ],
        throwOnError: false,
    });

    return scope.innerHTML;
}

export function resolveAssetUrl(src: string): string {
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

export function rewriteHtmlAssetUrls(html: string): string {
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
        n: 'ⁿ',
        i: 'ⁱ',
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
                return (
                    <mark key={key} className="rounded bg-amber-200/70 px-1">
                        {text}
                    </mark>
                );
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
                <MathHtml
                    key={key}
                    html={`$$${String(block.latex ?? '')}$$`}
                    className="overflow-x-auto rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 [&_.katex-display]:overflow-x-auto [&_.katex-display]:py-2"
                />
            );
        }

        if (block?.type === 'html' && block.html) {
            return <MathHtml key={key} html={String(block.html)} className="prose max-w-none" />;
        }

        return null;
    });
}

const richContentClassName =
    'prose prose-slate max-w-none [&_.table-scroll-wrapper]:overflow-x-auto [&_.table-scroll-wrapper]:rounded-2xl [&_.table-scroll-wrapper]:border [&_.table-scroll-wrapper]:border-slate-200 [&_.table-scroll-wrapper]:bg-white [&_img]:h-auto [&_img]:max-w-full [&_img]:rounded-2xl [&_img]:border [&_img]:border-slate-200 [&_table]:w-full [&_table]:min-w-max [&_table]:border-collapse [&_td]:border [&_td]:border-slate-200 [&_td]:px-4 [&_td]:py-3 [&_th]:border [&_th]:border-slate-200 [&_th]:bg-slate-100 [&_th]:px-4 [&_th]:py-3 [&_ul]:pl-6 [&_ol]:pl-6 [&_.katex-display]:overflow-x-auto [&_.katex-display]:py-2';

function MathHtml({ html, className }: { html: string; className: string }) {
    const [renderedHtml, setRenderedHtml] = useState(() => renderMathMarkup(rewriteHtmlAssetUrls(html)));

    useEffect(() => {
        setRenderedHtml(renderMathMarkup(rewriteHtmlAssetUrls(html)));
    }, [html]);

    return <div className={className} dangerouslySetInnerHTML={{ __html: renderedHtml }} />;
}

export function RichContent({
    blocks,
    html,
    className,
}: {
    blocks?: Array<Record<string, any>>;
    html?: string;
    className?: string;
}) {
    const scopeRef = useMathRenderer<HTMLDivElement>([html, JSON.stringify(blocks ?? [])]);

    if (html && html.trim() !== '') {
        return <MathHtml html={html} className={className ?? richContentClassName} />;
    }

    if (hasRenderableBlocks(blocks)) {
        return (
            <div ref={scopeRef} className={className ?? 'space-y-4'}>
                {renderBlocks(blocks ?? [])}
            </div>
        );
    }

    return null;
}

export function RichOptionContent({ option }: { option: AttemptOption }) {
    const html = normalizeOptionHtml(String(option.text_html ?? ''));
    const inlineScopeRef = useMathRenderer<HTMLSpanElement>([html, option.text]);

    if (html !== '') {
        return (
            <MathHtml
                html={html}
                className="prose prose-slate max-w-none text-inherit [&_.table-scroll-wrapper]:overflow-x-auto [&_.table-scroll-wrapper]:rounded-2xl [&_.table-scroll-wrapper]:border [&_.table-scroll-wrapper]:border-current/10 [&_.table-scroll-wrapper]:bg-white/70 [&_img]:h-auto [&_img]:max-w-full [&_img]:rounded-2xl [&_img]:border [&_img]:border-current/10 [&_img]:bg-white [&_p]:my-0 [&_strong]:text-inherit [&_em]:text-inherit [&_.katex-display]:overflow-x-auto [&_.katex-display]:py-2"
            />
        );
    }

    return (
        <span ref={inlineScopeRef}>
            {presentInlineText(option.text)}
        </span>
    );
}
