"use client";

import { useMovieStore } from "../store/movieStore";

export function useRecommend() {
  const selectedMovie = useMovieStore((s) => s.selectedMovie);
  const textPrompt = useMovieStore((s) => s.textPrompt);
  const setRecommendations = useMovieStore((s) => s.setRecommendations);

  const getRecommendations = async () => {
    try {
      const res = await fetch("/api/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          selected_movie_id: selectedMovie || null,
          user_prompt: textPrompt || "",
        }),
      });

      const data = await res.json();

      // backend not ready → return error object
      if (!Array.isArray(data)) {
        setRecommendations([]); // avoid crashes
        return;
      }

      setRecommendations(data);
    } catch (err) {
      setRecommendations([]); // safe fallback
    }
  };

  return { getRecommendations };
}
