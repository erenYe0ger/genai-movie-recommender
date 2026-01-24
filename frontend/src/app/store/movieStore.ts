import { create } from "zustand";

type Movie = {
  id: string;
  title: string;
};

type MovieStore = {
  // inputs
  selectedMovie: string;
  textPrompt: string;

  // movie list from backend
  movies: Movie[];
  setMovies: (list: Movie[]) => void;

  // recommendations
  recommendations: any[];
  setRecommendations: (data: any[]) => void;

  // setters
  setSelectedMovie: (id: string) => void;
  setTextPrompt: (text: string) => void;
};

export const useMovieStore = create<MovieStore>((set) => ({
  selectedMovie: "",
  textPrompt: "",

  movies: [],
  setMovies: (list) => set({ movies: list }),

  recommendations: [],
  setRecommendations: (data) => set({ recommendations: data }),

  setSelectedMovie: (id) => set({ selectedMovie: id }),
  setTextPrompt: (text) => set({ textPrompt: text }),
}));
