import { useCallback, useEffect, useMemo, useState } from 'react';
import {
  ActivityIndicator,
  FlatList,
  NativeModules,
  Pressable,
  SafeAreaView,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  View,
} from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { QuestionStem } from './src/components/QuestionStem';
import { WorkshopCard } from './src/components/WorkshopCard';
import {
  ApiRequestError,
  evaluateWorkshopAnswer,
  getCurrentUser,
  getWorkshop,
  listWorkshops,
  login,
  logout,
} from './src/lib/api';
import {
  clearWorkshopPracticeState,
  clearSessionToken,
  loadWorkshopPracticeStateMap,
  loadWorkshopPracticeState,
  loadBaseUrl,
  loadSessionToken,
  saveBaseUrl,
  saveSessionToken,
  saveWorkshopPracticeState,
  type WorkshopPracticeState,
} from './src/lib/storage';
import type { WorkshopDetail, WorkshopEvaluationResult, WorkshopSummary } from './src/types/api';

const DEFAULT_BASE_URL = 'http://127.0.0.1:8080/api/v1';
const MIN_SESSION_DURATION_SECONDS = 10 * 60;
const PER_QUESTION_SECONDS = 90;
const STRICT_MODE_DURATION_SECONDS = 45 * 60;

type DetailAccessError = 'auth_required' | 'premium_access_required' | null;

type HydratedPracticeState = {
  questionIndex: number;
  selectedOptionByQuestion: Record<string, string>;
  evaluationByQuestion: Record<string, WorkshopEvaluationResult>;
  visitedQuestionIds: string[];
  elapsedSeconds: number;
  timerRunning: boolean;
};

type WorkshopProgressMeta = {
  completionPercent: number;
  resumeQuestionIndex: number;
  evaluatedCount: number;
  updatedAt: string;
};

type SessionRecommendation = {
  title: string;
  detail: string;
};

function hasPracticeData(state: {
  questionIndex: number;
  selectedOptionByQuestion: Record<string, string>;
  evaluationByQuestion: Record<string, WorkshopEvaluationResult>;
}): boolean {
  return (
    state.questionIndex > 0 ||
    Object.keys(state.selectedOptionByQuestion).length > 0 ||
    Object.keys(state.evaluationByQuestion).length > 0
  );
}

function hasPersistableState(state: {
  questionIndex: number;
  selectedOptionByQuestion: Record<string, string>;
  evaluationByQuestion: Record<string, WorkshopEvaluationResult>;
  visitedQuestionIds: string[];
  elapsedSeconds: number;
}): boolean {
  return hasPracticeData(state) || state.elapsedSeconds > 0 || state.visitedQuestionIds.length > 0;
}

function buildWorkshopProgressMeta(
  totalQuestions: number,
  state: Pick<WorkshopPracticeState, 'questionIndex' | 'evaluationByQuestion' | 'updatedAt'>,
): WorkshopProgressMeta {
  const resumeQuestionIndex =
    totalQuestions > 0 ? Math.max(0, Math.min(state.questionIndex, totalQuestions - 1)) : 0;
  const evaluatedCount = Object.keys(state.evaluationByQuestion).length;
  const completionPercent =
    totalQuestions > 0 ? Math.min(100, Math.round((evaluatedCount / totalQuestions) * 100)) : 0;

  return {
    completionPercent,
    resumeQuestionIndex,
    evaluatedCount,
    updatedAt: state.updatedAt,
  };
}

function buildSessionRecommendation(params: {
  scorePercent: number;
  wrongCount: number;
  pendingCount: number;
}): SessionRecommendation {
  const { scorePercent, wrongCount, pendingCount } = params;

  if (pendingCount > 0) {
    return {
      title: 'Completar evaluación',
      detail: `Te faltan ${pendingCount} preguntas por comprobar. Termínalas para cerrar el diagnóstico.`,
    };
  }

  if (wrongCount === 0) {
    return {
      title: 'Excelente cierre',
      detail: 'Terminaste sin errores. Repite el taller mañana para consolidar retención.',
    };
  }

  if (scorePercent >= 80) {
    return {
      title: 'Buen resultado, ajusta precisión',
      detail: `Repite solo las ${wrongCount} preguntas incorrectas para subir a 100%.`,
    };
  }

  if (scorePercent >= 60) {
    return {
      title: 'Base aceptable, falta consistencia',
      detail: `Prioriza las ${wrongCount} preguntas falladas y vuelve a resolver todo el bloque.`,
    };
  }

  return {
    title: 'Refuerzo recomendado',
    detail: `Tu sesión cerró en ${scorePercent}%. Repite este taller completo antes de pasar al siguiente.`,
  };
}

