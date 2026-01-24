import MovieDropdown from "./components/MovieDropdown";
import TextPrompt from "./components/TextPrompt";
import RecommendButton from "./components/RecommendButton";
import Recommendations from "./components/Recommendations";

export default function Home() {
  return (
    <main className="max-w-3xl mx-auto py-10 px-4">
      <h1 className="text-3xl font-bold text-center mb-8">
        GenAI Movie Recommender
      </h1>

      <p className="text-center text-gray-600 mb-10">
        Select a movie and/or describe what you’re in the mood for.
      </p>

      <MovieDropdown />
      <TextPrompt />
      <RecommendButton />

      <Recommendations />
    </main>
  );
}
