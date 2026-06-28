import asyncio
from datetime import datetime, timezone

import httpx
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

N8N_WEBHOOK = (
    "https://mon-n8n-mfof.onrender.com/webhook/6f3437d8-b95f-4894-80d3-074d47ec375c"
)

app = FastAPI(
    title="Jesse Richard — Portfolio IA",
    description="CV numérique interactif de Jesse Richard, Développeur IA",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


async def _notify(ip: str, ua: str, path: str) -> None:
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            await client.post(N8N_WEBHOOK, json={
                "ip": ip,
                "user_agent": ua,
                "path": path,
                "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
            })
    except Exception:
        pass


@app.middleware("http")
async def track_visitors(request: Request, call_next):
    response = await call_next(request)
    if request.method == "GET" and request.url.path not in ("/health", "/static"):
        asyncio.create_task(_notify(
            request.client.host if request.client else "unknown",
            request.headers.get("user-agent", "unknown"),
            str(request.url.path),
        ))
    return response


@app.get("/", response_class=HTMLResponse)
async def portfolio(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/cv", response_class=HTMLResponse)
async def cv_print(request: Request):
    return templates.TemplateResponse(request, "cv-print.html")


@app.get("/health")
@app.head("/health")
async def health():
    return {"status": "ok"}
