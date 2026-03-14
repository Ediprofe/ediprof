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

const MODE_LABELS: Record<PracticeMode, string> = {
  study: 'Estudio guiado',
  exam: 'Modo simulacro',
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
    const renderedHtml = String(html || '').trim();
    if (renderedHtml) {
      return optionsArg.wrapperClass
        ? `<div class="${escapeHtml(optionsArg.wrapperClass)}">${renderedHtml}</div>`
        : renderedHtml;
    }

    const renderedBlocks = renderBlocks(blocks, fallbackText, optionsArg);
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
            <span class="practice-stat-pill">Comprobadas ${studyCheckedCount}</span>
            <span class="practice-stat-pill">Correctas ${studyCorrectCount}</span>
            <span class="practice-stat-pill">Pendientes ${Math.max(total - studyCheckedCount, 0)}</span>
          </div>
        `
        : state.submitted
        ? (() => {
            const summary = computeExamSummary();
            return `
              <div class="practice-summary-row">
                <span class="practice-stat-pill">Aciertos ${summary.correct}</span>
                <span class="practice-stat-pill">Incorrectas ${summary.wrong}</span>
                <span class="practice-stat-pill">Omitidas ${summary.unanswered}</span>
              </div>
            `;
          })()
        : `
          <div class="practice-summary-row">
            <span class="practice-stat-pill">Respondidas ${answeredCount}</span>
            <span class="practice-stat-pill">Pendientes ${Math.max(total - answeredCount, 0)}</span>
          </div>
        `;

    return `
      <div class="practice-toolbar">
        <div class="practice-toolbar-copy">
          <p class="practice-toolbar-label">${escapeHtml(options.contentLabel)}</p>
          <h2 class="practice-toolbar-title">${escapeHtml(detail.title || 'Práctica interactiva')}</h2>
          <p class="practice-toolbar-desc">
            ${state.mode === 'study'
              ? 'Resuelve una pregunta y verifica de inmediato la explicación.'
              : state.submitted
              ? `Ya entregaste la ${escapeHtml(getExamContentName())}.`
              : `Responde primero y entrega la ${escapeHtml(getExamContentName())} cuando termines.`}
          </p>
        </div>
        <div class="practice-toolbar-actions">
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
                  ${MODE_LABELS[mode]}
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
              ? `<button type="button" class="members-button" data-action="submit-exam">Entregar ${escapeHtml(getExamContentName())}</button>`
              : ''
          }
        </div>
      </div>

      <div class="practice-top-meta">
        <div class="practice-progress-summary">
          ${summaryRow}
          <div class="members-progress-track" aria-label="Progreso">
            <div class="members-progress-fill" style="width:${progressPercent}%"></div>
          </div>
          <p class="members-progress-label">${progressPercent}% completado</p>
        </div>
      </div>
    `;
  }

  function renderNavigator(questions: PracticeQuestion[]): string {
    return `
      <div class="practice-panel">
        <p class="practice-panel-title">Navegación rápida</p>
        <div class="practice-chip-grid">
          ${questions
            .map((question, index) => {
              const classes = ['members-qchip', getQuestionState(question)];
              if (index === state.questionIndex) {
                classes.push('current');
              }
              return `
                <button
                  type="button"
                  class="${classes.join(' ')}"
                  data-question-index="${index}"
                  aria-label="Ir a la pregunta ${index + 1}"
                >
                  <span>${index + 1}</span>
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
        ? evaluation?.feedback_summary ?? question.feedback_summary ?? 'Respuesta'
        : question.feedback_summary ?? 'Respuesta';
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
        ? evaluation?.concepts_summary ?? question.concepts_summary ?? 'Conceptos relacionados'
        : question.concepts_summary ?? 'Conceptos relacionados';
    const conceptsMdx =
      state.mode === 'study'
        ? evaluation?.concepts_mdx ?? ''
        : question.concepts_mdx ?? '';

    return `
      <div class="practice-insight-card">
        <p class="practice-panel-title">Solución guiada</p>
        <div class="practice-insight-grid">
          <div>
            <p class="practice-insight-label">Tu respuesta</p>
            <p class="practice-insight-value">${selectedOption ? `${escapeHtml(selectedOption.id)}. ${renderInlineText(selectedOption.text)}` : 'Sin responder'}</p>
          </div>
          <div>
            <p class="practice-insight-label">Respuesta correcta</p>
            <p class="practice-insight-value">${correctOption ? `${escapeHtml(correctOption.id)}. ${renderInlineText(correctOption.text)}` : 'No disponible'}</p>
          </div>
          <div>
            <p class="practice-insight-label">Estado</p>
            <p class="practice-insight-value">${
              !selectedOption
                ? 'Omitida'
                : evaluation?.is_correct
                ? 'Correcta'
                : 'Por reforzar'
            }</p>
          </div>
        </div>
        ${
          feedbackBlocks.length > 0 || feedbackMdx || feedbackHtml
            ? `
          <details class="practice-details">
            <summary>${escapeHtml(feedbackSummary || 'Respuesta')}</summary>
            ${renderRichFragment(feedbackHtml, feedbackBlocks, feedbackMdx, { feedback: true })}
          </details>
        `
            : ''
        }
        ${
          conceptBlocks.length > 0 || conceptsMdx || conceptsHtml
            ? `
          <details class="practice-details conceptos-relacionados">
            <summary>${escapeHtml(conceptsSummary || 'Conceptos relacionados')}</summary>
            ${renderRichFragment(conceptsHtml, conceptBlocks, conceptsMdx, { feedback: true })}
          </details>
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
    const scoreLabel =
      typeof state.detail?.attempt?.score_percent === 'number'
        ? `${state.detail.attempt.score_percent}%`
        : `${summary.score}%`;

    return `
      <section class="practice-results-card">
        <div>
          <p class="practice-toolbar-label">Resultado final</p>
          <h2 class="practice-toolbar-title">Revisión del simulacro</h2>
          <p class="practice-toolbar-desc">Ya puedes revisar cada pregunta con su explicación y profundización.</p>
        </div>
        <div class="practice-results-grid">
          <article class="practice-result-box">
            <h3>Puntaje</h3>
            <p>${scoreLabel}</p>
          </article>
          <article class="practice-result-box">
            <h3>Aciertos</h3>
            <p>${summary.correct}</p>
          </article>
          <article class="practice-result-box">
            <h3>Incorrectas</h3>
            <p>${summary.wrong}</p>
          </article>
          <article class="practice-result-box">
            <h3>Omitidas</h3>
            <p>${summary.unanswered}</p>
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
            ${escapeHtml(option.id)}. ${renderInlineText(option.text || '')}
          </button>
        `;
      })
      .join('');

    return `
      <section class="practice-question-card">
        <div class="practice-question-head">
          <p class="practice-question-count">
            Pregunta ${state.questionIndex + 1}
            <span class="members-current-number"><span>de ${questions.length}</span></span>
          </p>
          <span class="practice-question-status" data-state="${getQuestionState(question)}">
            ${
              getQuestionState(question) === 'correct'
                ? 'Correcta'
                : getQuestionState(question) === 'wrong'
                ? 'Por reforzar'
                : getQuestionState(question) === 'selected'
                ? 'Seleccionada'
                : 'Pendiente'
            }
          </span>
        </div>

        ${renderNavigator(questions)}

        ${
          showContext
            ? `
          <div class="practice-panel">
            <p class="practice-panel-title">Contexto compartido</p>
            ${renderRichFragment(
              question.context_html ?? '',
              question.context_blocks ?? [],
              question.context_mdx ?? '',
              { wrapperClass: 'practice-rich-fragment' }
            )}
          </div>
        `
            : ''
        }

        ${renderRichFragment(
          question.stem_html ?? '',
          question.stem_blocks ?? [],
          question.stem_mdx ?? '',
          { wrapperClass: 'practice-rich-fragment' }
        )}

        <div class="members-options">${optionsHtml}</div>

        ${renderQuestionInsight(question)}

        <div class="members-actions members-actions-primary">
          <button type="button" class="members-button secondary" data-nav="prev" ${state.questionIndex <= 0 ? 'disabled' : ''}>Anterior</button>
          ${
            state.mode === 'study'
              ? `<button type="button" class="members-button" data-action="check" ${selectedId ? '' : 'disabled'}>Comprobar</button>`
              : state.submitted
              ? `<button type="button" class="members-button secondary" data-action="back-to-top">Ver resultado</button>`
              : `<button type="button" class="members-button" data-action="submit-exam">${state.questionIndex === questions.length - 1 ? 'Entregar simulacro' : 'Entregar ahora'}</button>`
          }
          <button type="button" class="members-button secondary" data-nav="next" ${state.questionIndex >= questions.length - 1 ? 'disabled' : ''}>Siguiente</button>
        </div>
      </section>
    `;
  }

  function showError(message: string): void {
    if (feedbackEl) {
      feedbackEl.innerHTML = `<div class="members-alert error">${escapeHtml(message)}</div>`;
    }
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
