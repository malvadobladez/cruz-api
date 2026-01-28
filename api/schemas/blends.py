from pydantic import BaseModel
from decimal import Decimal
from typing import Optional


class BlendCreate(BaseModel):
    name: str
    notes: Optional[str] = None


class BlendItemCreate(BaseModel):
    herb_id: int
    grams: Decimal


class BlendCostResponse(BaseModel):
    blend: str
    total_grams: Decimal
    total_cost: Decimal
    cost_per_gram: Decimal