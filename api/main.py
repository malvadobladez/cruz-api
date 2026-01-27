from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from api.db.session import get_db
from api.db.models import Herb
from api.routes import herbs, blends  # blends already created

app = FastAPI()

templates = Jinja2Templates(directory="templates")


# -------------------------
# Health
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------
# Web UI (server-rendered)
# -------------------------
@app.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    herbs = (
        db.query(Herb)
        .filter(Herb.is_active == True)
        .order_by(Herb.name)
        .all()
    )

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "herbs": herbs,
        },
    )


# -------------------------
# Routers
# -------------------------
app.include_router(herbs.router)
app.include_router(blends.router)