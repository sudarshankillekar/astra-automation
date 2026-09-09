import { env } from 'cloudflare:workers';
import { validateLead } from '@/lib/lead';
export async function POST(request: Request) {
  const origin = request.headers.get('origin');
  if (origin && origin !== new URL(request.url).origin)
    return Response.json(
      { error: 'Please submit from the Astra website.' },
      { status: 403 },
    );
  if (!request.headers.get('content-type')?.includes('application/json'))
    return Response.json(
      { error: 'JSON content is required.' },
      { status: 415 },
    );
  if (Number(request.headers.get('content-length') || 0) > 16000)
    return Response.json(
      { error: 'Your message is too long.' },
      { status: 413 },
    );
  try {
    const raw = await request.text();
    if (raw.length > 16000)
      return Response.json(
        { error: 'Your message is too long.' },
        { status: 413 },
      );
    let data: Record<string, unknown>;
    try {
      data = JSON.parse(raw);
    } catch {
      return Response.json(
        { error: 'Please check your enquiry and try again.' },
        { status: 400 },
      );
    }
    if (!data || typeof data !== 'object' || Array.isArray(data))
      return Response.json({ error: 'Invalid enquiry.' }, { status: 400 });
    if (data.website)
      return Response.json(
        { error: 'Please try again without autofill.' },
        { status: 400 },
      );
    const error = validateLead(data);
    if (error) return Response.json({ error }, { status: 400 });
    const id = crypto.randomUUID();
    await env.DB.prepare(
      'INSERT INTO enquiries (id,name,business,phone,email,industry,need,message,created_at) VALUES (?,?,?,?,?,?,?,?,?)',
    )
      .bind(
        id,
        ...[
          'name',
          'business',
          'phone',
          'email',
          'industry',
          'need',
          'message',
        ].map((k) => (data[k] as string).trim()),
        new Date().toISOString(),
      )
      .run();
    return Response.json(
      { reference: id.slice(0, 8).toUpperCase() },
      { status: 201, headers: { 'Cache-Control': 'no-store' } },
    );
  } catch {
    return Response.json(
      {
        error:
          'We could not save your enquiry right now. Please try again shortly.',
      },
      { status: 503 },
    );
  }
}
