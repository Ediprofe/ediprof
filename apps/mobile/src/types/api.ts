export type AuthSession = {
  token: string;
  tokenType: 'Bearer';
  expiresAt: string;
  user: {
    id: number;
    name: string;
    email: string;
  };
};

export type WorkshopSummary = {
  id: string;
  content_external_id: string | null;
  title: string;
  route: string;
  area_slug: string | null;
  unidad_slug: string | null;
  access_tier: 'free' | 'premium';
  published: boolean;
  can_access: boolean;
  stats: {
    total_questions: number;
    total_assets: number;
  };
  asset_preview: string[];
  updated_at: string | null;
};

export type WorkshopListResponse = {
  ok: boolean;
  data: WorkshopSummary[];
  meta: {
    current_page: number;
    per_page: number;
    total: number;
    last_page: number;
    from: number | null;
    to: number | null;
  };
};

export type WorkshopQuestionOption = {
  id: string;
  text: string;
  is_correct?: boolean;
};

export type WorkshopInlineSegment = {
  text: string;
  variant: 'plain' | 'bold' | 'highlight' | 'strike';
};

export type WorkshopRichBlock =
  | {
      type: 'paragraph';
      inlines: WorkshopInlineSegment[];
    }
  | {
      type: 'equation';
      latex: string;
    }
  | {
      type: 'table';
      rows: string[][];
    }
  | {
      type: 'image';
      src: string;
      alt?: string;
    };

export type WorkshopQuestion = {
  id: string;
  order: number;
  stem_mdx?: string;
  stem_assets: string[];
  stem_blocks?: WorkshopRichBlock[];
  options: WorkshopQuestionOption[];
  correct_option_id: string | null;
  feedback_mdx?: string;
  feedback_assets: string[];
  feedback_blocks?: WorkshopRichBlock[];
  app_payload_version?: number | null;
};

export type WorkshopDetail = {
  id: string;
  title: string;
  route: string;
  access_tier: 'free' | 'premium';
  published: boolean;
  questions: WorkshopQuestion[];
  assets: string[];
  stats: {
    total_questions: number;
    total_assets: number;
  };
};

export type WorkshopEvaluationResult = {
  workshop_id: string;
  question_id: string;
  selected_option_id: string;
  correct_option_id: string | null;
  is_correct: boolean;
  feedback_mdx?: string;
  feedback_assets: string[];
  feedback_blocks?: WorkshopRichBlock[];
  next_question_id: string | null;
};

export type ApiError = {
  ok: false;
  error?: {
    code?: string;
    message?: string;
  };
};
