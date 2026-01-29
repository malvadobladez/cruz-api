from sqlalchemy import Column, Integer, String, Boolean, Numeric, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Herb(Base):
    __tablename__ = "herbs"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    sku = Column(String, nullable=True)
    supplier = Column(String, nullable=True)

    cost_per_gram = Column(Numeric(10, 4), nullable=False)
    markup_percent = Column(Numeric(5, 2), nullable=False, server_default="0")

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    @property
    def sell_price_per_gram(self):
        return float(self.cost_per_gram) * (1 + float(self.markup_percent) / 100)
    