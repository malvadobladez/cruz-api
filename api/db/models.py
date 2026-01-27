from sqlalchemy import (
    Column, Integer, String, Numeric, Boolean,
    ForeignKey, Text
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

Base = declarative_base()


class Herb(Base):
    __tablename__ = "herbs"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    cost_per_gram = Column(Numeric(10, 4), nullable=False)
    supplier = Column(String)
    sku = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Blend(Base):
    __tablename__ = "blends"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    notes = Column(Text)


class BlendItem(Base):
    __tablename__ = "blend_items"

    blend_id = Column(Integer, ForeignKey("blends.id"), primary_key=True)
    herb_id = Column(Integer, ForeignKey("herbs.id"), primary_key=True)
    grams = Column(Numeric(10, 2), nullable=False)