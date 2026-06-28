from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Jesse Richard — Portfolio IA",
    description="CV numérique interactif de Jesse Richard, Développeur IA",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


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
