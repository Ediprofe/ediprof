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
  useWindowDimensions,
  View,
} from 'react-native';
import { Image } from 'expo-image';
import { StatusBar } from 'expo-status-bar';
import { QuestionStem } from './src/components/QuestionStem';
import { WorkshopCard } from './src/components/WorkshopCard';
import {
  ApiRequestError,
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
import type { WorkshopDetail, WorkshopSummary } from './src/types/api';

const DEFAULT_BASE_URL = 'http://127.0.0.1:8080/api/v1';

export default function App() {
  const { width } = useWindowDimensions();
  const isCompact = width < 1080;

  const [baseUrl, setBaseUrl] = useState(DEFAULT_BASE_URL);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useState<string | null>(null);
  const [workshops, setWorkshops] = useState<WorkshopSummary[]>([]);
  const [selectedWorkshopId, setSelectedWorkshopId] = useState<string | null>(null);
  const [selectedWorkshop, setSelectedWorkshop] = useState<WorkshopDetail | null>(null);
  const [loading, setLoading] = useState(false);
  const [loadingWorkshop, setLoadingWorkshop] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [detailAccessError, setDetailAccessError] = useState<
    'auth_required' | 'premium_access_required' | null
  >(null);

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
    setLoading(true);
    setErrorMessage(null);

    try {
      await saveBaseUrl(baseUrl);
      const response = await listWorkshops(baseUrl, token ?? undefined);
      setWorkshops(response.data);

      if (response.data.length > 0) {
        const firstId = response.data[0]?.id ?? null;
        setSelectedWorkshopId((current) => current ?? firstId);
      } else {
        setSelectedWorkshopId(null);
        setSelectedWorkshop(null);
      }

      setDetailAccessError(null);
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : 'No fue posible cargar catálogo.');
    } finally {
      setLoading(false);
    }
  }, [baseUrl, token]);

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
      } catch (error) {
        if (
          error instanceof ApiRequestError &&
          (error.code === 'auth_required' || error.code === 'premium_access_required')
        ) {
          setDetailAccessError(error.code);
          setSelectedWorkshop(null);
          setErrorMessage(error.message);

          return;
        }

        setErrorMessage(error instanceof Error ? error.message : 'No fue posible cargar el taller.');
        setSelectedWorkshop(null);
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
    setLoading(true);
    setErrorMessage(null);

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
      setLoading(false);
    }
  }, [baseUrl, email, password, refreshCatalog]);

  const handleLogout = useCallback(async () => {
    setLoading(true);
    setErrorMessage(null);

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
      setLoading(false);
    }
  }, [baseUrl, refreshCatalog, token]);

  const selectedTitle = useMemo(() => {
    if (!selectedWorkshop) {
      return 'Selecciona un taller';
    }

    return `${selectedWorkshop.title} (${selectedWorkshop.stats.total_questions} preguntas)`;
  }, [selectedWorkshop]);

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar style="light" />
      <View style={styles.root}>
        <Text style={styles.h1}>Ediprofe Mobile MVP</Text>
        <Text style={styles.subtitle}>
          Para dispositivo físico usa la IP LAN, por ejemplo: http://192.168.x.x:8080/api/v1
        </Text>

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
              placeholderTextColor="#7f90b8"
              value={email}
              onChangeText={setEmail}
              autoCapitalize="none"
              autoCorrect={false}
            />
            <TextInput
              style={[styles.input, styles.grow]}
              placeholder="password"
              placeholderTextColor="#7f90b8"
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

        <View style={[styles.columns, isCompact ? styles.columnsCompact : null]}>
          <View style={[styles.leftCol, isCompact ? styles.leftColCompact : null]}>
            <Text style={styles.sectionTitle}>Catálogo</Text>
            {loading ? <ActivityIndicator color="#9ac0ff" /> : null}
            <FlatList
              data={workshops}
              keyExtractor={(item) => item.id}
              renderItem={({ item }) => (
                <WorkshopCard
                  item={item}
                  isSelected={item.id === selectedWorkshopId}
                  onPress={handlePressWorkshop}
                />
              )}
              removeClippedSubviews
              initialNumToRender={8}
              maxToRenderPerBatch={10}
              windowSize={7}
              contentContainerStyle={styles.catalogContent}
            />
          </View>

          <View style={[styles.rightCol, isCompact ? styles.rightColCompact : null]}>
            <Text style={styles.sectionTitle}>{selectedTitle}</Text>
            {loadingWorkshop ? <ActivityIndicator color="#9ac0ff" /> : null}

            <ScrollView style={styles.detailScroll} contentContainerStyle={styles.detailContent}>
              {!selectedWorkshop && detailAccessError === 'auth_required' ? (
                <View style={styles.emptyState}>
                  <Text style={styles.emptyTitle}>Taller premium bloqueado</Text>
                  <Text style={styles.emptyText}>
                    Inicia sesión con una cuenta que tenga acceso premium para ver preguntas y
                    retroalimentación.
                  </Text>
                </View>
              ) : null}

              {!selectedWorkshop && detailAccessError === 'premium_access_required' ? (
                <View style={styles.emptyState}>
                  <Text style={styles.emptyTitle}>Sin acceso premium</Text>
                  <Text style={styles.emptyText}>
                    Tu cuenta está autenticada, pero no tiene una suscripción o un permiso activo
                    para este taller.
                  </Text>
                </View>
              ) : null}

              {selectedWorkshop?.questions.map((question) => (
                <View key={question.id} style={styles.questionCard}>
                  <Text style={styles.questionTitle}>Pregunta {question.order}</Text>
                  <QuestionStem stem={question.stem_mdx} />

                  {question.stem_assets.map((asset, idx) => (
                    <Image
                      key={`${question.id}-asset-${idx}`}
                      source={asset}
                      style={styles.questionImage}
                      contentFit="contain"
                      transition={120}
                    />
                  ))}

                  {question.options.map((option) => (
                    <View key={option.id} style={styles.optionRow}>
                      <Text style={styles.optionText}>
                        {option.id}. {option.text}
                      </Text>
                    </View>
                  ))}
                </View>
              ))}
            </ScrollView>
          </View>
        </View>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#0b1020',
  },
  root: {
    flex: 1,
    padding: 12,
    gap: 10,
  },
  h1: {
    color: '#eef3ff',
    fontSize: 24,
    fontWeight: '800',
  },
  subtitle: {
    color: '#95a6cf',
    fontSize: 12,
  },
  panel: {
    borderWidth: 1,
    borderColor: '#24345d',
    borderRadius: 12,
    backgroundColor: '#0f1a35',
    padding: 10,
    gap: 8,
  },
  label: {
    color: '#dce6ff',
    fontSize: 12,
    fontWeight: '600',
  },
  input: {
    borderWidth: 1,
    borderColor: '#2a3d6a',
    borderRadius: 8,
    paddingHorizontal: 10,
    paddingVertical: 8,
    color: '#f5f8ff',
    backgroundColor: '#0b142d',
    minWidth: 120,
  },
  grow: {
    flex: 1,
  },
  row: {
    flexDirection: 'row',
    gap: 8,
    alignItems: 'center',
  },
  buttonPrimary: {
    borderRadius: 8,
    backgroundColor: '#2f6bff',
    paddingHorizontal: 12,
    paddingVertical: 9,
  },
  buttonGhost: {
    borderRadius: 8,
    backgroundColor: '#1a2749',
    paddingHorizontal: 12,
    paddingVertical: 9,
  },
  buttonText: {
    color: '#edf2ff',
    fontWeight: '700',
    fontSize: 12,
  },
  meta: {
    color: '#99a8cd',
    fontSize: 12,
  },
  error: {
    color: '#ff98a1',
    fontSize: 12,
  },
  columns: {
    flex: 1,
    flexDirection: 'row',
    gap: 10,
  },
  columnsCompact: {
    flexDirection: 'column',
  },
  leftCol: {
    flex: 1,
    borderWidth: 1,
    borderColor: '#23335b',
    borderRadius: 12,
    backgroundColor: '#0d1731',
    padding: 8,
  },
  rightCol: {
    flex: 1.2,
    borderWidth: 1,
    borderColor: '#23335b',
    borderRadius: 12,
    backgroundColor: '#0d1731',
    padding: 8,
  },
  leftColCompact: {
    flex: 0,
    minHeight: 260,
  },
  rightColCompact: {
    flex: 1,
    minHeight: 420,
  },
  sectionTitle: {
    color: '#e8eeff',
    fontWeight: '700',
    marginBottom: 8,
  },
  catalogContent: {
    paddingBottom: 12,
  },
  detailScroll: {
    flex: 1,
  },
  detailContent: {
    paddingBottom: 20,
    gap: 10,
  },
  questionCard: {
    borderWidth: 1,
    borderColor: '#253761',
    borderRadius: 10,
    backgroundColor: '#0a142b',
    padding: 10,
    gap: 8,
  },
  questionTitle: {
    color: '#f0f4ff',
    fontWeight: '700',
    fontSize: 14,
  },
  questionImage: {
    width: '100%',
    height: 220,
    borderRadius: 8,
    backgroundColor: '#f4f7ff',
    borderWidth: 1,
    borderColor: '#2a3f6d',
  },
  optionRow: {
    borderWidth: 1,
    borderColor: '#2a3f6d',
    borderRadius: 8,
    backgroundColor: '#0f1a35',
    paddingHorizontal: 9,
    paddingVertical: 6,
  },
  optionText: {
    color: '#dee6ff',
    fontSize: 12,
  },
  emptyState: {
    borderWidth: 1,
    borderColor: '#334a7f',
    borderRadius: 10,
    backgroundColor: '#0b142b',
    padding: 14,
    gap: 8,
  },
  emptyTitle: {
    color: '#f0f4ff',
    fontWeight: '700',
    fontSize: 16,
  },
  emptyText: {
    color: '#c9d5f6',
    fontSize: 13,
    lineHeight: 19,
  },
});
