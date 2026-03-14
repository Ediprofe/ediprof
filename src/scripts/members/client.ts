type MemberUser = {
  id: number;
  name: string;
  email: string;
  role?: string;
  member_status?: string;
  auth_provider?: string | null;
  google_avatar_url?: string | null;
};

type LoginResponse = {
  ok: boolean;
  data?: {
    token: string;
    user: MemberUser;
  };
  error?: {
    code?: string;
    message?: string;
  };
};

const TOKEN_KEY = 'ediprofe_member_token';
const USER_KEY = 'ediprofe_member_user';
const API_BASE_KEY = 'ediprofe_member_api_base';

function getDefaultApiBase(): string {
  if (typeof window === 'undefined') {
    return 'http://127.0.0.1:8080/api/v1';
  }

  const host = window.location.hostname;
  if (host === 'localhost' || host === '127.0.0.1') {
    return 'http://127.0.0.1:8080/api/v1';
  }

  const normalizedHost = host.replace(/^www\./, '');
  if (normalizedHost.startsWith('api.')) {
    return `https://${normalizedHost}/api/v1`;
  }

  return `https://api.${normalizedHost}/api/v1`;
}

export function getApiBase(): string {
  if (typeof window === 'undefined') {
    return getDefaultApiBase();
  }

  const stored = window.localStorage.getItem(API_BASE_KEY);
  if (!stored || stored.trim() === '') {
    return getDefaultApiBase();
  }

  return stored.trim().replace(/\/+$/, '');
}

export function setApiBase(url: string): void {
  if (typeof window === 'undefined') {
    return;
  }

  const normalized = url.trim().replace(/\/+$/, '');
  window.localStorage.setItem(API_BASE_KEY, normalized);
}

export function getSessionToken(): string | null {
  if (typeof window === 'undefined') {
    return null;
  }

  return window.localStorage.getItem(TOKEN_KEY);
}

export function getSessionUser(): MemberUser | null {
  if (typeof window === 'undefined') {
    return null;
  }

  const raw = window.localStorage.getItem(USER_KEY);
  if (!raw) {
    return null;
  }

  try {
    return JSON.parse(raw) as MemberUser;
  } catch {
    return null;
  }
}

export function saveSession(token: string, user: MemberUser): void {
  if (typeof window === 'undefined') {
    return;
  }

  window.localStorage.setItem(TOKEN_KEY, token);
  window.localStorage.setItem(USER_KEY, JSON.stringify(user));
}

export function clearSession(): void {
  if (typeof window === 'undefined') {
    return;
  }

  window.localStorage.removeItem(TOKEN_KEY);
  window.localStorage.removeItem(USER_KEY);
}

async function parseApiResponse<T>(response: Response): Promise<T> {
  const payload = await response.json().catch(() => null);
  if (!response.ok) {
    const message = payload?.error?.message || payload?.message || 'Request failed.';
    throw new Error(message);
  }

  return payload as T;
}

export async function apiLogin(input: {
  email: string;
  password: string;
  device_name?: string;
}): Promise<LoginResponse> {
  const response = await fetch(`${getApiBase()}/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(input),
  });

  return parseApiResponse<LoginResponse>(response);
}

export async function apiGoogleLogin(input: {
  credential: string;
  device_name?: string;
}): Promise<LoginResponse> {
  const response = await fetch(`${getApiBase()}/auth/google/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(input),
  });

  return parseApiResponse<LoginResponse>(response);
}

