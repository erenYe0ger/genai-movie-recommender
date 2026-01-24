import { NextResponse } from "next/server";

export async function POST(req: Request) {
  const body = await req.json();

  const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL;
  const url = `${backendUrl ?? "http://localhost:8000"}/recommend`;

  try {
    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const data = await res.json();
    return NextResponse.json(data);
  } catch (err) {
    return NextResponse.json(
      { error: "Failed to fetch recommendation" },
      { status: 500 }
    );
  }
}
