"use client";

import { useMovieStore } from "../store/movieStore";

export default function Recommendations() {
  const recommendations = useMovieStore((s) => s.recommendations);

  if (!Array.isArray(recommendations) || recommendations.length === 0) {
    return null;
  }

  return (
    <div className="mt-10">
      <h2 className="text-xl font-semibold mb-4">Recommended Movies</h2>

      <div className="grid grid-cols-2 gap-6">
        {recommendations.map((movie: any) => (
          <div key={movie.movie_id} className="bg-white shadow rounded-md p-3">
            <img
              src={movie.poster_url}
              alt={movie.title}
              className="w-full h-auto rounded"
            />
            <h3 className="mt-3 font-semibold">{movie.title}</h3>
            <p className="text-sm text-gray-600 mt-1">{movie.why}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
