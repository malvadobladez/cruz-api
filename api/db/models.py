from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Numeric,
    ForeignKey,
    DateTime,
    func,
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


# -------------------------
# Herb
# -------------------------
class Herb(Base):
    __tablename__ = "herbs"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    sku = Column(String, nullable=True)
    supplier = Column(String, nullable=True)

    cost_per_gram = Column(Numeric(10, 4), nullable=False)
    markup_percent = Column(Numeric(5, 2), nullable=False, server_default="0")

    is_active = Column(Boolean, default=True, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    blend_items = relationship("BlendItem", back_populates="herb")


# -------------------------
# Blend
# -------------------------
class Blend(Base):
    __tablename__ = "blends"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    items = relationship(
        "BlendItem",
        back_populates="blend",
        cascade="all, delete-orphan",
    )


# -------------------------
# BlendItem (join table)
# -------------------------
class BlendItem(Base):
    __tablename__ = "blend_items"

    id = Column(Integer, primary_key=True)

    blend_id = Column(
        Integer,
        ForeignKey("blends.id", ondelete="CASCADE"),
        nullable=False,
    )

    herb_id = Column(
        Integer,
        ForeignKey("herbs.id"),
        nullable=False,
    )

    grams = Column(Numeric(10, 2), nullable=False)

    blend = relationship("Blend", back_populates="items")
    herb = relationship("Herb", back_populates="blend_items")