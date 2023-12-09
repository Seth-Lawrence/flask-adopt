from app import db
from models import Pet

db.drop_all()
db.create_all()

sample_pet = Pet(name="Pal", species="dog", age=4)

db.session.add(sample_pet)
db.session.commit()