function formatDuration(totalSeconds: number): string {
  const safe = Math.max(0, Math.floor(totalSeconds));
  const minutes = Math.floor(safe / 60);
  const seconds = safe % 60;
  return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

function extractHostFromUrl(url: string): string | null {
  try {
    const parsed = new URL(url);
    return parsed.hostname || null;
  } catch {
    return null;
  }
}

function isLanHost(host: string): boolean {
  if (host === 'localhost' || host === '127.0.0.1') {
    return false;
  }

  if (host.startsWith('192.168.')) {
    return true;
  }

  if (host.startsWith('10.')) {
    return true;
  }

  const match = host.match(/^172\.(\d+)\./);
  if (!match) {
    return false;
  }

  const secondOctet = Number(match[1]);
  return Number.isFinite(secondOctet) && secondOctet >= 16 && secondOctet <= 31;
}

function resolvePreferredBaseUrl(savedUrl: string | null, detectedUrl: string | null): string {
  if (!savedUrl && detectedUrl) {
    return detectedUrl;
  }

  if (!savedUrl) {
    return DEFAULT_BASE_URL;
  }

  if (!detectedUrl) {
    return savedUrl;
  }

  const savedHost = extractHostFromUrl(savedUrl);
  const detectedHost = extractHostFromUrl(detectedUrl);

  if (!savedHost || !detectedHost) {
    return savedUrl;
  }

  if (savedHost === detectedHost) {
    return savedUrl;
  }

  // In device testing, LAN host from Expo is usually the most reliable source.
  if (savedHost === 'localhost' || savedHost === '127.0.0.1') {
    return detectedUrl;
  }

  if (isLanHost(savedHost) && isLanHost(detectedHost)) {
    return detectedUrl;
  }

  return savedUrl;
}

function detectLanApiBaseUrl(): string | null {
  const scriptUrl = (NativeModules as { SourceCode?: { scriptURL?: string } })?.SourceCode?.scriptURL;
  if (!scriptUrl || typeof scriptUrl !== 'string') {
    return null;
  }

  const hostMatch = scriptUrl.match(/^(?:https?|exp|exps):\/\/([^/:]+):\d+/i);
  const host = hostMatch?.[1];
  if (!host || host === 'localhost' || host === '127.0.0.1') {
    return null;
  }

  return `http://${host}:8080/api/v1`;
}

function hydratePracticeState(
  detail: WorkshopDetail,
  persisted: Awaited<ReturnType<typeof loadWorkshopPracticeState>>,
): HydratedPracticeState {
  const questionById = new Map(detail.questions.map((question) => [question.id, question]));

  const selectedOptionByQuestion: Record<string, string> = {};
  const persistedSelected = persisted?.selectedOptionByQuestion ?? {};

  for (const [questionId, optionId] of Object.entries(persistedSelected)) {
    if (typeof optionId !== 'string') {
      continue;
    }

    const question = questionById.get(questionId);
    if (!question) {
      continue;
    }

    if (!question.options.some((option) => option.id === optionId)) {
      continue;
    }

    selectedOptionByQuestion[questionId] = optionId;
  }

  const evaluationByQuestion: Record<string, WorkshopEvaluationResult> = {};
  const persistedEvaluation = persisted?.evaluationByQuestion ?? {};

  for (const [questionId, evaluation] of Object.entries(persistedEvaluation)) {
    const question = questionById.get(questionId);
    if (!question || typeof evaluation !== 'object' || evaluation === null) {
      continue;
    }

    const selectedOptionId =
      typeof evaluation.selected_option_id === 'string' ? evaluation.selected_option_id : '';
    if (!selectedOptionId || !question.options.some((option) => option.id === selectedOptionId)) {
      continue;
    }

    const correctOptionId =
      typeof evaluation.correct_option_id === 'string' || evaluation.correct_option_id === null
        ? evaluation.correct_option_id
        : null;

    if (
      typeof correctOptionId === 'string' &&
      !question.options.some((option) => option.id === correctOptionId)
    ) {
      continue;
    }

    evaluationByQuestion[questionId] = {
      workshop_id: detail.id,
      question_id: questionId,
      selected_option_id: selectedOptionId,
      correct_option_id: correctOptionId,
      is_correct: Boolean(evaluation.is_correct),
      feedback_mdx: typeof evaluation.feedback_mdx === 'string' ? evaluation.feedback_mdx : '',
      feedback_assets: Array.isArray(evaluation.feedback_assets) ? evaluation.feedback_assets : [],
      feedback_blocks: Array.isArray(evaluation.feedback_blocks) ? evaluation.feedback_blocks : [],
      next_question_id:
        typeof evaluation.next_question_id === 'string' || evaluation.next_question_id === null
          ? evaluation.next_question_id
          : null,
    };
  }

  const totalQuestions = detail.questions.length;
  const persistedIndex = persisted?.questionIndex ?? 0;
  const boundedQuestionIndex =
    totalQuestions > 0
      ? Math.max(0, Math.min(Number.isFinite(persistedIndex) ? persistedIndex : 0, totalQuestions - 1))
      : 0;

  const visitedQuestionIds = Array.isArray(persisted?.visitedQuestionIds)
    ? persisted.visitedQuestionIds.filter((id) => typeof id === 'string' && questionById.has(id))
    : [];

  return {
    questionIndex: boundedQuestionIndex,
    selectedOptionByQuestion,
    evaluationByQuestion,
    visitedQuestionIds,
    elapsedSeconds:
      typeof persisted?.elapsedSeconds === 'number' && Number.isFinite(persisted.elapsedSeconds)
        ? Math.max(0, Math.floor(persisted.elapsedSeconds))
        : 0,
    timerRunning: typeof persisted?.timerRunning === 'boolean' ? persisted.timerRunning : true,
  };
}

export default function App() {
  const [detectedLanBaseUrl] = useState<string | null>(() => detectLanApiBaseUrl());
  const [baseUrl, setBaseUrl] = useState(() =>
    resolvePreferredBaseUrl(null, detectLanApiBaseUrl()),
  );
  const [email, setEmail] = useState('demo@ediprofe.com');
  const [password, setPassword] = useState('Demo12345!');
  const [token, setToken] = useState<string | null>(null);

  const [workshops, setWorkshops] = useState<WorkshopSummary[]>([]);
  const [selectedWorkshopId, setSelectedWorkshopId] = useState<string | null>(null);
  const [selectedWorkshop, setSelectedWorkshop] = useState<WorkshopDetail | null>(null);

  const [questionIndex, setQuestionIndex] = useState(0);
  const [selectedOptionByQuestion, setSelectedOptionByQuestion] = useState<Record<string, string>>({});
  const [evaluationByQuestion, setEvaluationByQuestion] = useState<Record<string, WorkshopEvaluationResult>>({});
  const [visitedQuestionIds, setVisitedQuestionIds] = useState<string[]>([]);
  const [elapsedSeconds, setElapsedSeconds] = useState(0);
  const [timerRunning, setTimerRunning] = useState(false);
  const [showResultScreen, setShowResultScreen] = useState(false);
  const [strictModeEnabled, setStrictModeEnabled] = useState(false);
  const [reviewModeActive, setReviewModeActive] = useState(false);
  const [reviewQuestionIds, setReviewQuestionIds] = useState<string[]>([]);
  const [reviewCursor, setReviewCursor] = useState(0);
  const [progressByWorkshopId, setProgressByWorkshopId] = useState<Record<string, WorkshopProgressMeta>>({});
  const [resumeNotice, setResumeNotice] = useState<string | null>(null);

  const [loadingCatalog, setLoadingCatalog] = useState(false);
  const [loadingWorkshop, setLoadingWorkshop] = useState(false);
  const [submittingAnswer, setSubmittingAnswer] = useState(false);

  const [detailAccessError, setDetailAccessError] = useState<DetailAccessError>(null);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const apiLooksLoopback = /127\.0\.0\.1|localhost/i.test(baseUrl);

  useEffect(() => {
    let mounted = true;

    const bootstrap = async () => {
      const [savedUrl, savedToken] = await Promise.all([loadBaseUrl(), loadSessionToken()]);
      const preferredUrl = resolvePreferredBaseUrl(savedUrl, detectedLanBaseUrl);

      if (!mounted) {
        return;
      }

      if (preferredUrl) {
        setBaseUrl(preferredUrl);
        if (preferredUrl !== savedUrl) {
          await saveBaseUrl(preferredUrl);
        }
      }

      if (!savedToken) {
        return;
      }

      try {
        await getCurrentUser(preferredUrl, savedToken);
        setToken(savedToken);
      } catch {
        await clearSessionToken();
      }
    };

    void bootstrap();

    return () => {
      mounted = false;
    };
  }, [detectedLanBaseUrl]);

  const refreshCatalog = useCallback(async () => {
    setLoadingCatalog(true);
    setErrorMessage(null);

    try {
      await saveBaseUrl(baseUrl);
      const response = await listWorkshops(baseUrl, token ?? undefined);
      setWorkshops(response.data);
      const persistedMap = await loadWorkshopPracticeStateMap(response.data.map((workshop) => workshop.id));
      const progressMap: Record<string, WorkshopProgressMeta> = {};

      response.data.forEach((workshop) => {
        const state = persistedMap[workshop.id];
        if (!state || !hasPracticeData(state)) {
          return;
        }

        progressMap[workshop.id] = buildWorkshopProgressMeta(workshop.stats.total_questions, state);
      });

      setProgressByWorkshopId(progressMap);

      const selectedExists = selectedWorkshopId
        ? response.data.some((item) => item.id === selectedWorkshopId)
        : false;

      if (selectedExists) {
        return;
      }

      const firstId = response.data[0]?.id ?? null;
      setSelectedWorkshopId(firstId);
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : 'No fue posible cargar catálogo.');
    } finally {
      setLoadingCatalog(false);
    }
  }, [baseUrl, selectedWorkshopId, token]);

  useEffect(() => {
    void refreshCatalog();
  }, [refreshCatalog]);

  const loadWorkshopDetail = useCallback(
    async (workshopId: string) => {
      setLoadingWorkshop(true);
      setErrorMessage(null);
      setDetailAccessError(null);
      setResumeNotice(null);

      try {
        const detail = await getWorkshop(baseUrl, workshopId, token ?? undefined);
        const persisted = await loadWorkshopPracticeState(workshopId);
        const hydrated = hydratePracticeState(detail, persisted);

        setSelectedWorkshop(detail);
        setQuestionIndex(hydrated.questionIndex);
        setSelectedOptionByQuestion(hydrated.selectedOptionByQuestion);
        setEvaluationByQuestion(hydrated.evaluationByQuestion);
        setVisitedQuestionIds(hydrated.visitedQuestionIds);
        setElapsedSeconds(hydrated.elapsedSeconds);
        setTimerRunning(hydrated.timerRunning);
        setShowResultScreen(false);
        setReviewModeActive(false);
        setReviewQuestionIds([]);
        setReviewCursor(0);
        if (hasPracticeData(hydrated)) {
          setResumeNotice(`Reanudaste en la pregunta ${hydrated.questionIndex + 1}.`);
        }
      } catch (error) {
        setSelectedWorkshop(null);
        setQuestionIndex(0);
        setSelectedOptionByQuestion({});
        setEvaluationByQuestion({});
        setVisitedQuestionIds([]);
        setElapsedSeconds(0);
        setTimerRunning(false);
        setShowResultScreen(false);
        setReviewModeActive(false);
        setReviewQuestionIds([]);
        setReviewCursor(0);
        setResumeNotice(null);

        if (
          error instanceof ApiRequestError &&
          (error.code === 'auth_required' || error.code === 'premium_access_required')
        ) {
          setDetailAccessError(error.code);
          setErrorMessage(error.message);
          return;
        }

        setErrorMessage(error instanceof Error ? error.message : 'No fue posible cargar el taller.');
      } finally {
        setLoadingWorkshop(false);
      }
    },
    [baseUrl, token],
  );

  useEffect(() => {
    if (!selectedWorkshopId) {
      return;
    }

    void loadWorkshopDetail(selectedWorkshopId);
  }, [loadWorkshopDetail, selectedWorkshopId]);

  const handlePressWorkshop = useCallback((workshopId: string) => {
    setSelectedWorkshopId(workshopId);
  }, []);

  useEffect(() => {
    if (!selectedWorkshop) {
      return;
    }

    const timer = setTimeout(() => {
      const snapshot = {
        questionIndex,
        selectedOptionByQuestion,
        evaluationByQuestion,
        visitedQuestionIds,
        elapsedSeconds,
        timerRunning,
      };

      if (!hasPersistableState(snapshot)) {
        void clearWorkshopPracticeState(selectedWorkshop.id);
        setProgressByWorkshopId((prev) => {
          if (!(selectedWorkshop.id in prev)) {
            return prev;
          }

          const clone = { ...prev };
          delete clone[selectedWorkshop.id];
          return clone;
        });
        return;
      }

      const updatedAt = new Date().toISOString();
      void saveWorkshopPracticeState(selectedWorkshop.id, snapshot);
      setProgressByWorkshopId((prev) => ({
        ...prev,
        [selectedWorkshop.id]: buildWorkshopProgressMeta(selectedWorkshop.stats.total_questions, {
          questionIndex,
          evaluationByQuestion,
          updatedAt,
        }),
      }));
    }, 180);

    return () => {
      clearTimeout(timer);
    };
  }, [
    elapsedSeconds,
    evaluationByQuestion,
    questionIndex,
    selectedOptionByQuestion,
    selectedWorkshop,
    timerRunning,
    visitedQuestionIds,
  ]);

  const handleResetProgress = useCallback(async () => {
    if (!selectedWorkshop) {
      return;
    }

    await clearWorkshopPracticeState(selectedWorkshop.id);
    setQuestionIndex(0);
    setSelectedOptionByQuestion({});
    setEvaluationByQuestion({});
    setVisitedQuestionIds([]);
    setElapsedSeconds(0);
    setTimerRunning(true);
    setShowResultScreen(false);
    setReviewModeActive(false);
    setReviewQuestionIds([]);
    setReviewCursor(0);
    setResumeNotice('Progreso reiniciado.');
    setProgressByWorkshopId((prev) => {
      if (!(selectedWorkshop.id in prev)) {
        return prev;
      }

      const clone = { ...prev };
      delete clone[selectedWorkshop.id];
      return clone;
    });
  }, [selectedWorkshop]);

  const handleLogin = useCallback(async () => {
    setErrorMessage(null);
    setLoadingCatalog(true);

    try {
      if (!email.trim() || !password.trim()) {
        throw new Error('Escribe email y password.');
      }

      const session = await login(baseUrl, {
        email: email.trim(),
        password,
        deviceName: 'expo-mobile',
      });

      setToken(session.token);
      await saveSessionToken(session.token);
      await saveBaseUrl(baseUrl);
      await refreshCatalog();
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : 'No fue posible iniciar sesión.');
    } finally {
      setLoadingCatalog(false);
    }
  }, [baseUrl, email, password, refreshCatalog]);

  const handleLogout = useCallback(async () => {
    setErrorMessage(null);
    setLoadingCatalog(true);

    try {
      if (token) {
        await logout(baseUrl, token);
      }

      setToken(null);
      await clearSessionToken();
      await refreshCatalog();
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : 'No fue posible cerrar sesión.');
    } finally {
      setLoadingCatalog(false);
    }
  }, [baseUrl, refreshCatalog, token]);

  const currentQuestion = useMemo(() => {
    if (!selectedWorkshop || selectedWorkshop.questions.length === 0) {
      return null;
    }

    const boundedIndex = Math.max(0, Math.min(questionIndex, selectedWorkshop.questions.length - 1));
    return selectedWorkshop.questions[boundedIndex] ?? null;
  }, [questionIndex, selectedWorkshop]);

  const totalQuestions = selectedWorkshop?.questions.length ?? 0;
  const progressValue = totalQuestions > 0 ? (questionIndex + 1) / totalQuestions : 0;
  const sessionDurationSeconds = useMemo(
    () =>
      selectedWorkshop
        ? strictModeEnabled
          ? STRICT_MODE_DURATION_SECONDS
          : Math.max(MIN_SESSION_DURATION_SECONDS, selectedWorkshop.questions.length * PER_QUESTION_SECONDS)
        : 0,
    [selectedWorkshop, strictModeEnabled],
  );
  const remainingSeconds = Math.max(0, sessionDurationSeconds - elapsedSeconds);
  const timerExpired = sessionDurationSeconds > 0 && remainingSeconds === 0;
  const evaluatedCount = useMemo(
    () => Object.keys(evaluationByQuestion).length,
    [evaluationByQuestion],
  );
  const visitedCount = useMemo(() => {
    if (!selectedWorkshop) {
      return 0;
    }

    const allowedIds = new Set(selectedWorkshop.questions.map((question) => question.id));
    return visitedQuestionIds.filter((id) => allowedIds.has(id)).length;
  }, [selectedWorkshop, visitedQuestionIds]);
  const correctCount = useMemo(
    () => Object.values(evaluationByQuestion).filter((item) => item.is_correct).length,
    [evaluationByQuestion],
  );
  const wrongCount = Math.max(0, evaluatedCount - correctCount);
  const pendingEvaluationCount = Math.max(0, totalQuestions - evaluatedCount);
  const pendingVisitCount = Math.max(0, totalQuestions - visitedCount);
  const scorePercent = totalQuestions > 0 ? Math.round((correctCount / totalQuestions) * 100) : 0;
  const sessionCompleted = totalQuestions > 0 && evaluatedCount === totalQuestions;
  const sessionFinished = sessionCompleted || timerExpired;
  const blockedByTimer = timerExpired && !reviewModeActive;
  const pendingQuestionIdsInOrder = useMemo(() => {
    if (!selectedWorkshop) {
      return [];
    }

    return selectedWorkshop.questions
      .filter((question) => !evaluationByQuestion[question.id])
      .map((question) => question.id);
  }, [evaluationByQuestion, selectedWorkshop]);
  const wrongQuestionIdsInOrder = useMemo(() => {
    if (!selectedWorkshop) {
      return [];
    }

    return selectedWorkshop.questions
      .filter((question) => {
        const evaluation = evaluationByQuestion[question.id];
        return Boolean(evaluation && !evaluation.is_correct);
      })
      .map((question) => question.id);
  }, [evaluationByQuestion, selectedWorkshop]);

  const sessionRecommendation = useMemo(
    () =>
      buildSessionRecommendation({
        scorePercent,
        wrongCount,
        pendingCount: pendingEvaluationCount,
      }),
    [pendingEvaluationCount, scorePercent, wrongCount],
  );

  useEffect(() => {
    if (!selectedWorkshop || !timerRunning || timerExpired || showResultScreen) {
      return;
    }

    const timer = setInterval(() => {
      setElapsedSeconds((prev) => prev + 1);
    }, 1000);

    return () => {
      clearInterval(timer);
    };
  }, [selectedWorkshop, showResultScreen, timerExpired, timerRunning]);

  useEffect(() => {
    if (!selectedWorkshop) {
      return;
    }

    if (sessionFinished && timerRunning) {
      setTimerRunning(false);
    }

    if (sessionFinished && !reviewModeActive) {
      setShowResultScreen(true);
    }
  }, [reviewModeActive, selectedWorkshop, sessionFinished, timerRunning]);

  const currentQuestionId = currentQuestion?.id ?? null;
  const selectedOptionId = currentQuestionId ? selectedOptionByQuestion[currentQuestionId] : undefined;
  const evaluation = currentQuestionId ? evaluationByQuestion[currentQuestionId] : undefined;
  const currentQuestionEvaluated = Boolean(currentQuestionId && evaluationByQuestion[currentQuestionId]);
  const canGoPrev = reviewModeActive ? reviewCursor > 0 : questionIndex > 0;
  const canGoNext = reviewModeActive
    ? reviewCursor < reviewQuestionIds.length - 1
    : questionIndex < totalQuestions - 1;
  const canAdvance = reviewModeActive
    ? canGoNext
    : totalQuestions > 0 && (!strictModeEnabled || currentQuestionEvaluated);
  const canEvaluate = Boolean(selectedOptionId) && !submittingAnswer && !blockedByTimer;

  useEffect(() => {
    if (!currentQuestionId || showResultScreen) {
      return;
    }

    setVisitedQuestionIds((prev) => (prev.includes(currentQuestionId) ? prev : [...prev, currentQuestionId]));
  }, [currentQuestionId, showResultScreen]);

  const handleSelectOption = useCallback((optionId: string) => {
    if (!currentQuestion) {
      return;
    }

    const questionId = currentQuestion.id;

    setSelectedOptionByQuestion((prev) => ({
      ...prev,
      [questionId]: optionId,
    }));

    setEvaluationByQuestion((prev) => {
      if (!prev[questionId]) {
        return prev;
      }

      const clone = { ...prev };
      delete clone[questionId];
      return clone;
    });
  }, [currentQuestion]);

  const handleEvaluate = useCallback(async () => {
    if (!selectedWorkshop || !currentQuestion || !selectedOptionId || blockedByTimer) {
      return;
    }

    setSubmittingAnswer(true);
    setErrorMessage(null);

    try {
      const result = await evaluateWorkshopAnswer(
        baseUrl,
        selectedWorkshop.id,
        currentQuestion.id,
        selectedOptionId,
        token ?? undefined,
      );

      setEvaluationByQuestion((prev) => ({
        ...prev,
        [result.question_id]: result,
      }));

      if (reviewModeActive && result.is_correct) {
        const updatedReviewIds = reviewQuestionIds.filter((id) => id !== result.question_id);
        setReviewQuestionIds(updatedReviewIds);

        if (updatedReviewIds.length === 0) {
          setReviewModeActive(false);
          setShowResultScreen(true);
          setResumeNotice('Repaso completado.');
          return;
        }

        const nextCursor = Math.min(reviewCursor, updatedReviewIds.length - 1);
        const nextQuestionId = updatedReviewIds[nextCursor];
        const nextQuestionIndex = selectedWorkshop.questions.findIndex(
          (question) => question.id === nextQuestionId,
        );

        setReviewCursor(nextCursor);
        if (nextQuestionIndex >= 0) {
          setQuestionIndex(nextQuestionIndex);
        }
      }
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : 'No fue posible evaluar la respuesta.');
    } finally {
      setSubmittingAnswer(false);
    }
  }, [
    baseUrl,
    blockedByTimer,
    currentQuestion,
    reviewCursor,
    reviewModeActive,
    reviewQuestionIds,
    selectedOptionId,
    selectedWorkshop,
    token,
  ]);

  const goPrev = useCallback(() => {
    if (!selectedWorkshop) {
      return;
    }

    if (reviewModeActive) {
      if (reviewQuestionIds.length === 0) {
        return;
      }
      const nextCursor = Math.max(0, reviewCursor - 1);
      const questionId = reviewQuestionIds[nextCursor];
      const nextQuestionIndex = selectedWorkshop.questions.findIndex((question) => question.id === questionId);
      setReviewCursor(nextCursor);
      if (nextQuestionIndex >= 0) {
        setQuestionIndex(nextQuestionIndex);
      }
      return;
    }

    setQuestionIndex((prev) => Math.max(0, prev - 1));
  }, [reviewCursor, reviewModeActive, reviewQuestionIds, selectedWorkshop]);

  const goNext = useCallback(() => {
    if (!selectedWorkshop) {
      return;
    }

    if (reviewModeActive) {
      if (reviewQuestionIds.length === 0) {
        return;
      }
      const nextCursor = Math.min(reviewQuestionIds.length - 1, reviewCursor + 1);
      const questionId = reviewQuestionIds[nextCursor];
      const nextQuestionIndex = selectedWorkshop.questions.findIndex((question) => question.id === questionId);
      setReviewCursor(nextCursor);
      if (nextQuestionIndex >= 0) {
        setQuestionIndex(nextQuestionIndex);
      }
      return;
    }

    setQuestionIndex((prev) => Math.min(selectedWorkshop.questions.length - 1, prev + 1));
  }, [reviewCursor, reviewModeActive, reviewQuestionIds, selectedWorkshop]);

  const openResultScreen = useCallback(() => {
    setTimerRunning(false);
    setShowResultScreen(true);
  }, []);

  const handleAdvance = useCallback(() => {
    if (reviewModeActive) {
      goNext();
      return;
    }

    if (strictModeEnabled && !currentQuestionEvaluated) {
      setResumeNotice('Modo examen activo: primero debes comprobar esta pregunta.');
      return;
    }

    if (questionIndex >= totalQuestions - 1) {
      openResultScreen();
      return;
    }

    goNext();
  }, [
    currentQuestionEvaluated,
    goNext,
    openResultScreen,
    questionIndex,
    reviewModeActive,
    strictModeEnabled,
    totalQuestions,
  ]);

  const goToNextPending = useCallback(() => {
    if (!selectedWorkshop || pendingQuestionIdsInOrder.length === 0) {
      return;
    }

    const nextPendingId = pendingQuestionIdsInOrder[0];
    const nextPendingIndex = selectedWorkshop.questions.findIndex((question) => question.id === nextPendingId);
    if (nextPendingIndex < 0) {
      return;
    }

    setReviewModeActive(false);
    setReviewQuestionIds([]);
    setReviewCursor(0);
    setQuestionIndex(nextPendingIndex);
    setShowResultScreen(false);
    setResumeNotice(`Pendiente seleccionada: pregunta ${nextPendingIndex + 1}.`);
  }, [pendingQuestionIdsInOrder, selectedWorkshop]);

  const startWrongReview = useCallback(() => {
    if (!selectedWorkshop || wrongQuestionIdsInOrder.length === 0) {
      return;
    }

    const firstWrongId = wrongQuestionIdsInOrder[0];
    const firstWrongIndex = selectedWorkshop.questions.findIndex((question) => question.id === firstWrongId);

    setReviewModeActive(true);
    setReviewQuestionIds(wrongQuestionIdsInOrder);
    setReviewCursor(0);
    if (firstWrongIndex >= 0) {
      setQuestionIndex(firstWrongIndex);
    }
    setShowResultScreen(false);
    setResumeNotice(`Repaso activo: ${wrongQuestionIdsInOrder.length} preguntas con error.`);
  }, [selectedWorkshop, wrongQuestionIdsInOrder]);

  const stopWrongReview = useCallback(() => {
    setReviewModeActive(false);
    setReviewQuestionIds([]);
    setReviewCursor(0);
    setShowResultScreen(true);
  }, []);

  const toggleStrictMode = useCallback(() => {
    if (reviewModeActive) {
      return;
    }

    setStrictModeEnabled((prev) => {
      const next = !prev;
      setResumeNotice(
        next
          ? 'Modo examen activo: no puedes avanzar sin comprobar.'
          : 'Modo práctica activo: puedes navegar libremente.',
      );
      return next;
    });
  }, [reviewModeActive]);

  const title = selectedWorkshop
    ? `${selectedWorkshop.title} (${selectedWorkshop.stats.total_questions} preguntas)`
    : 'Selecciona un taller';

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar style="light" />
      <ScrollView style={styles.root} contentContainerStyle={styles.rootContent}>
        <View style={styles.page}>
          <View style={styles.heroCard}>
            <Text style={styles.h1}>Ediprofe Mobile</Text>
            <Text style={styles.subtitle}>Práctica guiada tipo Saber con retroalimentación inmediata.</Text>
            <View style={styles.heroBadges}>
              <Text style={[styles.heroBadge, token ? styles.heroBadgeOk : styles.heroBadgeWarn]}>
                {token ? 'Sesión activa' : 'Sesión anónima'}
              </Text>
              <Text style={[styles.heroBadge, strictModeEnabled ? styles.heroBadgeOk : styles.heroBadgeInfo]}>
                {strictModeEnabled ? 'Modo examen ON' : 'Modo práctica'}
              </Text>
            </View>
          </View>

          <View style={styles.panel}>
          <Text style={styles.label}>API Base URL</Text>
          <TextInput
            style={styles.input}
            value={baseUrl}
            onChangeText={setBaseUrl}
            autoCapitalize="none"
            autoCorrect={false}
          />

          <View style={styles.row}>
            <TextInput
              style={[styles.input, styles.grow]}
              placeholder="email"
              placeholderTextColor="#8195be"
              value={email}
              onChangeText={setEmail}
              autoCapitalize="none"
              autoCorrect={false}
            />
            <TextInput
              style={[styles.input, styles.grow]}
              placeholder="password"
              placeholderTextColor="#8195be"
              value={password}
              onChangeText={setPassword}
              secureTextEntry
            />
          </View>

          <View style={styles.row}>
            <Pressable style={styles.buttonPrimary} onPress={handleLogin}>
              <Text style={styles.buttonText}>Login</Text>
            </Pressable>
            <Pressable style={styles.buttonGhost} onPress={handleLogout}>
              <Text style={styles.buttonText}>Logout</Text>
            </Pressable>
            <Pressable style={styles.buttonGhost} onPress={() => void refreshCatalog()}>
              <Text style={styles.buttonText}>Refresh</Text>
            </Pressable>
          </View>

          <Text style={styles.meta}>Token: {token ? 'activo' : 'anónimo'}</Text>
          {detectedLanBaseUrl && baseUrl.trim() !== detectedLanBaseUrl ? (
            <View style={styles.detectedUrlRow}>
              <Text style={styles.detectedUrlText}>URL detectada: {detectedLanBaseUrl}</Text>
              <Pressable style={styles.detectedUrlButton} onPress={() => setBaseUrl(detectedLanBaseUrl)}>
                <Text style={styles.detectedUrlButtonText}>Usar detectada</Text>
              </Pressable>
            </View>
          ) : null}
          {apiLooksLoopback ? (
            <Text style={styles.warning}>
              En celular no uses 127.0.0.1/localhost. Usa la IP LAN de tu Mac.
            </Text>
          ) : null}
          {errorMessage ? <Text style={styles.error}>{errorMessage}</Text> : null}
        </View>

          <View style={styles.panel}>
          <Text style={styles.sectionTitle}>Catálogo</Text>
          {loadingCatalog ? <ActivityIndicator color="#9ac0ff" style={styles.loader} /> : null}
          <FlatList
            data={workshops}
            keyExtractor={(item) => item.id}
            horizontal
            showsHorizontalScrollIndicator={false}
            contentContainerStyle={styles.catalogRow}
            renderItem={({ item }) => (
              <View style={styles.catalogCardWrap}>
                <WorkshopCard
                  item={item}
                  isSelected={item.id === selectedWorkshopId}
                  onPress={handlePressWorkshop}
                  progress={progressByWorkshopId[item.id] ?? null}
                />
              </View>
            )}
          />
          </View>

          <View style={styles.panel}>
          <Text style={styles.sectionTitle}>{title}</Text>

          {loadingWorkshop ? <ActivityIndicator color="#9ac0ff" style={styles.loader} /> : null}

          {!selectedWorkshop && detailAccessError === 'auth_required' ? (
            <View style={styles.emptyState}>
              <Text style={styles.emptyTitle}>Taller premium bloqueado</Text>
              <Text style={styles.emptyText}>
                Inicia sesión con una cuenta autorizada para desbloquear preguntas y retroalimentación.
              </Text>
            </View>
          ) : null}

          {!selectedWorkshop && detailAccessError === 'premium_access_required' ? (
            <View style={styles.emptyState}>
              <Text style={styles.emptyTitle}>Tu cuenta no tiene este acceso</Text>
              <Text style={styles.emptyText}>
                Este taller requiere una suscripción premium o un acceso institucional activo.
              </Text>
            </View>
          ) : null}

          {selectedWorkshop ? (
            <View style={styles.modeRow}>
              <View style={styles.modeTextWrap}>
                <Text style={styles.modeTitle}>Modo examen</Text>
                <Text style={styles.modeDescription}>
                  {strictModeEnabled
                    ? `Activo · tiempo fijo ${formatDuration(sessionDurationSeconds)} · avance bloqueado sin comprobar`
                    : 'Desactivado · modo práctica con navegación libre'}
                </Text>
              </View>
              <Pressable
                style={[
                  styles.modeToggle,
                  strictModeEnabled ? styles.modeToggleOn : styles.modeToggleOff,
                  reviewModeActive ? styles.controlDisabled : null,
                ]}
                onPress={toggleStrictMode}
                disabled={reviewModeActive}
              >
                <Text style={styles.modeToggleText}>{strictModeEnabled ? 'ON' : 'OFF'}</Text>
              </Pressable>
            </View>
          ) : null}

          {selectedWorkshop && showResultScreen ? (
            <View style={styles.resultScreenCard}>
              <View style={styles.resultHeader}>
                <Text style={styles.resultTitle}>
                  {sessionCompleted ? 'Resultado final' : 'Resultado parcial'}
                </Text>
                <Text style={styles.resultScore}>{scorePercent}%</Text>
              </View>
              <Text style={styles.resultMeta}>
                Tiempo: {formatDuration(elapsedSeconds)} / {formatDuration(sessionDurationSeconds)}
              </Text>
              <Text style={styles.resultMeta}>
                {correctCount} correctas · {wrongCount} incorrectas · {pendingEvaluationCount} sin comprobar
              </Text>
              <Text style={styles.resultMeta}>
                {visitedCount} visitadas · {pendingVisitCount} por visitar
              </Text>
              {timerExpired ? <Text style={styles.timerExpiredText}>Tiempo agotado para esta sesión.</Text> : null}
              <Text style={styles.resultRecommendationTitle}>{sessionRecommendation.title}</Text>
              <Text style={styles.resultRecommendationText}>{sessionRecommendation.detail}</Text>

              <View style={styles.resultActionsRow}>
                <Pressable
                  style={[
                    styles.resultActionButton,
                    pendingQuestionIdsInOrder.length === 0 ? styles.controlDisabled : null,
                  ]}
                  onPress={goToNextPending}
                  disabled={pendingQuestionIdsInOrder.length === 0}
                >
                  <Text style={styles.resultActionText}>
                    Resolver pendientes ({pendingQuestionIdsInOrder.length})
                  </Text>
                </Pressable>
                <Pressable
                  style={[
                    styles.resultActionButton,
                    wrongQuestionIdsInOrder.length === 0 ? styles.controlDisabled : null,
                  ]}
                  onPress={startWrongReview}
                  disabled={wrongQuestionIdsInOrder.length === 0}
                >
                  <Text style={styles.resultActionText}>
                    Repasar incorrectas ({wrongQuestionIdsInOrder.length})
                  </Text>
                </Pressable>
                <Pressable style={styles.resultActionButtonSecondary} onPress={() => setShowResultScreen(false)}>
                  <Text style={styles.resultActionText}>Volver a preguntas</Text>
                </Pressable>
                <Pressable style={styles.resultActionButtonSecondary} onPress={() => void handleResetProgress()}>
                  <Text style={styles.resultActionText}>Reiniciar sesión</Text>
                </Pressable>
              </View>
            </View>
          ) : null}

          {selectedWorkshop && currentQuestion && !showResultScreen ? (
            <View style={styles.practiceCard}>
              <View style={styles.progressHeader}>
                <Text style={styles.progressTitle}>
                  {reviewModeActive
                    ? `Repaso ${reviewCursor + 1} de ${reviewQuestionIds.length}`
                    : `Pregunta ${questionIndex + 1} de ${totalQuestions}`}
                </Text>
                <Text style={styles.progressCounter}>{Math.round(progressValue * 100)}%</Text>
              </View>
              <View style={styles.metricsRow}>
                <Text style={[styles.metricPill, styles.metricGood]}>Correctas: {correctCount}</Text>
                <Text style={[styles.metricPill, styles.metricBad]}>Incorrectas: {wrongCount}</Text>
                <Text style={[styles.metricPill, styles.metricPending]}>
                  Sin comprobar: {pendingEvaluationCount}
                </Text>
                <Text style={[styles.metricPill, styles.metricVisit]}>
                  Por visitar: {pendingVisitCount}
                </Text>
                <Text style={[styles.metricPill, timerExpired ? styles.metricBad : styles.metricTimer]}>
                  Tiempo: {formatDuration(remainingSeconds)}
                </Text>
              </View>

              <View style={styles.progressTrack}>
                <View style={[styles.progressFill, { width: `${progressValue * 100}%` }]} />
              </View>
              <View style={styles.resumeRow}>
                <Text style={styles.resumeText}>{resumeNotice ?? ' '}</Text>
                <View style={styles.resumeActions}>
                  {reviewModeActive ? (
                    <Pressable style={styles.resetProgressButton} onPress={stopWrongReview}>
                      <Text style={styles.resetProgressText}>Salir repaso</Text>
                    </Pressable>
                  ) : null}
                  <Pressable style={styles.resetProgressButton} onPress={() => void handleResetProgress()}>
                    <Text style={styles.resetProgressText}>Reiniciar progreso</Text>
                  </Pressable>
                </View>
              </View>

              {blockedByTimer ? (
                <Text style={styles.timerExpiredText}>
                  Tiempo agotado. Revisa resultados o inicia repaso de incorrectas.
                </Text>
              ) : null}

              <QuestionStem
                stem={currentQuestion.stem_mdx ?? ''}
                stemAssets={currentQuestion.stem_assets}
                blocks={currentQuestion.stem_blocks}
              />

              <View style={styles.optionsWrap}>
                {currentQuestion.options.map((option) => {
                  const isSelected = selectedOptionId === option.id;
                  const isCorrectOption = evaluation?.correct_option_id === option.id;
                  const isWrongSelected =
                    evaluation !== undefined && !evaluation.is_correct && isSelected && !isCorrectOption;

                  return (
                    <Pressable
                      key={option.id}
                      onPress={() => handleSelectOption(option.id)}
                      style={[
                        styles.optionButton,
                        isSelected ? styles.optionSelected : null,
                        isCorrectOption ? styles.optionCorrect : null,
                        isWrongSelected ? styles.optionWrong : null,
                      ]}
                      disabled={submittingAnswer}
                    >
                      <Text style={styles.optionText}>
                        {option.id}. {option.text}
                      </Text>
                    </Pressable>
                  );
                })}
              </View>

              <View style={styles.controlsRow}>
                <Pressable
                  style={[styles.controlButton, !canGoPrev ? styles.controlDisabled : null]}
                  onPress={goPrev}
                  disabled={!canGoPrev}
                >
                  <Text style={styles.buttonText}>Anterior</Text>
                </Pressable>

                <Pressable
                  style={[styles.controlButtonPrimary, !canEvaluate ? styles.controlDisabled : null]}
                  onPress={handleEvaluate}
                  disabled={!canEvaluate}
                >
                  <Text style={styles.buttonText}>
                    {submittingAnswer ? 'Comprobando...' : blockedByTimer ? 'Tiempo agotado' : 'Comprobar'}
                  </Text>
                </Pressable>

                <Pressable
                  style={[styles.controlButton, !canAdvance ? styles.controlDisabled : null]}
                  onPress={handleAdvance}
                  disabled={!canAdvance}
                >
                  <Text style={styles.buttonText}>
                    {reviewModeActive
                      ? 'Siguiente'
                      : strictModeEnabled && !currentQuestionEvaluated
                        ? 'Comprobar primero'
                      : questionIndex >= totalQuestions - 1
                        ? 'Resultados'
                        : 'Siguiente'}
                  </Text>
                </Pressable>
              </View>
              {!reviewModeActive && !strictModeEnabled ? (
                <Pressable style={styles.finishSessionButton} onPress={openResultScreen}>
                  <Text style={styles.finishSessionText}>Finalizar sesión y ver resultados</Text>
                </Pressable>
              ) : null}

              {evaluation ? (
                <View style={[styles.feedbackCard, evaluation.is_correct ? styles.feedbackOk : styles.feedbackBad]}>
                  <Text style={styles.feedbackTitle}>
                    {evaluation.is_correct ? 'Respuesta correcta' : 'Respuesta incorrecta'}
                  </Text>
                  <QuestionStem
                    stem={evaluation.feedback_mdx ?? ''}
                    stemAssets={evaluation.feedback_assets}
                    blocks={evaluation.feedback_blocks}
                  />
                </View>
              ) : null}
            </View>
          ) : null}
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#070d1d',
  },
  root: {
    flex: 1,
  },
  rootContent: {
    padding: 16,
    paddingBottom: 30,
  },
  page: {
    width: '100%',
    maxWidth: 1100,
    alignSelf: 'center',
    gap: 12,
  },
  heroCard: {
    borderWidth: 1,
    borderColor: '#2a4275',
    borderRadius: 16,
    backgroundColor: '#0a1530',
    paddingHorizontal: 14,
    paddingVertical: 12,
    gap: 6,
  },
  h1: {
    color: '#f4f7ff',
    fontSize: 29,
    fontWeight: '900',
  },
  subtitle: {
    color: '#a7badf',
    fontSize: 13,
    lineHeight: 19,
  },
  heroBadges: {
    marginTop: 2,
    flexDirection: 'row',
    gap: 8,
    flexWrap: 'wrap',
  },
  heroBadge: {
    borderRadius: 999,
    paddingHorizontal: 10,
    paddingVertical: 4,
    fontSize: 11,
    fontWeight: '800',
    overflow: 'hidden',
  },
  heroBadgeOk: {
    color: '#9df0ca',
    backgroundColor: 'rgba(59, 201, 132, 0.18)',
  },
  heroBadgeWarn: {
    color: '#ffd9a0',
    backgroundColor: 'rgba(225, 159, 47, 0.18)',
  },
  heroBadgeInfo: {
    color: '#a5d0ff',
    backgroundColor: 'rgba(69, 141, 234, 0.2)',
  },
  panel: {
    borderWidth: 1,
    borderColor: '#2a4275',
    borderRadius: 16,
    padding: 12,
    gap: 10,
    backgroundColor: '#0b1734',
  },
  label: {
    color: '#dce6ff',
    fontSize: 12,
    fontWeight: '700',
  },
  input: {
    borderWidth: 1,
    borderColor: '#2a3d6a',
    borderRadius: 10,
    paddingHorizontal: 10,
    paddingVertical: 9,
    color: '#f5f8ff',
    backgroundColor: '#0a132a',
    minWidth: 120,
  },
  grow: {
    flex: 1,
  },
  row: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  meta: {
    color: '#9ab0db',
    fontSize: 12,
  },
  detectedUrlRow: {
    marginTop: 2,
    gap: 8,
  },
  detectedUrlText: {
    color: '#93c7ff',
    fontSize: 12,
    lineHeight: 18,
  },
  detectedUrlButton: {
    alignSelf: 'flex-start',
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#3264c4',
    backgroundColor: '#152c5d',
    paddingHorizontal: 10,
    paddingVertical: 7,
  },
  detectedUrlButtonText: {
    color: '#d5e6ff',
    fontSize: 12,
    fontWeight: '700',
  },
  error: {
    color: '#ff9aa4',
    fontSize: 12,
    lineHeight: 18,
  },
  warning: {
    color: '#ffd39a',
    fontSize: 12,
    lineHeight: 18,
  },
  loader: {
    marginVertical: 8,
  },
  sectionTitle: {
    color: '#eef3ff',
    fontSize: 17,
    fontWeight: '800',
  },
  catalogRow: {
    paddingRight: 6,
  },
  catalogCardWrap: {
    width: 320,
    marginRight: 10,
  },
  buttonPrimary: {
    borderRadius: 10,
    backgroundColor: '#2f6bff',
    paddingHorizontal: 14,
    paddingVertical: 10,
  },
  buttonGhost: {
    borderRadius: 10,
    backgroundColor: '#18274b',
    paddingHorizontal: 14,
    paddingVertical: 10,
  },
  buttonText: {
    color: '#eff4ff',
    fontWeight: '800',
    fontSize: 12,
  },
  emptyState: {
    borderWidth: 1,
    borderColor: '#334a7f',
    borderRadius: 12,
    backgroundColor: '#0a142b',
    padding: 14,
    gap: 8,
  },
  emptyTitle: {
    color: '#f0f4ff',
    fontWeight: '800',
    fontSize: 16,
  },
  emptyText: {
    color: '#c9d5f6',
    fontSize: 13,
    lineHeight: 20,
  },
  modeRow: {
    borderWidth: 1,
    borderColor: '#304978',
    borderRadius: 12,
    backgroundColor: '#0a1732',
    paddingHorizontal: 10,
    paddingVertical: 9,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: 10,
  },
  modeTextWrap: {
    flex: 1,
    gap: 2,
  },
  modeTitle: {
    color: '#eef4ff',
    fontSize: 13,
    fontWeight: '800',
  },
  modeDescription: {
    color: '#a8bde6',
    fontSize: 11,
    lineHeight: 16,
  },
  modeToggle: {
    borderRadius: 999,
    borderWidth: 1,
    paddingHorizontal: 12,
    paddingVertical: 6,
    minWidth: 54,
    alignItems: 'center',
    justifyContent: 'center',
  },
  modeToggleOn: {
    borderColor: '#55d89d',
    backgroundColor: 'rgba(49, 186, 122, 0.2)',
  },
  modeToggleOff: {
    borderColor: '#406399',
    backgroundColor: 'rgba(53, 85, 142, 0.2)',
  },
  modeToggleText: {
    color: '#e7f0ff',
    fontSize: 11,
    fontWeight: '800',
  },
  practiceCard: {
    borderWidth: 1,
    borderColor: '#2a3c67',
    borderRadius: 14,
    backgroundColor: '#091228',
    padding: 12,
    gap: 10,
  },
  progressHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  progressTitle: {
    color: '#e8eeff',
    fontWeight: '800',
    fontSize: 15,
  },
  progressCounter: {
    color: '#99b6ff',
    fontWeight: '800',
    fontSize: 12,
  },
  progressTrack: {
    height: 8,
    borderRadius: 999,
    backgroundColor: '#1a2a4d',
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    borderRadius: 999,
    backgroundColor: '#3f86ff',
  },
  metricsRow: {
    flexDirection: 'row',
    gap: 6,
    flexWrap: 'wrap',
  },
  metricPill: {
    borderRadius: 999,
    paddingHorizontal: 8,
    paddingVertical: 3,
    fontSize: 11,
    fontWeight: '700',
    overflow: 'hidden',
  },
  metricGood: {
    color: '#9df0ca',
    backgroundColor: 'rgba(59, 201, 132, 0.18)',
  },
  metricBad: {
    color: '#ffb0b8',
    backgroundColor: 'rgba(210, 80, 100, 0.2)',
  },
  metricPending: {
    color: '#98c2ff',
    backgroundColor: 'rgba(74, 132, 226, 0.2)',
  },
  metricVisit: {
    color: '#b9ddff',
    backgroundColor: 'rgba(56, 108, 187, 0.26)',
  },
  metricTimer: {
    color: '#f0d79a',
    backgroundColor: 'rgba(240, 190, 93, 0.2)',
  },
  resumeRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: 10,
  },
  resumeActions: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  resumeText: {
    flex: 1,
    color: '#7fd7b3',
    fontSize: 12,
    lineHeight: 16,
  },
  resetProgressButton: {
    borderRadius: 8,
    backgroundColor: '#16274a',
    borderWidth: 1,
    borderColor: '#2d467a',
    paddingHorizontal: 10,
    paddingVertical: 7,
  },
  resetProgressText: {
    color: '#c0d6ff',
    fontWeight: '700',
    fontSize: 11,
  },
  optionsWrap: {
    gap: 8,
    marginTop: 4,
  },
  optionButton: {
    borderWidth: 1,
    borderColor: '#2a3f6d',
    borderRadius: 10,
    backgroundColor: '#0f1a35',
    paddingHorizontal: 10,
    paddingVertical: 10,
  },
  optionSelected: {
    borderColor: '#5f8fff',
    backgroundColor: '#12244b',
  },
  optionCorrect: {
    borderColor: '#2ccf8f',
    backgroundColor: 'rgba(33, 171, 114, 0.18)',
  },
  optionWrong: {
    borderColor: '#ff6f7d',
    backgroundColor: 'rgba(209, 64, 86, 0.2)',
  },
  optionText: {
    color: '#e0e9ff',
    fontSize: 13,
    lineHeight: 19,
  },
  controlsRow: {
    flexDirection: 'row',
    gap: 8,
    marginTop: 2,
  },
  finishSessionButton: {
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#3a5f9f',
    backgroundColor: 'rgba(38, 63, 109, 0.45)',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 10,
  },
  finishSessionText: {
    color: '#d5e4ff',
    fontWeight: '800',
    fontSize: 12,
  },
  controlButton: {
    flex: 1,
    borderRadius: 10,
    backgroundColor: '#1a2749',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 10,
  },
  controlButtonPrimary: {
    flex: 1,
    borderRadius: 10,
    backgroundColor: '#2f6bff',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 10,
  },
  controlDisabled: {
    opacity: 0.45,
  },
  feedbackCard: {
    borderWidth: 1,
    borderRadius: 12,
    padding: 10,
    gap: 8,
  },
  feedbackOk: {
    borderColor: '#2ccf8f',
    backgroundColor: 'rgba(26, 133, 91, 0.18)',
  },
  feedbackBad: {
    borderColor: '#ff6f7d',
    backgroundColor: 'rgba(148, 47, 62, 0.2)',
  },
  feedbackTitle: {
    color: '#f4f8ff',
    fontSize: 14,
    fontWeight: '800',
  },
  timerExpiredText: {
    color: '#ffb6bd',
    fontSize: 12,
    lineHeight: 18,
    fontWeight: '700',
  },
  resultScreenCard: {
    borderWidth: 1,
    borderColor: '#385b97',
    borderRadius: 14,
    backgroundColor: '#0a1737',
    padding: 12,
    gap: 8,
  },
  resultHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: 10,
  },
  resultTitle: {
    color: '#f3f6ff',
    fontSize: 14,
    fontWeight: '800',
  },
  resultScore: {
    color: '#d4e5ff',
    fontSize: 14,
    fontWeight: '900',
  },
  resultMeta: {
    color: '#c0d1f2',
    fontSize: 12,
  },
  resultRecommendationTitle: {
    color: '#f3f6ff',
    fontSize: 13,
    fontWeight: '700',
  },
  resultRecommendationText: {
    color: '#c7d6f4',
    fontSize: 12,
    lineHeight: 18,
  },
  resultActionsRow: {
    marginTop: 2,
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
  },
  resultActionButton: {
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#3f86ff',
    backgroundColor: 'rgba(59, 114, 216, 0.2)',
    paddingHorizontal: 10,
    paddingVertical: 8,
  },
  resultActionButtonSecondary: {
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#325081',
    backgroundColor: 'rgba(25, 45, 81, 0.45)',
    paddingHorizontal: 10,
    paddingVertical: 8,
  },
  resultActionText: {
    color: '#d9e7ff',
    fontSize: 11,
    fontWeight: '800',
  },
});
