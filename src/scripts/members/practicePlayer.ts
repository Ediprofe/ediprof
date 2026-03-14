import {
  cleanInlineForRender,
  cleanInlineMarkdown,
  normalizeMathForDisplay,
  parseInlineSegments,
} from './workshopRender';

type PracticeMode = 'study' | 'exam';
type ContentType = 'taller' | 'simulacro' | 'assignment';

type MemberUser = {
  id: number;
  role?: string;
  member_status?: string;
};

type PracticeOption = {
  id: string;
  text: string;
  is_correct?: boolean;
};

type PracticeQuestion = {
  id: string;
  order?: number;
  stem_mdx?: string;
  stem_html?: string;
  stem_blocks?: Array<Record<string, any>>;
  context_mdx?: string;
  context_html?: string;
  context_blocks?: Array<Record<string, any>>;
  options?: PracticeOption[];
  correct_option_id?: string | null;
  feedback_mdx?: string;
  feedback_html?: string;
  feedback_summary?: string | null;
  feedback_blocks?: Array<Record<string, any>>;
  concepts_mdx?: string;
  concepts_html?: string;
  concepts_summary?: string | null;
  concepts_blocks?: Array<Record<string, any>>;
};

type PracticeDetail = {
  id: string;
  content_external_id?: string;
  title: string;
  route?: string;
  area_slug?: string;
  unidad_slug?: string;
  content_type?: string;
  stats?: {
    total_questions?: number;
    total_assets?: number;
  };
  attempt?: {
    id: string;
    mode: string;
    status: string;
    submitted: boolean;
    can_review: boolean;
    total_questions: number;
    score_raw?: number | null;
    score_percent?: number | null;
    score_scale?: number | null;
    started_at?: string | null;
    submitted_at?: string | null;
    graded_at?: string | null;
    review_released_at?: string | null;
  };
  questions?: PracticeQuestion[];
  selected_by_question?: Record<string, string>;
  evaluation_by_question?: Record<string, EvaluationResult>;
};

type EvaluationResult = {
  question_id: string;
  selected_option_id: string;
  correct_option_id: string | null;
  is_correct: boolean;
  feedback_mdx?: string;
  feedback_html?: string;
  feedback_summary?: string | null;
  feedback_blocks?: Array<Record<string, any>>;
  concepts_mdx?: string;
  concepts_html?: string;
  concepts_summary?: string | null;
  concepts_blocks?: Array<Record<string, any>>;
};

type PracticePlayerOptions = {
  root: HTMLElement | null;
  feedback?: HTMLElement | null;
  resetButton?: HTMLButtonElement | null;
  contentId: string;
  contentType: ContentType;
  contentLabel: string;
  backHref: string;
  allowedModes: PracticeMode[];
  defaultMode?: PracticeMode;
  examContentName?: string;
  emptyMessage?: string;
  api: {
    getSessionToken: () => string | null;
    clearSession: () => void;
    saveSession: (token: string, user: MemberUser) => void;
    me: () => Promise<any>;
    startAttempt: (
      contentId: string,
      options?: { mode?: 'study' | 'simulacro' | 'evaluation' | 'exam'; reset?: boolean }
    ) => Promise<any>;
    getAttempt: (attemptId: string) => Promise<any>;
    answerAttempt: (attemptId: string, questionId: string, optionId: string) => Promise<any>;
    submitAttempt?: (attemptId: string) => Promise<any>;
  };
};

type PersistedProgress = {
  content_id: string;
  mode: PracticeMode;
  question_index: number;
  selected_by_question: Record<string, string>;
  evaluation_by_question: Record<string, EvaluationResult>;
  submitted: boolean;
  updated_at: number;
};

type PracticeState = {
  mode: PracticeMode;
  detail: PracticeDetail | null;
  detailHasAnswers: boolean;
  questionIndex: number;
  selectedByQuestion: Record<string, string>;
  evaluationByQuestion: Record<string, EvaluationResult>;
  submitted: boolean;
  currentUser: MemberUser | null;
  isLoading: boolean;
};

