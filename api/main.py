from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    herbs = [
        {"name": "Hibiscus", "cost_per_gram": 0.1899},
        {"name": "Dandelion Root", "cost_per_gram": 0.0420},
    ]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "herbs": herbs,
        },
    )


@app.get("/api/herbs")
def list_herbs():
    return [
        {"name": "Hibiscus", "cost_per_gram": 0.1899},
        {"name": "Dandelion Root", "cost_per_gram": 0.0420},
    ]
