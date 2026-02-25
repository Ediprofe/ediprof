import AsyncStorage from '@react-native-async-storage/async-storage';

const SESSION_KEY = 'ediprofe_mobile_session_v1';
const BASE_URL_KEY = 'ediprofe_mobile_base_url_v1';

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
