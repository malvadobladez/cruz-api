from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from api.db.session import get_db
from api.db.models import Herb
from api.routes import herbs, blends

app = FastAPI()

templates = Jinja2Templates(directory="api/templates")


@app.get("/health")
def health():
    return {"status": "ok"}


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


app.include_router(herbs.router)
app.include_router(blends.router)