import { NextResponse } from "next/server";

export async function GET() {
  const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL;

  // fallback for dev
  const url = `${backendUrl ?? "http://localhost:8000"}/movies`;

  try {
    const res = await fetch(url, { cache: "no-store" });
    const data = await res.json();
    return NextResponse.json(data);
  } catch (err) {
    return NextResponse.json({ error: "Failed to fetch movies" }, { status: 500 });
  }
}
