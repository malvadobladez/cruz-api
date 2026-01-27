from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from models import Herb  # adjust import if needed

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

HERBS = [
    # name, cost_per_gram
    ("Hibiscus", 18.99 / 100),
    # add the rest here
]

def seed():
    session = Session()

    for name, cost in HERBS:
        exists = session.query(Herb).filter_by(name=name).first()
        if exists:
            continue

        herb = Herb(
            name=name,
            cost_per_gram=round(cost, 4),
            active=True,
        )
        session.add(herb)

    session.commit()
    session.close()
    print("Herb seeding complete")

if __name__ == "__main__":
    seed()