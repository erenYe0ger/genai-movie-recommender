"use client";

import { useEffect } from "react";
import { useMovieStore } from "../store/movieStore";

export function useMovies() {
  const setMovies = useMovieStore((s: any) => s.setMovies);

  useEffect(() => {
    const fetchMovies = async () => {
      const res = await fetch("/api/movies");
      const data = await res.json();

      if (data && Array.isArray(data)) {
        setMovies(data);
      }
    };

    fetchMovies();
  }, [setMovies]);
}
