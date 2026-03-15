<?php

namespace App\Http\Resources;

use App\Services\Content\RichContentPayloadNormalizer;
use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

/**
 * @mixin \App\Models\Workshop
 */
class WorkshopResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        $includeAnswers = $request->boolean('include_answers', true);
        $appFormat = strtolower((string) $request->query('format', '')) === 'app';
        $questions = is_array($this->questions) ? $this->questions : [];
        $normalizer = app(RichContentPayloadNormalizer::class);

        $questions = array_map(function (array $question) use ($includeAnswers, $appFormat, $normalizer): array {
            unset($question['meta']);

            if (! $includeAnswers) {
                $question['correct_option_id'] = null;
                $question['feedback_mdx'] = '';
                $question['feedback_html'] = '';
                $question['feedback_summary'] = null;
                $question['feedback_assets'] = [];
                $question['feedback_blocks'] = [];
                $question['concepts_mdx'] = '';
                $question['concepts_html'] = '';
                $question['concepts_summary'] = null;
                $question['concepts_assets'] = [];
                $question['concepts_blocks'] = [];

                $question['options'] = array_map(static function (array $option): array {
                    unset($option['is_correct']);

                    return $option;
                }, is_array($question['options'] ?? null) ? $question['options'] : []);

            }

            if ($appFormat) {
                unset(
                    $question['stem_mdx'],
                    $question['context_mdx'],
                    $question['feedback_mdx'],
                    $question['concepts_mdx']
                );
            }

            return $normalizer->normalizeQuestion($question);
        }, $questions);

        return [
            'id' => $this->external_id,
            'content_external_id' => $this->content_external_id,
            'content_type' => $this->content_type,
            'title' => $this->title,
            'route' => $this->route,
            'area_slug' => $this->area_slug,
            'unidad_slug' => $this->unidad_slug,
            'access_tier' => $this->access_tier,
            'published' => $this->is_published,
            'stats' => [
                'total_questions' => $this->total_questions,
                'total_assets' => $this->total_assets,
            ],
            'render_contract' => $normalizer->renderContract(),
            'assets' => $normalizer->normalizeAssetList(is_array($this->assets) ? $this->assets : []),
            'asset_refs' => $normalizer->normalizeAssetRefs(
                is_array($this->asset_refs ?? null)
                    ? $this->asset_refs
                    : $normalizer->buildAssetRefsFromStrings(is_array($this->assets) ? $this->assets : [])
            ),
            'questions' => $questions,
            'updated_at' => $this->updated_at?->toIso8601String(),
        ];
    }
}
