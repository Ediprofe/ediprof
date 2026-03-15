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
  text_html?: string;
  text_assets?: string[];
  asset_refs?: AssetRef[];
  nodes_mobile?: WorkshopRichBlock[];
  is_correct?: boolean;
};

export type AssetRef = {
  asset_id: string;
  src: string;
  alt?: string | null;
  caption?: string | null;
  type: string;
  mime_type?: string | null;
  fallback_url?: string | null;
  width?: number | null;
  height?: number | null;
};

export type WorkshopRenderContract = {
  strategy: 'html_first';
  html_primary_fields: string[];
  block_fallback_fields: string[];
  mobile_node_fields?: string[];
  asset_url_policy: string;
  notes: string[];
};

export type WorkshopInlineSegment = {
  text: string;
  variant: 'plain' | 'bold' | 'highlight' | 'strike' | 'italic';
};

export type WorkshopRichBlock =
  | {
      type: 'paragraph';
      inlines: WorkshopInlineSegment[];
      layout?: string;
    }
  | {
      type: 'heading';
      depth: number;
      inlines: WorkshopInlineSegment[];
      layout?: string;
    }
  | {
      type: 'list';
      ordered: boolean;
      items: Array<{
        inlines: WorkshopInlineSegment[];
      }>;
      layout?: string;
    }
  | {
      type: 'equation';
      latex: string;
      layout?: string;
    }
  | {
      type: 'table';
      rows: string[][];
      layout?: string;
    }
  | {
      type: 'image';
      src: string;
      alt?: string;
      layout?: string;
    }
  | {
      type: 'html';
      html: string;
      layout?: string;
    };

export type WorkshopQuestion = {
  id: string;
  order: number;
  stem_mdx?: string;
  stem_html?: string;
  stem_assets: string[];
  stem_asset_refs?: AssetRef[];
  stem_blocks?: WorkshopRichBlock[];
  stem_nodes?: WorkshopRichBlock[];
  context_mdx?: string;
  context_html?: string;
  context_assets?: string[];
  context_asset_refs?: AssetRef[];
  context_blocks?: WorkshopRichBlock[];
  context_nodes?: WorkshopRichBlock[];
  options: WorkshopQuestionOption[];
  correct_option_id: string | null;
  feedback_mdx?: string;
  feedback_html?: string;
  feedback_assets: string[];
  feedback_asset_refs?: AssetRef[];
  feedback_blocks?: WorkshopRichBlock[];
  feedback_nodes?: WorkshopRichBlock[];
  concepts_mdx?: string;
  concepts_html?: string;
  concepts_assets?: string[];
  concepts_asset_refs?: AssetRef[];
  concepts_blocks?: WorkshopRichBlock[];
  concepts_nodes?: WorkshopRichBlock[];
  app_payload_version?: number | null;
};

export type WorkshopDetail = {
  id: string;
  title: string;
  route: string;
  access_tier: 'free' | 'premium';
  published: boolean;
  render_contract?: WorkshopRenderContract;
  questions: WorkshopQuestion[];
  assets: string[];
  asset_refs?: AssetRef[];
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
  feedback_html?: string;
  feedback_assets: string[];
  feedback_asset_refs?: AssetRef[];
  feedback_blocks?: WorkshopRichBlock[];
  feedback_nodes?: WorkshopRichBlock[];
  concepts_mdx?: string;
  concepts_html?: string;
  concepts_assets?: string[];
  concepts_asset_refs?: AssetRef[];
  concepts_blocks?: WorkshopRichBlock[];
  concepts_nodes?: WorkshopRichBlock[];
  next_question_id: string | null;
};

export type ApiError = {
  ok: false;
  error?: {
    code?: string;
    message?: string;
  };
};
