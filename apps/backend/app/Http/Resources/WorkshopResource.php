<?php

namespace App\Http\Resources;

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
        $questions = is_array($this->questions) ? $this->questions : [];

        $questions = array_map(static function (array $question) use ($includeAnswers): array {
            unset($question['meta']);

            if (! $includeAnswers) {
                $question['correct_option_id'] = null;
                $question['feedback_mdx'] = '';
                $question['feedback_assets'] = [];
                $question['feedback_blocks'] = [];

                $question['options'] = array_map(static function (array $option): array {
                    unset($option['is_correct']);

                    return $option;
                }, is_array($question['options'] ?? null) ? $question['options'] : []);

            }

            return $question;
        }, $questions);

        return [
            'id' => $this->external_id,
            'content_external_id' => $this->content_external_id,
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
            'assets' => $this->assets ?? [],
            'questions' => $questions,
            'updated_at' => $this->updated_at?->toIso8601String(),
        ];
    }
}
