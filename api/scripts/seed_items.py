import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.db.models import Herb

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

LB_TO_G = 453.592

HERBS = [
    ("Anise Star Whole", 9.99, 114),
    ("Arnica Flower Whole", 11.99, 114),
    ("Ashwagandha Root C/S", 21.99, LB_TO_G),
    ("Balm Lemon Herb C/S", 28.99, LB_TO_G),
    ("Black Seed Whole", 8.99, 114),
    ("Black Tea C/S", 26.99, LB_TO_G),
    ("Burdock Root C/S", 12.99, 114),
    ("Butterfly Pea Flower", 21.99, 114),
    ("Calendula Petals (Marigold)", 14.99, LB_TO_G),
    ("Cat's Claw Bark C/S", 17.99, 114),
    ("Catnip Herb C/S", 14.99, 114),
    ("Chai Tea Masala", 29.99, LB_TO_G),
    ("Cinnamon Chips Ceylon", 29.99, LB_TO_G),
    ("Cinnamon Tea", 19.99, LB_TO_G),
    ("Cleavers Herb C/S", 13.99, 114),
    ("Cloves Whole", 10.99, 114),
    ("Comfrey Root C/S", 12.99, 114),
    ("Corriander Seed Whole", 5.99, 114),
    ("Dandelion Root C/S", 28.99, LB_TO_G),
    ("Devil's Claw Root C/S", 13.99, 114),
    ("Elderflower Whole", 18.99, 114),
    ("Fenugreek Leaves C/S", 10.99, 114),
    ("Ginger Root C/S", 13.99, LB_TO_G),
    ("Ginseng Siberian C/S", 23.99, LB_TO_G),
    ("Green Tea China C/S (Lucky Dragon Hyson)", 23.99, LB_TO_G),
    ("Hops Flower", 16.99, 114),
    ("Lavender Flower Super Blue", 29.99, LB_TO_G),
    ("Linden Leaves & Flower C/S", 39.99, LB_TO_G),
    ("Lungwort", 18.99, 114),
    ("Marshmallow Root C/S", 29.99, LB_TO_G),
    ("Mugwort Herb C/S", 11.99, 114),
    ("Mullein Leaves C/S", 27.99, LB_TO_G),
    ("Oatstraw Herb C/S", 27.99, LB_TO_G),
    ("Oolong Standard Tea", 23.99, LB_TO_G),
    ("Orange Peel C/S", 6.99, 114),
    ("Passiflora Herb C/S", 18.99, LB_TO_G),
    ("Peppermint Leaves C/S", 22.99, LB_TO_G),
    ("Pomegranate Peel C/S", 6.99, 114),
    ("Red Clover Blossoms Whole", 13.99, 114),
    ("Red Rose Petals", 24.99, 114),
    ("Rosehips Seedless C/S", 12.99, 114),
    ("Rosemary Leaves C/S", 5.99, 114),
    ("Skullcap Herb C/S", 53.99, LB_TO_G),
    ("Valerian Root C/S", 15.99, 114),
    ("Vervain Herb C/S", 12.99, 114),
    ("Vetiver Root C/S", 12.99, 114),
    ("White Willow Bark C/S", 10.99, 114),
    ("Yarrow Flower C/S", 19.99, LB_TO_G),
]

def seed():
    session = Session()

    for name, cost, grams in HERBS:
        existing = session.query(Herb).filter_by(name=name).first()
        if existing:
            continue

        herb = Herb(
            name=name,
            cost_per_gram=round(cost / grams, 4),
            is_active=True,
        )
        session.add(herb)

    session.commit()
    session.close()
    print("Herb seeding complete")

if __name__ == "__main__":
    seed()