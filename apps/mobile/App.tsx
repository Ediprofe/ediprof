import { useCallback, useEffect, useMemo, useState } from 'react';
import {
  ActivityIndicator,
  FlatList,
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
  clearSessionToken,
  loadBaseUrl,
  loadSessionToken,
  saveBaseUrl,
  saveSessionToken,
} from './src/lib/storage';
import type { WorkshopDetail, WorkshopEvaluationResult, WorkshopSummary } from './src/types/api';

const DEFAULT_BASE_URL = 'http://127.0.0.1:8080/api/v1';

type DetailAccessError = 'auth_required' | 'premium_access_required' | null;

export default function App() {
  const [baseUrl, setBaseUrl] = useState(DEFAULT_BASE_URL);
  const [email, setEmail] = useState('demo@ediprofe.com');
  const [password, setPassword] = useState('Demo12345!');
  const [token, setToken] = useState<string | null>(null);

  const [workshops, setWorkshops] = useState<WorkshopSummary[]>([]);
  const [selectedWorkshopId, setSelectedWorkshopId] = useState<string | null>(null);
  const [selectedWorkshop, setSelectedWorkshop] = useState<WorkshopDetail | null>(null);

  const [questionIndex, setQuestionIndex] = useState(0);
  const [selectedOptionByQuestion, setSelectedOptionByQuestion] = useState<Record<string, string>>({});
  const [evaluationByQuestion, setEvaluationByQuestion] = useState<Record<string, WorkshopEvaluationResult>>({});

  const [loadingCatalog, setLoadingCatalog] = useState(false);
  const [loadingWorkshop, setLoadingWorkshop] = useState(false);
  const [submittingAnswer, setSubmittingAnswer] = useState(false);

  const [detailAccessError, setDetailAccessError] = useState<DetailAccessError>(null);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  useEffect(() => {
    let mounted = true;

    const bootstrap = async () => {
      const [savedUrl, savedToken] = await Promise.all([loadBaseUrl(), loadSessionToken()]);

      if (!mounted) {
        return;
      }

      if (savedUrl) {
        setBaseUrl(savedUrl);
      }

      if (!savedToken) {
        return;
      }

      try {
        await getCurrentUser(savedUrl ?? DEFAULT_BASE_URL, savedToken);
        setToken(savedToken);
      } catch {
        await clearSessionToken();
      }
    };

    void bootstrap();

    return () => {
      mounted = false;
    };
  }, []);

  const refreshCatalog = useCallback(async () => {
    setLoadingCatalog(true);
    setErrorMessage(null);

    try {
      await saveBaseUrl(baseUrl);
      const response = await listWorkshops(baseUrl, token ?? undefined);
      setWorkshops(response.data);

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

      try {
        const detail = await getWorkshop(baseUrl, workshopId, token ?? undefined);
        setSelectedWorkshop(detail);
        setQuestionIndex(0);
        setSelectedOptionByQuestion({});
        setEvaluationByQuestion({});
      } catch (error) {
        setSelectedWorkshop(null);
        setQuestionIndex(0);
        setSelectedOptionByQuestion({});
        setEvaluationByQuestion({});

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

  const currentQuestionId = currentQuestion?.id ?? null;
  const selectedOptionId = currentQuestionId ? selectedOptionByQuestion[currentQuestionId] : undefined;
  const evaluation = currentQuestionId ? evaluationByQuestion[currentQuestionId] : undefined;

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
    if (!selectedWorkshop || !currentQuestion || !selectedOptionId) {
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
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : 'No fue posible evaluar la respuesta.');
    } finally {
      setSubmittingAnswer(false);
    }
  }, [baseUrl, currentQuestion, selectedOptionId, selectedWorkshop, token]);

  const goPrev = useCallback(() => {
    setQuestionIndex((prev) => Math.max(0, prev - 1));
  }, []);

  const goNext = useCallback(() => {
    if (!selectedWorkshop) {
      return;
    }

    setQuestionIndex((prev) => Math.min(selectedWorkshop.questions.length - 1, prev + 1));
  }, [selectedWorkshop]);

  const title = selectedWorkshop
    ? `${selectedWorkshop.title} (${selectedWorkshop.stats.total_questions} preguntas)`
    : 'Selecciona un taller';

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar style="light" />
      <ScrollView style={styles.root} contentContainerStyle={styles.rootContent}>
        <Text style={styles.h1}>Ediprofe Mobile</Text>
        <Text style={styles.subtitle}>Práctica guiada tipo Saber con retroalimentación inmediata.</Text>

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

          {selectedWorkshop && currentQuestion ? (
            <View style={styles.practiceCard}>
              <View style={styles.progressHeader}>
                <Text style={styles.progressTitle}>
                  Pregunta {questionIndex + 1} de {totalQuestions}
                </Text>
                <Text style={styles.progressCounter}>{Math.round(progressValue * 100)}%</Text>
              </View>

              <View style={styles.progressTrack}>
                <View style={[styles.progressFill, { width: `${progressValue * 100}%` }]} />
              </View>

              <QuestionStem
                stem={currentQuestion.stem_mdx}
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
                  style={[styles.controlButton, questionIndex === 0 ? styles.controlDisabled : null]}
                  onPress={goPrev}
                  disabled={questionIndex === 0}
                >
                  <Text style={styles.buttonText}>Anterior</Text>
                </Pressable>

                <Pressable
                  style={[
                    styles.controlButtonPrimary,
                    !selectedOptionId || submittingAnswer ? styles.controlDisabled : null,
                  ]}
                  onPress={handleEvaluate}
                  disabled={!selectedOptionId || submittingAnswer}
                >
                  <Text style={styles.buttonText}>{submittingAnswer ? 'Comprobando...' : 'Comprobar'}</Text>
                </Pressable>

                <Pressable
                  style={[
                    styles.controlButton,
                    questionIndex >= totalQuestions - 1 ? styles.controlDisabled : null,
                  ]}
                  onPress={goNext}
                  disabled={questionIndex >= totalQuestions - 1}
                >
                  <Text style={styles.buttonText}>Siguiente</Text>
                </Pressable>
              </View>

              {evaluation ? (
                <View style={[styles.feedbackCard, evaluation.is_correct ? styles.feedbackOk : styles.feedbackBad]}>
                  <Text style={styles.feedbackTitle}>
                    {evaluation.is_correct ? 'Respuesta correcta' : 'Respuesta incorrecta'}
                  </Text>
                  <QuestionStem
                    stem={evaluation.feedback_mdx}
                    stemAssets={evaluation.feedback_assets}
                    blocks={evaluation.feedback_blocks}
                  />
                </View>
              ) : null}
            </View>
          ) : null}
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
    padding: 14,
    gap: 12,
    paddingBottom: 30,
  },
  h1: {
    color: '#f1f5ff',
    fontSize: 30,
    fontWeight: '900',
  },
  subtitle: {
    color: '#95a6cf',
    fontSize: 13,
  },
  panel: {
    borderWidth: 1,
    borderColor: '#22345d',
    borderRadius: 16,
    padding: 12,
    gap: 10,
    backgroundColor: '#0c1631',
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
  error: {
    color: '#ff9aa4',
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
});
