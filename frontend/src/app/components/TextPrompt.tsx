"use client";

import { useMovieStore } from "../store/movieStore";

export default function TextPrompt() {
  const textPrompt = useMovieStore((s) => s.textPrompt);
  const setTextPrompt = useMovieStore((s) => s.setTextPrompt);

  return (
    <div className="mt-6">
      <label className="block mb-2 font-medium">
        Describe what you're looking for (optional)
      </label>

      <textarea
        value={textPrompt}
        onChange={(e) => setTextPrompt(e.target.value)}
        className="w-full border rounded-md p-2 bg-white h-28 resize-none"
        placeholder="e.g. funny sci-fi with emotional depth"
      />
    </div>
  );
}
