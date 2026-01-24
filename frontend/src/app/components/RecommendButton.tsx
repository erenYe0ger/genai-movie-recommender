"use client";

import { useMovieStore } from "../store/movieStore";
import { useRecommend } from "../hooks/useRecommend";

export default function RecommendButton() {
  const selectedMovie = useMovieStore((s) => s.selectedMovie);
  const textPrompt = useMovieStore((s) => s.textPrompt);

  const { getRecommendations } = useRecommend();

  const canRecommend = selectedMovie !== "" || textPrompt.trim() !== "";

  return (
    <div className="mt-8">
      <button
        onClick={async () => {
          if (canRecommend) {
            await getRecommendations();
          }
        }}
        disabled={!canRecommend}
        className={`w-full py-3 rounded-md font-medium transition ${
          canRecommend
            ? "bg-blue-600 text-white hover:bg-blue-700"
            : "bg-gray-300 text-gray-500 cursor-not-allowed"
        }`}
      >
        Recommend Movies
      </button>
    </div>
  );
}
