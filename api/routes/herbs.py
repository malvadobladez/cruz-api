from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from decimal import Decimal

from api.db.session import get_db
from api.db.models import Herb

router = APIRouter(prefix="/herbs", tags=["herbs"])


@router.patch("/{herb_id}/markup")
def update_markup(
    herb_id: int,
    markup_percent: Decimal,
    db: Session = Depends(get_db),
):
    herb = db.query(Herb).filter(Herb.id == herb_id).first()
    if not herb:
        raise HTTPException(status_code=404, detail="Herb not found")

    herb.markup_percent = markup_percent
    db.commit()
    db.refresh(herb)

    return {
        "id": herb.id,
        "markup_percent": herb.markup_percent,
    }