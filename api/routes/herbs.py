from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.db.session import get_db
from api.db.models import Herb

router = APIRouter(prefix="/api/herbs", tags=["herbs"])


@router.get("/")
def list_herbs(db: Session = Depends(get_db)):
    return (
        db.query(Herb)
        .filter(Herb.is_active == True)
        .order_by(Herb.name)
        .all()
    )