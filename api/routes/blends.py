from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from decimal import Decimal

from api.db.session import get_db
from api.db.models import Blend, BlendItem, Herb
from api.schemas.blends import (
    BlendCreate,
    BlendItemCreate,
    BlendCostResponse
)

router = APIRouter(prefix="/blends", tags=["blends"])


# -------------------------------------------------
# Create a blend
# -------------------------------------------------
@router.post("", response_model=dict)
def create_blend(payload: BlendCreate, db: Session = Depends(get_db)):
    existing = db.query(Blend).filter_by(name=payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Blend already exists")

    blend = Blend(name=payload.name, notes=payload.notes)
    db.add(blend)
    db.commit()
    db.refresh(blend)

    return {"id": blend.id, "name": blend.name}


# -------------------------------------------------
# Add or overwrite blend item
# -------------------------------------------------
@router.post("/{blend_id}/items", response_model=dict)
def add_blend_item(
    blend_id: int,
    payload: BlendItemCreate,
    db: Session = Depends(get_db),
):
    blend = db.query(Blend).get(blend_id)
    if not blend:
        raise HTTPException(status_code=404, detail="Blend not found")

    herb = db.query(Herb).get(payload.herb_id)
    if not herb:
        raise HTTPException(status_code=404, detail="Herb not found")

    item = (
        db.query(BlendItem)
        .filter_by(blend_id=blend_id, herb_id=payload.herb_id)
        .first()
    )

    if item:
        item.grams = payload.grams  # OVERWRITE (authoritative)
    else:
        item = BlendItem(
            blend_id=blend_id,
            herb_id=payload.herb_id,
            grams=payload.grams
        )
        db.add(item)

    db.commit()
    return {"status": "ok"}


# -------------------------------------------------
# Get blend cost
# -------------------------------------------------
@router.get("/{blend_id}/cost", response_model=BlendCostResponse)
def get_blend_cost(blend_id: int, db: Session = Depends(get_db)):
    blend = db.query(Blend).get(blend_id)
    if not blend:
        raise HTTPException(status_code=404, detail="Blend not found")

    totals = (
        db.query(
            func.sum(BlendItem.grams).label("total_grams"),
            func.sum(BlendItem.grams * Herb.cost_per_gram).label("total_cost"),
        )
        .join(Herb, Herb.id == BlendItem.herb_id)
        .filter(BlendItem.blend_id == blend_id)
        .one()
    )

    total_grams = totals.total_grams or Decimal("0")
    total_cost = totals.total_cost or Decimal("0")

    cost_per_gram = (
        (total_cost / total_grams)
        if total_grams > 0
        else Decimal("0")
    )

    return BlendCostResponse(
        blend=blend.name,
        total_grams=total_grams,
        total_cost=total_cost,
        cost_per_gram=cost_per_gram,
    )