export async function apiMe(): Promise<any> {
  const token = getSessionToken();
  if (!token) {
    throw new Error('No active session.');
  }

  const response = await fetch(`${getApiBase()}/auth/me`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return parseApiResponse<any>(response);
}

export async function apiLogout(): Promise<void> {
  const token = getSessionToken();
  if (!token) {
    clearSession();
    return;
  }

  await fetch(`${getApiBase()}/auth/logout`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  clearSession();
}

function getAuthorizedHeaders(extra: Record<string, string> = {}): Record<string, string> {
  const token = getSessionToken();
  if (!token) {
    throw new Error('No active session.');
  }

  return {
    Authorization: `Bearer ${token}`,
    ...extra,
  };
}

export async function apiWorkshops(options: { published?: boolean } = {}): Promise<any> {
  return apiCatalog('workshops', options);
}

export async function apiSimulacros(options: { published?: boolean } = {}): Promise<any> {
  return apiCatalog('simulacros', options);
}

export async function apiMyCourses(): Promise<any> {
  const response = await fetch(`${getApiBase()}/me/courses`, {
    headers: getAuthorizedHeaders(),
  });

  return parseApiResponse<any>(response);
}

export async function apiMyLibrary(options: {
  published?: boolean;
  contentType?: 'taller' | 'simulacro';
  search?: string;
} = {}): Promise<any> {
  const params = new URLSearchParams();
  params.set('per_page', '60');
  if (typeof options.published === 'boolean') {
    params.set('published', String(options.published));
  }
  if (options.contentType) {
    params.set('content_type', options.contentType);
  }
  if (options.search) {
    params.set('search', options.search);
  }

  const response = await fetch(`${getApiBase()}/me/library?${params.toString()}`, {
    headers: getAuthorizedHeaders(),
  });

  return parseApiResponse<any>(response);
}

export async function apiMyAssignments(options: { mode?: 'study' | 'simulacro' | 'evaluation' } = {}): Promise<any> {
  const params = new URLSearchParams();
  if (options.mode) {
    params.set('mode', options.mode);
  }

  const response = await fetch(`${getApiBase()}/me/assignments${params.toString() ? `?${params.toString()}` : ''}`, {
    headers: getAuthorizedHeaders(),
  });

  return parseApiResponse<any>(response);
}

export async function apiMyAssignment(assignmentId: string): Promise<any> {
  const response = await fetch(`${getApiBase()}/me/assignments/${encodeURIComponent(assignmentId)}`, {
    headers: getAuthorizedHeaders(),
  });

  return parseApiResponse<any>(response);
}

function encodeCompositeId(value: string): string {
  return value
    .split('/')
    .map(encodeURIComponent)
    .join('/');
}

async function apiCatalog(resource: 'workshops' | 'simulacros', options: { published?: boolean } = {}): Promise<any> {
  const token = getSessionToken();
  const params = new URLSearchParams();
  params.set('per_page', '60');
  if (typeof options.published === 'boolean') {
    params.set('published', String(options.published));
  }

  const response = await fetch(`${getApiBase()}/${resource}?${params.toString()}`, {
    headers: token
      ? {
          Authorization: `Bearer ${token}`,
        }
      : undefined,
  });
  return parseApiResponse<any>(response);
}

type DetailOptions = {
  publishedOnly?: boolean;
  includeAnswers?: boolean;
  format?: 'app' | 'default';
};

type StartAttemptOptions = {
  mode?: 'study' | 'simulacro' | 'evaluation' | 'exam';
  reset?: boolean;
};

async function apiContentDetail(
  resource: 'workshops' | 'simulacros',
  contentId: string,
  options: DetailOptions = {}
): Promise<any> {
  const token = getSessionToken();
  const encodedId = encodeCompositeId(contentId);
  const params = new URLSearchParams();
  params.set('published_only', String(options.publishedOnly ?? false));
  params.set('include_answers', String(options.includeAnswers ?? false));
  params.set('format', options.format ?? 'app');

  const response = await fetch(
    `${getApiBase()}/${resource}/${encodedId}?${params.toString()}`,
    {
      headers: token
        ? {
            Authorization: `Bearer ${token}`,
          }
        : undefined,
    }
  );

  return parseApiResponse<any>(response);
}

export async function apiWorkshopDetail(workshopId: string, options: DetailOptions = {}): Promise<any> {
  return apiContentDetail('workshops', workshopId, options);
}

export async function apiSimulacroDetail(simulacroId: string, options: DetailOptions = {}): Promise<any> {
  return apiContentDetail('simulacros', simulacroId, options);
}

async function apiStartAttempt(
  resource: 'workshops' | 'simulacros',
  contentId: string,
  options: StartAttemptOptions = {}
): Promise<any> {
  const encodedId = encodeCompositeId(contentId);
  const response = await fetch(`${getApiBase()}/${resource}/${encodedId}/attempts`, {
    method: 'POST',
    headers: getAuthorizedHeaders({
      'Content-Type': 'application/json',
    }),
    body: JSON.stringify(options),
  });

  return parseApiResponse<any>(response);
}

export async function apiStartWorkshopAttempt(
  workshopId: string,
  options: StartAttemptOptions = {}
): Promise<any> {
  return apiStartAttempt('workshops', workshopId, options);
}

export async function apiStartSimulacroAttempt(
  simulacroId: string,
  options: StartAttemptOptions = {}
): Promise<any> {
  return apiStartAttempt('simulacros', simulacroId, options);
}

export async function apiStartAssignmentAttempt(
  assignmentId: string,
  options: StartAttemptOptions = {}
): Promise<any> {
  const response = await fetch(`${getApiBase()}/assignments/${encodeURIComponent(assignmentId)}/attempts`, {
    method: 'POST',
    headers: getAuthorizedHeaders({
      'Content-Type': 'application/json',
    }),
    body: JSON.stringify(options),
  });

  return parseApiResponse<any>(response);
}

export async function apiAssessmentAttempt(attemptId: string): Promise<any> {
  const response = await fetch(`${getApiBase()}/assessment-attempts/${encodeURIComponent(attemptId)}`, {
    headers: getAuthorizedHeaders(),
  });

  return parseApiResponse<any>(response);
}

export async function apiAnswerAssessmentAttempt(
  attemptId: string,
  questionId: string,
  optionId: string
): Promise<any> {
  const response = await fetch(
    `${getApiBase()}/assessment-attempts/${encodeURIComponent(attemptId)}/questions/${encodeURIComponent(questionId)}`,
    {
      method: 'PATCH',
      headers: getAuthorizedHeaders({
        'Content-Type': 'application/json',
      }),
      body: JSON.stringify({
        option_id: optionId,
      }),
    }
  );

  return parseApiResponse<any>(response);
}

export async function apiSubmitAssessmentAttempt(attemptId: string): Promise<any> {
  const response = await fetch(`${getApiBase()}/assessment-attempts/${encodeURIComponent(attemptId)}/submit`, {
    method: 'POST',
    headers: getAuthorizedHeaders(),
  });

  return parseApiResponse<any>(response);
}

async function apiEvaluateContent(
  resource: 'workshops' | 'simulacros',
  contentId: string,
  questionId: string,
  optionId: string
): Promise<any> {
  const token = getSessionToken();
  const encodedId = encodeCompositeId(contentId);
  const encodedQuestion = encodeURIComponent(questionId);

  const response = await fetch(
    `${getApiBase()}/${resource}/${encodedId}/questions/${encodedQuestion}/evaluate?published_only=false&format=app`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(token
          ? {
              Authorization: `Bearer ${token}`,
            }
          : {}),
      },
      body: JSON.stringify({
        option_id: optionId,
      }),
    }
  );

  return parseApiResponse<any>(response);
}

