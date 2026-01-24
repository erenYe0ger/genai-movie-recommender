"use client";

import { useEffect } from "react";
import { useMovieStore } from "../store/movieStore";

export default function MovieDropdown() {
  const movies = useMovieStore((s) => s.movies);
  const selectedMovie = useMovieStore((s) => s.selectedMovie);
  const setSelectedMovie = useMovieStore((s) => s.setSelectedMovie);

  // fetch movie list once (via /api/movies)
  useEffect(() => {
    fetch("/api/movies")
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) {
          useMovieStore.setState({ movies: data });
        }
      });
  }, []);

  return (
    <div className="mt-6">
      <label className="block mb-2 font-medium">Select a movie (optional)</label>

      <select
        value={selectedMovie}
        onChange={(e) => setSelectedMovie(e.target.value)}
        className="w-full border rounded-md p-2 bg-white"
      >
        <option value="">-- choose a movie --</option>

        {movies.map((m: any) => (
          <option key={m.id} value={m.id}>
            {m.title}
          </option>
        ))}
      </select>
    </div>
  );
}
