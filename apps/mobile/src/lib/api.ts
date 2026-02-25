import type {
  ApiError,
  AuthSession,
  WorkshopDetail,
  WorkshopListResponse,
} from '../types/api';

export class ApiRequestError extends Error {
  readonly status: number;

  readonly code?: string;

  constructor(message: string, status: number, code?: string) {
    super(message);
    this.name = 'ApiRequestError';
    this.status = status;
    this.code = code;
  }
}

type LoginPayload = {
  email: string;
  password: string;
  deviceName: string;
};

function normalizeBaseUrl(url: string): string {
  return url.replace(/\/$/, '');
}

async function parseJson<T>(response: Response): Promise<T> {
  return (await response.json()) as T;
}

function toErrorMessage(payload: unknown, fallback: string): string {
  if (!payload || typeof payload !== 'object') {
    return fallback;
  }

  const maybeError = (payload as ApiError).error;
  if (maybeError?.message) {
    return maybeError.message;
  }

  return fallback;
}

function toApiRequestError(
  response: Response,
  payload: ApiError | unknown,
  fallback: string,
): ApiRequestError {
  const message = toErrorMessage(payload, fallback);
  const code =
    payload && typeof payload === 'object' && 'error' in payload
      ? (payload as ApiError).error?.code
      : undefined;

  return new ApiRequestError(message, response.status, code);
}

export async function login(baseUrl: string, payload: LoginPayload): Promise<AuthSession> {
  const url = `${normalizeBaseUrl(baseUrl)}/auth/login`;
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      email: payload.email,
      password: payload.password,
      device_name: payload.deviceName,
    }),
  });

  const data = await parseJson<{ ok: boolean; data?: any } & ApiError>(response);

  if (!response.ok || !data.ok || !data.data?.token) {
    throw toApiRequestError(response, data, 'No fue posible iniciar sesión.');
  }

  return {
    token: data.data.token as string,
    tokenType: 'Bearer',
    expiresAt: data.data.expires_at as string,
    user: {
      id: data.data.user.id as number,
      name: data.data.user.name as string,
      email: data.data.user.email as string,
    },
  };
}

export async function listWorkshops(baseUrl: string, token?: string): Promise<WorkshopListResponse> {
  // Dev-first for current content state: workshops are mostly drafts.
  const url = `${normalizeBaseUrl(baseUrl)}/workshops?published=false&per_page=30`;
  const response = await fetch(url, {
    headers: token
      ? {
          Authorization: `Bearer ${token}`,
        }
      : undefined,
  });

  const data = await parseJson<WorkshopListResponse & ApiError>(response);

  if (!response.ok || !data.ok) {
    throw toApiRequestError(response, data, 'No fue posible cargar talleres.');
  }

  return data;
}

export async function getWorkshop(
  baseUrl: string,
  workshopId: string,
  token?: string,
): Promise<WorkshopDetail> {
  const encodedId = workshopId
    .split('/')
    .map(encodeURIComponent)
    .join('/');

  const url = `${normalizeBaseUrl(baseUrl)}/workshops/${encodedId}?published_only=false&include_answers=false`;
  const response = await fetch(url, {
    headers: token
      ? {
          Authorization: `Bearer ${token}`,
        }
      : undefined,
  });

  const data = await parseJson<{ ok: boolean; data?: WorkshopDetail } & ApiError>(response);

  if (!response.ok || !data.ok || !data.data) {
    throw toApiRequestError(response, data, 'No fue posible cargar el taller.');
  }

  return data.data;
}

export async function getCurrentUser(baseUrl: string, token: string): Promise<void> {
  const url = `${normalizeBaseUrl(baseUrl)}/auth/me`;
  const response = await fetch(url, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    const data = await parseJson<ApiError>(response).catch(() => null);
    throw toApiRequestError(response, data, 'Tu sesión no es válida.');
  }
}

export async function logout(baseUrl: string, token: string): Promise<void> {
  const url = `${normalizeBaseUrl(baseUrl)}/auth/logout`;
  await fetch(url, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
}