export async function apiEvaluate(workshopId: string, questionId: string, optionId: string): Promise<any> {
  return apiEvaluateContent('workshops', workshopId, questionId, optionId);
}

export async function apiEvaluateSimulacro(
  simulacroId: string,
  questionId: string,
  optionId: string
): Promise<any> {
  return apiEvaluateContent('simulacros', simulacroId, questionId, optionId);
}

export async function apiAdminCourses(): Promise<any> {
  const response = await fetch(`${getApiBase()}/admin/courses`, {
    headers: getAuthorizedHeaders(),
  });

  return parseApiResponse<any>(response);
}

export async function apiAdminCreateCourse(input: {
  name: string;
  slug?: string;
  school_year?: string;
  is_active?: boolean;
  notes?: string;
}): Promise<any> {
  const response = await fetch(`${getApiBase()}/admin/courses`, {
    method: 'POST',
    headers: getAuthorizedHeaders({
      'Content-Type': 'application/json',
    }),
    body: JSON.stringify(input),
  });

  return parseApiResponse<any>(response);
}

export async function apiAdminUpdateCourse(
  courseId: number,
  input: {
    name: string;
    slug?: string;
    school_year?: string;
    is_active?: boolean;
    notes?: string;
  }
): Promise<any> {
  const response = await fetch(`${getApiBase()}/admin/courses/${courseId}`, {
    method: 'PATCH',
    headers: getAuthorizedHeaders({
      'Content-Type': 'application/json',
    }),
    body: JSON.stringify(input),
  });

  return parseApiResponse<any>(response);
}

export async function apiAdminCourseContents(courseId: number): Promise<any> {
  const response = await fetch(`${getApiBase()}/admin/courses/${courseId}/contents`, {
    headers: getAuthorizedHeaders(),
  });

  return parseApiResponse<any>(response);
}

export async function apiAdminAddCourseContent(courseId: number, contentId: string): Promise<any> {
  const response = await fetch(`${getApiBase()}/admin/courses/${courseId}/contents`, {
    method: 'POST',
    headers: getAuthorizedHeaders({
      'Content-Type': 'application/json',
    }),
    body: JSON.stringify({
      content_id: contentId,
    }),
  });

  return parseApiResponse<any>(response);
}

export async function apiAdminRemoveCourseContent(courseId: number, contentId: string): Promise<any> {
  const response = await fetch(
    `${getApiBase()}/admin/courses/${courseId}/contents/${contentId
      .split('/')
      .map(encodeURIComponent)
      .join('/')}`,
    {
      method: 'DELETE',
      headers: getAuthorizedHeaders(),
    }
  );

  return parseApiResponse<any>(response);
}

export async function apiAdminImportCourseEnrollments(courseId: number, file: File): Promise<any> {
  const formData = new FormData();
  formData.append('csv', file);

  const response = await fetch(`${getApiBase()}/admin/courses/${courseId}/enrollments/import`, {
    method: 'POST',
    headers: getAuthorizedHeaders(),
    body: formData,
  });

  return parseApiResponse<any>(response);
}

export async function apiAdminPanelHandoff(redirectTo?: string): Promise<any> {
  const response = await fetch(`${getApiBase()}/admin/panel-handoff`, {
    method: 'POST',
    headers: getAuthorizedHeaders({
      'Content-Type': 'application/json',
    }),
    body: JSON.stringify({
      redirect_to: redirectTo,
    }),
  });

  return parseApiResponse<any>(response);
}