export function mountPracticePlayer(options: PracticePlayerOptions): void {
  if (!options.root) {
    return;
  }
  const root = options.root;

  const token = options.api.getSessionToken();
  if (!token) {
    window.location.href = '/miembros/login';
    return;
  }

  const state: PracticeState = {
    mode: options.defaultMode && options.allowedModes.includes(options.defaultMode)
      ? options.defaultMode
      : options.allowedModes[0] ?? 'study',
    detail: null,
    detailHasAnswers: false,
    questionIndex: 0,
    selectedByQuestion: {},
    evaluationByQuestion: {},
    submitted: false,
    currentUser: null,
    isLoading: true,
  };

  function getExamContentName(): string {
    return String(options.examContentName || 'simulacro').trim() || 'simulacro';
  }

  function getModeUiLabel(mode: PracticeMode): string {
    if (mode === 'study') {
      return 'Práctica guiada';
    }

    return getExamContentName() === 'evaluación' ? 'Evaluación' : 'Simulacro';
  }

  function getExamModeDescription(): string {
    return getExamContentName() === 'evaluación'
      ? '📝 <strong>Modo evaluación:</strong> responde todo y entrega al final.'
      : '⏱️ <strong>Modo simulacro:</strong> responde todo y entrega al final.';
  }

  const feedbackEl = options.feedback ?? null;
  const resetButton = options.resetButton ?? null;
  const modePreferenceKey = `ediprofe_member_practice_mode:${options.contentType}:${options.contentId}`;

  function getStorageKey(mode: PracticeMode): string | null {
    if (!state.currentUser) return null;
    return `ediprofe_member_practice:${state.currentUser.id}:${options.contentType}:${options.contentId}:${mode}`;
  }

  function safeParseJSON<T>(raw: string | null): T | null {
    if (!raw) return null;
    try {
      return JSON.parse(raw) as T;
    } catch {
      return null;
    }
  }

  function persistModePreference(): void {
    window.localStorage.setItem(modePreferenceKey, state.mode);
  }

  function restoreModePreference(): void {
    const stored = window.localStorage.getItem(modePreferenceKey);
    if (stored === 'study' || stored === 'exam') {
      if (options.allowedModes.includes(stored)) {
        state.mode = stored;
      }
    }
  }

  function getProgress(mode: PracticeMode): PersistedProgress | null {
    const key = getStorageKey(mode);
    if (!key) return null;
    return safeParseJSON<PersistedProgress>(window.localStorage.getItem(key));
  }

  function persistProgress(): void {
    const key = getStorageKey(state.mode);
    if (!key || !state.detail) return;

    const payload: PersistedProgress = {
      content_id: state.detail.id,
      mode: state.mode,
      question_index: state.questionIndex,
      selected_by_question: state.selectedByQuestion,
      evaluation_by_question: state.evaluationByQuestion,
      submitted: state.submitted,
      updated_at: Date.now(),
    };

    window.localStorage.setItem(key, JSON.stringify(payload));
  }

  function clearModeProgress(mode: PracticeMode = state.mode): void {
    const key = getStorageKey(mode);
    if (key) {
      window.localStorage.removeItem(key);
    }
  }

  function clearStateForMode(): void {
    state.questionIndex = 0;
    state.selectedByQuestion = {};
    state.evaluationByQuestion = {};
    state.submitted = false;
    state.detailHasAnswers = false;
  }

  function getCurrentAttemptId(): string | null {
    const attemptId = state.detail?.attempt?.id;
    return typeof attemptId === 'string' && attemptId.trim() !== '' ? attemptId.trim() : null;
  }

  function hydrateFromAttemptPayload(payload: PracticeDetail | null, mode: PracticeMode): void {
    state.detail = payload;
    clearStateForMode();

    if (!payload) {
      return;
    }

    state.selectedByQuestion =
      payload.selected_by_question && typeof payload.selected_by_question === 'object'
        ? payload.selected_by_question
        : {};

    state.evaluationByQuestion =
      payload.evaluation_by_question && typeof payload.evaluation_by_question === 'object'
        ? payload.evaluation_by_question
        : {};

    const submitted = Boolean(payload.attempt?.submitted);
    state.submitted = mode === 'exam' ? submitted : false;
    state.detailHasAnswers = mode === 'study' ? true : Boolean(payload.attempt?.can_review);
  }

  function escapeHtml(value: unknown): string {
    return String(value ?? '')
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#039;');
  }

  function renderMathInlineText(value = '', optionsArg: { compact?: boolean } = {}): string {
    const compact = Boolean(optionsArg.compact);
    const base = cleanInlineForRender(value || '');
    const source = compact
      ? normalizeMathForDisplay(base)
      : String(base).replace(/\r?\n/g, ' ');
    const exponentPattern = /\^\\?\{([^}]+)\}|\^([A-Za-z0-9+\-]+)/g;

    let output = '';
    let lastIndex = 0;
    let match: RegExpExecArray | null = null;

    while ((match = exponentPattern.exec(source)) !== null) {
      const tokenIndex = match.index ?? 0;
      const exponentRaw = match[1] ?? match[2] ?? '';

      output += escapeHtml(source.slice(lastIndex, tokenIndex));
      output += `<sup>${escapeHtml(exponentRaw)}</sup>`;
      lastIndex = tokenIndex + match[0].length;
    }

    if (lastIndex < source.length) {
      output += escapeHtml(source.slice(lastIndex));
    }

    return output;
  }

  function shouldInsertInlineGap(prevRaw = '', nextRaw = ''): boolean {
    if (!prevRaw || !nextRaw) return false;
    if (/\s$/.test(prevRaw) || /^\s/.test(nextRaw)) return false;

    const prevChar = prevRaw.trimEnd().slice(-1);
    const nextChar = nextRaw.trimStart().slice(0, 1);
    if (!prevChar || !nextChar) return false;

    const prevIsWord = /[\p{L}\p{N})\]]/u.test(prevChar);
    const nextIsWord = /[\p{L}\p{N}([¿¡]/u.test(nextChar);
    return prevIsWord && nextIsWord;
  }

  function renderInlines(inlines: Array<{ text?: string; variant?: string }> = []): string {
    let html = '';
    let previousRaw = '';

    inlines.forEach((segment) => {
      const rawText = String(segment?.text ?? '');
      const text = renderMathInlineText(rawText);
      const variant = segment?.variant ?? 'plain';

      if (shouldInsertInlineGap(previousRaw, rawText)) {
        html += ' ';
      }

      if (variant === 'bold') {
        html += `<strong>${text}</strong>`;
      } else if (variant === 'italic') {
        html += `<em>${text}</em>`;
      } else if (variant === 'highlight') {
        html += `<mark>${text}</mark>`;
      } else if (variant === 'strike') {
        html += `<del>${text}</del>`;
      } else {
        html += text;
      }

      previousRaw = rawText;
    });

    return html;
  }

  function renderInlineText(value = ''): string {
    return renderInlines(parseInlineSegments(value));
  }

  function shouldRenderParagraphAsEquation(inlines: Array<{ text?: string; variant?: string }> = []): boolean {
    if (!Array.isArray(inlines) || inlines.length === 0) return false;

    const hasRichVariants = inlines.some((segment) => segment?.variant && segment.variant !== 'plain');
    if (hasRichVariants) return false;

    const raw = inlines
      .map((segment) => String(segment?.text || ''))
      .join(' ')
      .replace(/\s+/g, ' ')
      .trim();

    if (!raw || raw.length > 120) return false;
    if (!raw.includes('^')) return false;
    if (/[¿?!:;,\.]/.test(raw)) return false;

    const tokenMatches = raw.match(/[0-9]*[spdfgSPDFG][ ]*\^[0-9]+/g);
    return Array.isArray(tokenMatches) && tokenMatches.length >= 2;
  }

  function wrapBlock(block: Record<string, any> = {}, html = ''): string {
    if (!html) return '';

    const classes = ['members-block'];
    if (block.layout === 'full-width') {
      classes.push('layout-full-width');
    }

    return `<div class="${classes.join(' ')}">${html}</div>`;
  }

  function hasRenderableBlocks(blocks: Array<Record<string, any>> = []): boolean {
    if (!Array.isArray(blocks) || blocks.length === 0) return false;

    return blocks.some((block) => {
      if (!block || typeof block !== 'object') return false;

      if (block.type === 'image') {
        return Boolean(String(block.src || '').trim());
      }

      if (block.type === 'table' || block.type === 'equation') {
        return true;
      }

      if (block.type === 'html') {
        return Boolean(String(block.html || '').trim());
      }

      if (block.type === 'list') {
        return Array.isArray(block.items) && block.items.length > 0;
      }

      const text = Array.isArray(block.inlines)
        ? block.inlines.map((item) => item?.text || '').join(' ').trim()
        : String(block.text || '').trim();

      return Boolean(text);
    });
  }

  function renderBlocks(
    blocks: Array<Record<string, any>> = [],
    fallbackText = '',
    optionsArg: { feedback?: boolean } = {}
  ): string {
    if (!Array.isArray(blocks) || blocks.length === 0) {
      const fallback = cleanInlineMarkdown(fallbackText || '');
      return fallback ? `<p>${renderInlineText(fallback)}</p>` : '';
    }

    return blocks
      .map((block) => {
        if (!block || typeof block !== 'object') return '';

        if (block.type === 'paragraph') {
          const inlines =
            Array.isArray(block.inlines) && block.inlines.length > 0
              ? block.inlines
              : parseInlineSegments(block.text || '');

          if (shouldRenderParagraphAsEquation(inlines)) {
            const eqRaw = inlines.map((segment) => segment?.text || '').join(' ');
            return wrapBlock(block, `<code class="members-equation">${renderMathInlineText(eqRaw)}</code>`);
          }

          const renderedInline = renderInlines(inlines);
          return wrapBlock(block, `<p>${renderedInline}</p>`);
        }

        if (block.type === 'heading') {
          const depthRaw = Number(block.depth ?? 3);
          const depth = Math.min(Math.max(depthRaw, 2), 4);
          const tag = `h${depth}`;
          const inlines =
            Array.isArray(block.inlines) && block.inlines.length > 0
              ? block.inlines
              : parseInlineSegments(block.text || '');

          return wrapBlock(block, `<${tag} class="practice-rich-heading practice-rich-heading-${depth}">${renderInlines(inlines)}</${tag}>`);
        }

        if (block.type === 'image') {
          const src = escapeHtml(block.src || '');
          const alt = escapeHtml(block.alt || 'imagen');
          return wrapBlock(block, `<img src="${src}" alt="${alt}" loading="lazy" />`);
        }

        if (block.type === 'equation') {
          const latex = renderMathInlineText(cleanInlineMarkdown(block.latex || ''), { compact: true });
          return wrapBlock(block, `<code class="members-equation">${latex}</code>`);
        }

        if (block.type === 'table') {
          const rows = Array.isArray(block.rows) ? block.rows : [];
          if (rows.length === 0) return '';

          const header = rows[0] || [];
          const body = rows.slice(1);

          return wrapBlock(
            block,
            `
            <div class="members-table-wrap">
              <table class="members-table">
                <thead>
                  <tr>${header.map((cell) => `<th>${renderInlineText(cell)}</th>`).join('')}</tr>
                </thead>
                <tbody>
                  ${body
                    .map(
                      (row) => `<tr>${(row || []).map((cell) => `<td>${renderInlineText(cell)}</td>`).join('')}</tr>`
                    )
                    .join('')}
                </tbody>
              </table>
            </div>
          `
          );
        }

        if (block.type === 'list') {
          const items = Array.isArray(block.items) ? block.items : [];
          if (items.length === 0) return '';

          const tag = block.ordered ? 'ol' : 'ul';
          const renderedItems = items
            .map((item) => {
              const inlines =
                Array.isArray(item?.inlines) && item.inlines.length > 0
                  ? item.inlines
                  : parseInlineSegments(item?.text || '');
              return `<li>${renderInlines(inlines)}</li>`;
            })
            .join('');

          return wrapBlock(block, `<${tag} class="members-list-block">${renderedItems}</${tag}>`);
        }

        if (block.type === 'html' && optionsArg.feedback) {
          return wrapBlock(block, String(block.html || ''));
        }

        return '';
      })
      .join('');
  }

  function renderRichFragment(
    html = '',
    blocks: Array<Record<string, any>> = [],
    fallbackText = '',
    optionsArg: { feedback?: boolean; wrapperClass?: string } = {}
  ): string {
    const renderedBlocks = hasRenderableBlocks(blocks)
      ? renderBlocks(blocks, fallbackText, optionsArg)
      : '';

    if (optionsArg.feedback && renderedBlocks) {
      return optionsArg.wrapperClass
        ? `<div class="${escapeHtml(optionsArg.wrapperClass)}">${renderedBlocks}</div>`
        : renderedBlocks;
    }

    const renderedHtml = String(html || '').trim();
    if (renderedHtml) {
      return optionsArg.wrapperClass
        ? `<div class="${escapeHtml(optionsArg.wrapperClass)}">${renderedHtml}</div>`
        : renderedHtml;
    }

    if (!renderedBlocks) {
      return '';
    }

    return optionsArg.wrapperClass
      ? `<div class="${escapeHtml(optionsArg.wrapperClass)}">${renderedBlocks}</div>`
      : renderedBlocks;
  }

  function hasMeaningfulContext(
    blocks: Array<Record<string, any>> = [],
    html = '',
    fallbackText = ''
  ): boolean {
    if (String(html || '').trim() || String(fallbackText || '').trim()) {
      return true;
    }

    if (!Array.isArray(blocks) || blocks.length === 0) return false;

    return blocks.some((block) => {
      if (!block || typeof block !== 'object') return false;

      if (block.type === 'image') {
        return Boolean(String(block.src || '').trim());
      }

      if (block.type === 'table' || block.type === 'equation') {
        return true;
      }

      if (block.type === 'list') {
        return Array.isArray(block.items) && block.items.length > 0;
      }

      if (block.type === 'paragraph') {
        const raw = Array.isArray(block.inlines)
          ? block.inlines.map((item) => item?.text || '').join(' ').trim()
          : String(block.text || '').trim();

        return Boolean(raw);
      }

      return false;
    });
  }

  function getQuestions(): PracticeQuestion[] {
    return Array.isArray(state.detail?.questions) ? state.detail?.questions ?? [] : [];
  }

  function getQuestionEvaluation(question: PracticeQuestion): EvaluationResult | null {
    if (state.mode === 'study') {
      return state.evaluationByQuestion[question.id] ?? null;
    }

    if (!state.submitted || !state.detailHasAnswers) {
      return null;
    }

    const selectedId = state.selectedByQuestion[question.id];
    const persistedEvaluation = state.evaluationByQuestion[question.id];
    if (persistedEvaluation) {
      return persistedEvaluation;
    }

    const correctOptionId = String(question.correct_option_id ?? '');
    return {
      question_id: question.id,
      selected_option_id: selectedId ?? '',
      correct_option_id: correctOptionId || null,
      is_correct: Boolean(selectedId && correctOptionId && selectedId === correctOptionId),
      feedback_mdx: question.feedback_mdx ?? '',
      feedback_blocks: Array.isArray(question.feedback_blocks) ? question.feedback_blocks : [],
      concepts_mdx: question.concepts_mdx ?? '',
      concepts_blocks: Array.isArray(question.concepts_blocks) ? question.concepts_blocks : [],
    };
  }

  function getQuestionState(question: PracticeQuestion): 'pending' | 'selected' | 'correct' | 'wrong' {
    const selectedId = state.selectedByQuestion[question.id];
    const evaluation = getQuestionEvaluation(question);

    if (state.mode === 'exam' && state.submitted && !selectedId) {
      return 'pending';
    }

    if (evaluation) {
      return evaluation.is_correct ? 'correct' : 'wrong';
    }

    if (selectedId) {
      return 'selected';
    }

    return 'pending';
  }

  function computeExamSummary(): { correct: number; wrong: number; unanswered: number; score: number } {
    const questions = getQuestions();
    const correct = questions.filter((question) => getQuestionEvaluation(question)?.is_correct).length;
    const answered = questions.filter((question) => Boolean(state.selectedByQuestion[question.id])).length;
    const unanswered = Math.max(questions.length - answered, 0);
    const wrong = Math.max(answered - correct, 0);
    const score = questions.length > 0 ? Math.round((correct / questions.length) * 100) : 0;

    return { correct, wrong, unanswered, score };
  }

  function renderToolbar(detail: PracticeDetail, total: number): string {
    const studyCheckedCount = Object.keys(state.evaluationByQuestion).length;
    const studyCorrectCount = Object.values(state.evaluationByQuestion).filter((item) => item?.is_correct).length;
    const answeredCount = Object.keys(state.selectedByQuestion).length;
    const progressCount = state.mode === 'study' ? studyCheckedCount : state.submitted ? total : answeredCount;
    const progressPercent = total > 0 ? Math.round((progressCount / total) * 100) : 0;
    
    const summaryRow =
      state.mode === 'study'
        ? `
          <div class="practice-summary-row">
            <span class="practice-stat-pill approved">✅ ${studyCorrectCount} Correctas</span>
            <span class="practice-stat-pill pending">⏳ ${Math.max(total - studyCheckedCount, 0)} Pendientes</span>
          </div>
        `
        : state.submitted
        ? (() => {
            const summary = computeExamSummary();
            return `
              <div class="practice-summary-row">
                <span class="practice-stat-pill approved">🎯 ${summary.correct} Aciertos</span>
                <span class="practice-stat-pill blocked">❌ ${summary.wrong} Incorrectas</span>
                <span class="practice-stat-pill secondary">⚪ ${summary.unanswered} Omitidas</span>
              </div>
            `;
          })()
        : `
          <div class="practice-summary-row">
            <span class="practice-stat-pill approved">✍️ ${answeredCount} Respondidas</span>
            <span class="practice-stat-pill pending">❓ ${Math.max(total - answeredCount, 0)} Pendientes</span>
          </div>
        `;

    return `
      <div class="practice-toolbar">
        <div class="practice-toolbar-copy">
          <p class="practice-toolbar-label">${escapeHtml(options.contentLabel)}</p>
          <h2 class="practice-toolbar-title">${escapeHtml(detail.title || 'Práctica interactiva')}</h2>
          <p class="practice-toolbar-desc">
            ${state.mode === 'study'
              ? '📚 <strong>Práctica guiada:</strong> verifica cada respuesta para aprender.'
              : state.submitted
              ? `🏁 <strong>Entregado:</strong> Revisa tus resultados abajo.`
              : getExamModeDescription()}
          </p>
        </div>
        <div class="practice-toolbar-actions">
          <a class="members-button secondary" href="${escapeHtml(options.backHref)}">Volver</a>
          ${
            options.allowedModes.length > 1
              ? `
            <div class="practice-mode-toggle" role="tablist" aria-label="Modo de práctica">
              ${options.allowedModes
                .map(
                  (mode) => `
                <button
                  type="button"
                  class="practice-mode-button ${state.mode === mode ? 'is-active' : ''}"
                  data-mode="${mode}"
                >
                  ${getModeUiLabel(mode)}
                </button>
              `
                )
                .join('')}
            </div>
          `
              : ''
          }
          ${
            state.mode === 'exam' && !state.submitted
              ? `<button type="button" class="members-button" data-action="submit-exam">🚀 Entregar ${escapeHtml(getExamContentName())}</button>`
              : ''
          }
        </div>
      </div>

      <div class="practice-top-meta" style="background: color-mix(in oklab, var(--bg-secondary) 50%, var(--bg-primary)); border-radius: 18px; padding: 1.25rem; border: 1px solid var(--border-color); margin-top: 1rem;">
        <div class="practice-progress-summary">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
             ${summaryRow}
             <span style="font-size: 0.85rem; font-weight: 800; color: var(--color-primary);">${progressPercent}%</span>
          </div>
          <div class="members-progress-track" aria-label="Progreso" style="margin-top: 0; height: 12px; background: color-mix(in oklab, var(--border-color) 40%, transparent);">
            <div class="members-progress-fill" style="width:${progressPercent}%"></div>
          </div>
        </div>
      </div>
    `;
  }

  function renderNavigator(questions: PracticeQuestion[]): string {
    return `
      <div class="practice-panel" style="background: var(--bg-primary); border-color: color-mix(in oklab, var(--border-color) 60%, var(--color-primary) 40%);">
        <p class="practice-panel-title">Navegación de preguntas</p>
        <div class="practice-chip-grid" style="gap: 0.6rem;">
          ${questions
            .map((question, index) => {
              const classes = ['members-qchip', getQuestionState(question)];
              if (index === state.questionIndex) {
                classes.push('current');
              }
              const stateEmoji = 
                getQuestionState(question) === 'correct' ? '✓' :
                getQuestionState(question) === 'wrong' ? '✕' :
                getQuestionState(question) === 'selected' ? '•' : '';

              return `
                <button
                  type="button"
                  class="${classes.join(' ')}"
                  data-question-index="${index}"
                  aria-label="Ir a la pregunta ${index + 1}"
                  style="position: relative;"
                >
                  <span>${index + 1}</span>
                  ${stateEmoji ? `<small style="position: absolute; top: -4px; right: -4px; background: inherit; border: 1px solid; border-radius: 50%; width: 14px; height: 14px; font-size: 10px; display: flex; align-items: center; justify-content: center;">${stateEmoji}</small>` : ''}
                </button>
              `;
            })
            .join('')}
        </div>
      </div>
    `;
  }

  function renderQuestionInsight(question: PracticeQuestion): string {
    const selectedId = state.selectedByQuestion[question.id];
    const evaluation = getQuestionEvaluation(question);
    const shouldShowReview = Boolean(evaluation) || (state.mode === 'exam' && state.submitted && state.detailHasAnswers);

    if (!shouldShowReview) {
      return '';
    }

    const optionsMap = new Map((question.options ?? []).map((option) => [option.id, option]));
    const selectedOption = selectedId ? optionsMap.get(selectedId) : null;
    const questionCorrectOptionId = String(question.correct_option_id ?? '');
    const correctOptionId = evaluation?.correct_option_id ?? (questionCorrectOptionId || null);
    const correctOption = correctOptionId ? optionsMap.get(correctOptionId) : null;
    
    const feedbackBlocks =
      state.mode === 'study'
        ? evaluation?.feedback_blocks ?? []
        : Array.isArray(question.feedback_blocks)
        ? question.feedback_blocks
        : [];
    const feedbackHtml =
      state.mode === 'study'
        ? evaluation?.feedback_html ?? ''
        : question.feedback_html ?? '';
    const feedbackSummary =
      state.mode === 'study'
        ? evaluation?.feedback_summary ?? question.feedback_summary ?? '💡 Explicación de la respuesta'
        : question.feedback_summary ?? '💡 Explicación de la respuesta';
    const feedbackMdx =
      state.mode === 'study'
        ? evaluation?.feedback_mdx ?? ''
        : question.feedback_mdx ?? '';
        
    const conceptBlocks =
      state.mode === 'study'
        ? evaluation?.concepts_blocks ?? []
        : Array.isArray(question.concepts_blocks)
        ? question.concepts_blocks
        : [];
    const conceptsHtml =
      state.mode === 'study'
        ? evaluation?.concepts_html ?? ''
        : question.concepts_html ?? '';
    const conceptsSummary =
      state.mode === 'study'
        ? evaluation?.concepts_summary ?? question.concepts_summary ?? '📚 Conceptos relacionados'
        : question.concepts_summary ?? '📚 Conceptos relacionados';
    const conceptsMdx =
      state.mode === 'study'
        ? evaluation?.concepts_mdx ?? ''
        : question.concepts_mdx ?? '';

    return `
      <div class="practice-insight-card" style="border-color: ${evaluation?.is_correct ? '#27ae60' : evaluation ? '#c0392b' : 'var(--border-color)'}; background: color-mix(in oklab, ${evaluation?.is_correct ? '#27ae60' : evaluation ? '#c0392b' : 'var(--bg-primary)'} 6%, var(--bg-primary));">
        <p class="practice-panel-title">💡 Solución y Retroalimentación</p>
        
        <div class="insight-comparison">
          <div class="insight-item ${selectedOption ? (evaluation?.is_correct ? 'insight-item--correct' : 'insight-item--wrong') : 'insight-item--neutral'}">
            <div class="insight-item-icon">${evaluation?.is_correct ? '✓' : selectedOption ? '✕' : '•'}</div>
            <div class="insight-item-content">
              <label class="insight-item-label">Tu elección</label>
              <div class="insight-item-value">
                ${selectedOption ? `<strong>${escapeHtml(selectedOption.id)}</strong>. ${renderInlineText(selectedOption.text)}` : 'Sin responder'}
              </div>
            </div>
          </div>

          <div class="insight-item insight-item--correct">
            <div class="insight-item-icon">✓</div>
            <div class="insight-item-content">
              <label class="insight-item-label">Respuesta correcta</label>
              <div class="insight-item-value">
                ${correctOption ? `<strong>${escapeHtml(correctOption.id)}</strong>. ${renderInlineText(correctOption.text)}` : 'No disponible'}
              </div>
            </div>
          </div>
        </div>
        
        ${
          feedbackBlocks.length > 0 || feedbackMdx || feedbackHtml
            ? `
          <div class="practice-details-static">
            <p class="practice-panel-title" style="margin-bottom: 0.75rem;">${escapeHtml(feedbackSummary)}</p>
            <div class="members-render">
              ${renderRichFragment(feedbackHtml, feedbackBlocks, feedbackMdx, { feedback: true })}
            </div>
          </div>
        `
            : ''
        }
        
        ${
          conceptBlocks.length > 0 || conceptsMdx || conceptsHtml
            ? `
          <div class="practice-details-static" style="background: color-mix(in oklab, var(--color-secondary) 8%, var(--bg-primary)); border-color: color-mix(in oklab, var(--border-color) 70%, var(--color-secondary) 30%);">
            <p class="practice-panel-title" style="margin-bottom: 0.75rem;">${escapeHtml(conceptsSummary)}</p>
            <div class="members-render">
              ${renderRichFragment(conceptsHtml, conceptBlocks, conceptsMdx, { feedback: true })}
            </div>
          </div>
        `
            : ''
        }
      </div>
    `;
  }

  function renderResultsCard(): string {
    if (state.mode !== 'exam' || !state.submitted) {
      return '';
    }

    const summary = computeExamSummary();
    const canReview = Boolean(state.detail?.attempt?.can_review);
    const scoreLabel =
      typeof state.detail?.attempt?.score_percent === 'number'
        ? `${state.detail.attempt.score_percent}%`
        : `${summary.score}%`;
    const heading = canReview ? `🎯 Retroalimentación disponible` : `📤 Intento entregado con éxito`;
    const description = canReview
      ? 'Excelente, ya puedes revisar cada pregunta con su explicación detallada.'
      : 'Tu resultado ha sido guardado. Los docentes liberarán la retroalimentación próximamente.';

    return `
      <section class="practice-results-card" style="margin-top: 1rem; background: linear-gradient(135deg, color-mix(in oklab, var(--bg-primary) 92%, var(--color-primary) 8%), var(--bg-primary)); border-color: var(--color-primary); border-width: 2px;">
        <div style="display: flex; align-items: flex-start; gap: 1rem;">
          <div style="background: var(--color-primary); color: white; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0;">🏆</div>
          <div>
            <p class="practice-toolbar-label" style="color: var(--color-primary);">Resultados del intento</p>
            <h2 class="practice-toolbar-title" style="font-size: 1.5rem; margin: 0.25rem 0;">${heading}</h2>
            <p class="practice-toolbar-desc" style="font-size: 1rem;">${description}</p>
          </div>
        </div>
        <div class="practice-results-grid" style="margin-top: 0.5rem; gap: 1rem;">
          <article class="practice-result-box" style="background: var(--bg-primary); border-radius: 16px; border-width: 2px; border-color: var(--color-primary);">
            <p style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-secondary); margin-bottom: 0.25rem;">Puntaje</p>
            <p style="font-size: 2rem; font-weight: 900; color: var(--color-primary);">${scoreLabel}</p>
          </article>
          <article class="practice-result-box" style="background: var(--bg-primary); border-radius: 16px;">
            <p style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-secondary); margin-bottom: 0.25rem;">Aciertos</p>
            <p style="font-size: 1.75rem; font-weight: 800; color: #27ae60;">${summary.correct}</p>
          </article>
          <article class="practice-result-box" style="background: var(--bg-primary); border-radius: 16px;">
            <p style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-secondary); margin-bottom: 0.25rem;">Errores</p>
            <p style="font-size: 1.75rem; font-weight: 800; color: #c0392b;">${summary.wrong}</p>
          </article>
          <article class="practice-result-box" style="background: var(--bg-primary); border-radius: 16px;">
            <p style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-secondary); margin-bottom: 0.25rem;">Omitidas</p>
            <p style="font-size: 1.75rem; font-weight: 800; color: var(--text-secondary);">${summary.unanswered}</p>
          </article>
        </div>
      </section>
    `;
  }

  function renderQuestionCard(question: PracticeQuestion, questions: PracticeQuestion[]): string {
    const selectedId = state.selectedByQuestion[question.id];
    const evaluation = getQuestionEvaluation(question);
    const showContext = hasMeaningfulContext(
      question.context_blocks ?? [],
      question.context_html ?? '',
      question.context_mdx ?? ''
    );
    
    const optionsHtml = (question.options ?? [])
      .map((option) => {
        const isSelected = selectedId === option.id;
        const isCorrect = Boolean(evaluation?.correct_option_id && evaluation.correct_option_id === option.id);
        const isWrongSelection = Boolean(evaluation && isSelected && !isCorrect);
        const classes = [
          'members-option',
          isSelected ? 'selected' : '',
          evaluation && isCorrect ? 'correct' : '',
          isWrongSelection ? 'wrong' : '',
        ]
          .filter(Boolean)
          .join(' ');

        return `
          <button type="button" class="${classes}" data-option-id="${escapeHtml(option.id)}">
            <span class="members-option-prefix" style="font-weight: 900; margin-right: 0.75rem; color: color-mix(in oklab, var(--text-primary) 60%, var(--color-primary) 40%);">${escapeHtml(option.id)}.</span>
            <span class="members-option-text" style="flex: 1;">${renderInlineText(option.text || '')}</span>
          </button>
        `;
      })
      .join('');

    return `
      <section class="practice-question-card" style="margin-top: 1.5rem; border: none; padding: 0; background: transparent;">
        <div class="practice-question-head" style="margin-bottom: 1rem; align-items: flex-end;">
          <div style="display: flex; align-items: baseline; gap: 0.75rem;">
            <p class="practice-question-count" style="font-size: 1.75rem; letter-spacing: -0.02em;">
              Pregunta <span style="color: var(--color-primary);">${state.questionIndex + 1}</span>
            </p>
            <span style="font-size: 1.1rem; font-weight: 600; color: var(--text-secondary);">de ${questions.length}</span>
          </div>
          <span class="practice-question-status" data-state="${getQuestionState(question)}" style="box-shadow: 0 4px 10px -4px rgba(15, 23, 42, 0.1); border-width: 2px;">
            ${
              getQuestionState(question) === 'correct'
                ? '✅ Correcta'
                : getQuestionState(question) === 'wrong'
                ? '❌ Por reforzar'
                : getQuestionState(question) === 'selected'
                ? '🔘 Seleccionada'
                : '⏳ Pendiente'
            }
          </span>
        </div>

        ${renderNavigator(questions)}

        <div class="practice-content-wrap" style="background: var(--bg-primary); border: 1px solid var(--border-color); border-radius: 20px; padding: 1.75rem; box-shadow: 0 10px 30px -15px rgba(15, 23, 42, 0.1);">
          ${
            showContext
              ? `
            <div class="practice-panel" style="background: color-mix(in oklab, var(--bg-secondary) 50%, transparent); border-style: dashed; margin-bottom: 1.5rem;">
              <p class="practice-panel-title">📖 Contexto de la pregunta</p>
              <div class="members-render" style="font-size: 1.05rem;">
                ${renderRichFragment(
                  question.context_html ?? '',
                  question.context_blocks ?? [],
                  question.context_mdx ?? '',
                  { wrapperClass: 'practice-rich-fragment' }
                )}
              </div>
            </div>
          `
              : ''
          }

          <div class="members-render" style="margin-bottom: 2rem;">
            ${renderRichFragment(
              question.stem_html ?? '',
              question.stem_blocks ?? [],
              question.stem_mdx ?? '',
              { wrapperClass: 'practice-rich-fragment' }
            )}
          </div>

          <div class="members-options">${optionsHtml}</div>
          
          ${renderQuestionInsight(question)}
        </div>

        <div class="members-actions members-actions-primary" style="margin-top: 1.5rem; justify-content: center; gap: 1rem;">
          <button type="button" class="members-button secondary" data-nav="prev" ${state.questionIndex <= 0 ? 'disabled' : ''} style="min-width: 120px;">← Anterior</button>
          
          ${
            state.mode === 'study'
              ? `<button type="button" class="members-button" data-action="check" ${selectedId ? '' : 'disabled'} style="min-width: 180px; box-shadow: 0 8px 20px -8px rgba(37, 99, 235, 0.6);">Comprobar respuesta</button>`
              : state.submitted
              ? `<button type="button" class="members-button secondary" data-action="back-to-top" style="min-width: 180px;">Ver mis resultados</button>`
              : `<button type="button" class="members-button" data-action="submit-exam" style="min-width: 180px; box-shadow: 0 8px 20px -8px rgba(37, 99, 235, 0.6);">${state.questionIndex === questions.length - 1 ? 'Finalizar y entregar' : 'Entregar simulacro'}</button>`
          }
          
          <button type="button" class="members-button secondary" data-nav="next" ${state.questionIndex >= questions.length - 1 ? 'disabled' : ''} style="min-width: 120px;">Siguiente →</button>
        </div>
      </section>
    `;
  }

  function showFeedbackMessage(message: string, type: 'error' | 'warning' | 'ok' = 'error'): void {
    if (feedbackEl) {
      feedbackEl.innerHTML = `<div class="members-alert ${type}">${escapeHtml(message)}</div>`;
    }
  }

  function showError(message: string): void {
    showFeedbackMessage(message, 'error');
  }

  function clearFeedback(): void {
    if (feedbackEl) {
      feedbackEl.innerHTML = '';
    }
  }

  function scrollToTop(): void {
    const topNav = document.querySelector('.top-nav');
    const navOffset = topNav ? topNav.getBoundingClientRect().height : 0;
    const targetTop = window.scrollY + root.getBoundingClientRect().top - navOffset - 16;

    window.scrollTo({
      top: Math.max(0, targetTop),
      behavior: 'smooth',
    });
  }

  function render(): void {
    if (state.isLoading) {
      root.innerHTML = `<div class="practice-loading">Cargando práctica interactiva…</div>`;
      return;
    }

    if (!state.detail) {
      root.innerHTML = `
        <div class="practice-empty-state">
          ${escapeHtml(options.emptyMessage ?? 'No fue posible cargar este contenido.')}
          <div class="members-actions" style="margin-top:0.8rem;">
            <a class="members-button secondary" href="${escapeHtml(options.backHref)}">Volver</a>
          </div>
        </div>
      `;
      return;
    }

    const questions = getQuestions();
    if (questions.length === 0) {
      root.innerHTML = `
        <div class="practice-empty-state">
          Este contenido aún no tiene preguntas cargadas.
          <div class="members-actions" style="margin-top:0.8rem;">
            <a class="members-button secondary" href="${escapeHtml(options.backHref)}">Volver</a>
          </div>
        </div>
      `;
      return;
    }

    const safeIndex = Math.min(Math.max(0, state.questionIndex), Math.max(questions.length - 1, 0));
    state.questionIndex = safeIndex;
    const currentQuestion = questions[safeIndex];

    root.innerHTML = `
      <div class="practice-surface">
        ${renderToolbar(state.detail, questions.length)}
        ${renderResultsCard()}
        <div class="practice-section-grid">
          ${renderQuestionCard(currentQuestion, questions)}
        </div>
      </div>
    `;

    root.querySelectorAll<HTMLElement>('[data-question-index]').forEach((button) => {
      button.addEventListener('click', () => {
        const nextIndex = Number.parseInt(button.dataset.questionIndex ?? '', 10);
        if (!Number.isFinite(nextIndex)) return;
        state.questionIndex = Math.min(questions.length - 1, Math.max(0, nextIndex));
        persistProgress();
        render();
        scrollToTop();
      });
    });

    root.querySelectorAll<HTMLButtonElement>('[data-option-id]').forEach((button) => {
      button.addEventListener('click', async () => {
        const optionId = button.dataset.optionId;
        if (!optionId) return;

        state.selectedByQuestion[currentQuestion.id] = optionId;

        if (state.mode === 'study') {
          delete state.evaluationByQuestion[currentQuestion.id];
        }

        persistProgress();
        render();

        if (state.mode !== 'exam' || state.submitted) {
          return;
        }

        const attemptId = getCurrentAttemptId();
        if (!attemptId) {
          return;
        }

        try {
          const response = await options.api.answerAttempt(attemptId, currentQuestion.id, optionId);
          if (response?.data) {
            state.evaluationByQuestion[currentQuestion.id] = response.data;
            persistProgress();
          }
        } catch (error) {
          const message = error instanceof Error ? error.message : 'No fue posible guardar la respuesta.';
          showError(message);
        }
      });
    });

    root.querySelectorAll<HTMLButtonElement>('[data-nav="prev"]').forEach((button) => {
      button.addEventListener('click', () => {
        if (state.questionIndex <= 0) return;
        state.questionIndex -= 1;
        persistProgress();
        render();
        scrollToTop();
      });
    });

    root.querySelectorAll<HTMLButtonElement>('[data-nav="next"]').forEach((button) => {
      button.addEventListener('click', () => {
        if (state.questionIndex >= questions.length - 1) return;
        state.questionIndex += 1;
        persistProgress();
        render();
        scrollToTop();
      });
    });

    root.querySelectorAll<HTMLButtonElement>('[data-mode]').forEach((button) => {
      button.addEventListener('click', async () => {
        const nextMode = button.dataset.mode;
        if (nextMode !== 'study' && nextMode !== 'exam') return;
        if (state.mode === nextMode) return;
        await switchMode(nextMode);
      });
    });

    root.querySelectorAll<HTMLButtonElement>('[data-action="check"]').forEach((button) => {
      button.addEventListener('click', async () => {
        const selectedId = state.selectedByQuestion[currentQuestion.id];
        if (!selectedId) return;
        const attemptId = getCurrentAttemptId();
        if (!attemptId) return;

        try {
          clearFeedback();
          const response = await options.api.answerAttempt(attemptId, currentQuestion.id, selectedId);
          state.evaluationByQuestion[currentQuestion.id] = response?.data;
          persistProgress();
          render();
          scrollToTop();
        } catch (error) {
          const message = error instanceof Error ? error.message : 'No fue posible evaluar la respuesta.';
          showError(message);
        }
      });
    });

    root.querySelectorAll<HTMLButtonElement>('[data-action="submit-exam"]').forEach((button) => {
      button.addEventListener('click', async () => {
        if (state.mode !== 'exam' || state.submitted || !options.api.submitAttempt) return;
        await submitExam();
      });
    });

    root.querySelectorAll<HTMLButtonElement>('[data-action="back-to-top"]').forEach((button) => {
      button.addEventListener('click', scrollToTop);
    });
  }

  async function loadDetailForCurrentMode(reset = false): Promise<void> {
    state.isLoading = true;
    render();

    const progress = getProgress(state.mode);
    const response = await options.api.startAttempt(options.contentId, {
      mode: state.mode === 'exam' ? 'simulacro' : 'study',
      reset,
    });

    hydrateFromAttemptPayload(response?.data ?? null, state.mode);

    if (state.detail && progress && progress.content_id === state.detail.id) {
      const total = Array.isArray(state.detail.questions) ? state.detail.questions.length : 0;
      const nextIndex = Number.parseInt(String(progress.question_index ?? 0), 10);
      state.questionIndex = Number.isFinite(nextIndex)
        ? Math.min(Math.max(0, nextIndex), Math.max(total - 1, 0))
        : 0;
    }

    state.isLoading = false;
  }

  async function switchMode(nextMode: PracticeMode): Promise<void> {
    state.mode = nextMode;
    persistModePreference();
    clearFeedback();
    await loadDetailForCurrentMode();
    render();
  }

  async function submitExam(): Promise<void> {
    const total = getQuestions().length;
    const answered = Object.keys(state.selectedByQuestion).length;
    const shouldSubmit = window.confirm(
      answered < total
        ? `Has respondido ${answered} de ${total} preguntas. Si entregas ahora la ${getExamContentName()}, las restantes quedarán omitidas.`
        : `Se cerrará la ${getExamContentName()} actual. ¿Deseas continuar?`
    );

    if (!shouldSubmit) return;

    try {
      clearFeedback();
      state.isLoading = true;
      render();
      const attemptId = getCurrentAttemptId();
      if (!attemptId || !options.api.submitAttempt) {
        throw new Error('No fue posible localizar el intento activo.');
      }

      const answersToSync = Object.entries(state.selectedByQuestion);
      for (const [questionId, optionId] of answersToSync) {
        if (!optionId) continue;
        await options.api.answerAttempt(attemptId, questionId, optionId);
      }

      const response = await options.api.submitAttempt(attemptId);
      hydrateFromAttemptPayload(response?.data ?? null, state.mode);
      persistProgress();
      state.isLoading = false;
      if (state.detail?.attempt?.can_review) {
        showFeedbackMessage(`Entrega confirmada. Ya puedes revisar la ${getExamContentName()} con respuesta correcta y conceptos relacionados.`, 'ok');
      } else {
        showFeedbackMessage(`Entrega confirmada. Tu resultado quedó guardado, pero la retroalimentación todavía no está disponible.`, 'warning');
      }
      render();
      scrollToTop();
    } catch (error) {
      state.isLoading = false;
      render();
      const message = error instanceof Error ? error.message : 'No fue posible entregar el simulacro.';
      const normalizedMessage =
        message === 'No fue posible entregar el simulacro.'
          ? `No fue posible entregar la ${getExamContentName()}.`
          : message;
      showError(normalizedMessage);
    }
  }

  async function resetCurrentMode(): Promise<void> {
    const title = state.detail?.title || options.contentLabel;
    const shouldReset = window.confirm(`Se borrará tu avance guardado de "${title}". ¿Deseas continuar?`);
    if (!shouldReset) return;

    clearModeProgress();
    clearFeedback();
    await loadDetailForCurrentMode(true);
    render();
    scrollToTop();
  }

  async function boot(): Promise<void> {
    try {
      restoreModePreference();
      const sessionResponse = await options.api.me();
      const user = sessionResponse?.data?.user as MemberUser | undefined;
      if (!user) {
        throw new Error('Sesión inválida.');
      }

      state.currentUser = user;
      options.api.saveSession(token, user);

      if (user.member_status !== 'approved' && user.role !== 'admin') {
        showError('No tienes acceso activo a este contenido premium.');
        state.isLoading = false;
        render();
        return;
      }

      await loadDetailForCurrentMode();
      render();

      if (resetButton) {
        resetButton.addEventListener('click', () => {
          void resetCurrentMode();
        });
      }
    } catch (error) {
      const message = error instanceof Error ? error.message : 'No fue posible cargar la práctica.';
      if (/auth|required|sesión|session/i.test(message)) {
        options.api.clearSession();
        window.location.href = '/miembros/login';
        return;
      }

      state.isLoading = false;
      showError(message);
      render();
    }
  }

  void boot();
}
