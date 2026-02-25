import AsyncStorage from '@react-native-async-storage/async-storage';
import type { WorkshopEvaluationResult } from '../types/api';

const SESSION_KEY = 'ediprofe_mobile_session_v1';
const BASE_URL_KEY = 'ediprofe_mobile_base_url_v1';
const WORKSHOP_PROGRESS_PREFIX = 'ediprofe_mobile_workshop_progress_v1:';

export type WorkshopPracticeState = {
  questionIndex: number;
  selectedOptionByQuestion: Record<string, string>;
  evaluationByQuestion: Record<string, WorkshopEvaluationResult>;
  updatedAt: string;
};

export async function saveSessionToken(token: string): Promise<void> {
  await AsyncStorage.setItem(SESSION_KEY, token);
}

export async function loadSessionToken(): Promise<string | null> {
  return AsyncStorage.getItem(SESSION_KEY);
}

export async function clearSessionToken(): Promise<void> {
  await AsyncStorage.removeItem(SESSION_KEY);
}

export async function saveBaseUrl(url: string): Promise<void> {
  await AsyncStorage.setItem(BASE_URL_KEY, url);
}

export async function loadBaseUrl(): Promise<string | null> {
  return AsyncStorage.getItem(BASE_URL_KEY);
}

function workshopProgressKey(workshopId: string): string {
  return `${WORKSHOP_PROGRESS_PREFIX}${workshopId}`;
}

export async function saveWorkshopPracticeState(
  workshopId: string,
  state: Omit<WorkshopPracticeState, 'updatedAt'>,
): Promise<void> {
  const payload: WorkshopPracticeState = {
    questionIndex: state.questionIndex,
    selectedOptionByQuestion: state.selectedOptionByQuestion,
    evaluationByQuestion: state.evaluationByQuestion,
    updatedAt: new Date().toISOString(),
  };

  await AsyncStorage.setItem(workshopProgressKey(workshopId), JSON.stringify(payload));
}

export async function loadWorkshopPracticeState(workshopId: string): Promise<WorkshopPracticeState | null> {
  const raw = await AsyncStorage.getItem(workshopProgressKey(workshopId));
  if (!raw) {
    return null;
  }

  try {
    const parsed = JSON.parse(raw) as Partial<WorkshopPracticeState>;
    if (
      typeof parsed !== 'object' ||
      parsed === null ||
      typeof parsed.questionIndex !== 'number' ||
      !Number.isFinite(parsed.questionIndex) ||
      typeof parsed.selectedOptionByQuestion !== 'object' ||
      parsed.selectedOptionByQuestion === null ||
      typeof parsed.evaluationByQuestion !== 'object' ||
      parsed.evaluationByQuestion === null
    ) {
      return null;
    }

    return {
      questionIndex: parsed.questionIndex,
      selectedOptionByQuestion: parsed.selectedOptionByQuestion as Record<string, string>,
      evaluationByQuestion: parsed.evaluationByQuestion as Record<string, WorkshopEvaluationResult>,
      updatedAt: typeof parsed.updatedAt === 'string' ? parsed.updatedAt : new Date().toISOString(),
    };
  } catch {
    return null;
  }
}

export async function clearWorkshopPracticeState(workshopId: string): Promise<void> {
  await AsyncStorage.removeItem(workshopProgressKey(workshopId));
}
