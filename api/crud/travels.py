from sqlalchemy.orm import Session
from api.database.models.travels import Travels
from api.database.schemas.travels import TravelCreate, TravelUpdate

# Add travel
def create_travel(db: Session, travel: TravelCreate):
    new_travel = Travels(**travel.dict())
    db.add(new_travel)
    db.commit()
    db.refresh(new_travel)
    return new_travel

# Get all travels
def get_all_travels(db: Session):
    return db.query(Travels).all()

# Get travel by id
def get_travel_by_id(db: Session, travel_id: int):
    return db.query(Travels).filter(Travels.id == travel_id).first()

# Update travel
def update_travel(db: Session, travel_id: int, travel_data: TravelUpdate):
    travel = db.query(Travels).filter(Travels.id == travel_id).first()
    if travel:
        for key, value in travel_data.dict().items():
            setattr(travel, key, value)
        db.commit()
        db.refresh(travel)
    return travel

# Delete travel
def delete_travel(db: Session, travel_id: int):
    travel = db.query(Travels).filter(Travels.id == travel_id).first()
    if travel:
        db.delete(travel)
        db.commit()
    return travel
