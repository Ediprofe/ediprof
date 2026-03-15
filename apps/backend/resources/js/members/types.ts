export type NavItem = {
    label: string;
    href: string;
    active?: boolean;
};

export type SharedUser = {
    id: number;
    name: string;
    email: string;
    role: string;
    member_status: string;
    avatar_url?: string | null;
    display_name?: string | null;
};

export type SharedPageProps = {
    auth: {
        user: SharedUser | null;
    };
    flash: {
        success?: string | null;
        error?: string | null;
    };
};

export type QuickStat = {
    label: string;
    value: number | string;
};

export type DashboardSection = {
    title: string;
    description: string;
    href: string;
    emoji: string;
    count: number;
};

export type MemberAssignment = {
    id: string;
    title: string;
    mode: string;
    status: string;
    randomize_questions: boolean;
    max_attempts: number | null;
    time_limit_minutes: number | null;
    opens_at: string | null;
    closes_at: string | null;
    review_released_at: string | null;
    course: {
        id: number;
        name: string;
        slug: string;
        school_year: string | null;
    } | null;
    template: {
        id: string;
        title: string;
        content_type: string | null;
        route: string | null;
    } | null;
    stats: {
        selected_questions: number;
        effective_questions: number;
    };
    attempts: {
        used: number;
        limit: number | null;
        remaining: number | null;
    };
    feedback: {
        policy: string;
        policy_label: string;
        state: string;
        state_label: string;
        message: string;
        available: boolean;
        release_at: string | null;
    };
    availability: {
        can_view: boolean;
        can_start: boolean;
        state: string;
        code: string | null;
        message: string | null;
    };
    latest_attempt: {
        id: string;
        status: string;
        submitted_at: string | null;
        score_percent: number | null;
        score_scale: number | null;
        can_review: boolean;
        feedback_state: string;
        feedback_state_label: string;
    } | null;
    updated_at: string | null;
};

export type NextAction = {
    id: string;
    title: string;
    status: string;
    questions: number;
    href: string;
};

export type RenderContract = {
    strategy: 'html_first';
    html_primary_fields: string[];
    block_fallback_fields: string[];
    mobile_node_fields?: string[];
    asset_url_policy: string;
    notes: string[];
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

export type AttemptOption = {
    id: string;
    text: string;
    text_html?: string;
    text_assets?: string[];
    asset_refs?: AssetRef[];
    nodes_mobile?: Array<Record<string, any>>;
    is_correct?: boolean;
};

export type AttemptEvaluation = {
    attempt_id: string;
    question_id: string;
    selected_option_id: string | null;
    correct_option_id: string | null;
    is_correct: boolean | null;
    feedback_mdx?: string;
    feedback_html?: string;
    feedback_summary?: string | null;
    feedback_blocks?: Array<Record<string, any>>;
    feedback_nodes?: Array<Record<string, any>>;
    feedback_asset_refs?: AssetRef[];
    concepts_mdx?: string;
    concepts_html?: string;
    concepts_summary?: string | null;
    concepts_blocks?: Array<Record<string, any>>;
    concepts_nodes?: Array<Record<string, any>>;
    concepts_asset_refs?: AssetRef[];
};

export type AttemptQuestion = {
    id: string;
    order: number;
    stem_mdx?: string;
    stem_html?: string;
    stem_blocks?: Array<Record<string, any>>;
    stem_nodes?: Array<Record<string, any>>;
    stem_asset_refs?: AssetRef[];
    context_mdx?: string;
    context_html?: string;
    context_blocks?: Array<Record<string, any>>;
    context_nodes?: Array<Record<string, any>>;
    context_asset_refs?: AssetRef[];
    options?: AttemptOption[];
    correct_option_id?: string | null;
    feedback_mdx?: string;
    feedback_html?: string;
    feedback_summary?: string | null;
    feedback_blocks?: Array<Record<string, any>>;
    feedback_nodes?: Array<Record<string, any>>;
    feedback_asset_refs?: AssetRef[];
    concepts_mdx?: string;
    concepts_html?: string;
    concepts_summary?: string | null;
    concepts_blocks?: Array<Record<string, any>>;
    concepts_nodes?: Array<Record<string, any>>;
    concepts_asset_refs?: AssetRef[];
    selection_group_key?: string;
};

export type AttemptPayload = {
    id: string;
    content_external_id?: string;
    title: string;
    route?: string | null;
    area_slug?: string | null;
    unidad_slug?: string | null;
    content_type?: string | null;
    stats?: {
        total_questions?: number;
        total_assets?: number;
    };
    render_contract?: RenderContract;
    asset_refs?: AssetRef[];
    attempt: {
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
    questions: AttemptQuestion[];
    selected_by_question: Record<string, string>;
    evaluation_by_question: Record<string, AttemptEvaluation>;
    updated_at?: string | null;
};
