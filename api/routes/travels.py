from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.travels import TravelCreate, TravelUpdate, TravelResponse
from api.crud.travels import create_travel, get_all_travels, get_travel_by_id, update_travel, delete_travel
from typing import List

router = APIRouter()


@router.post("/add", response_model=TravelResponse)
def add_travel(travel: TravelCreate, db: Session = Depends(get_db)):
    return create_travel(db, travel)

@router.get("/all", response_model=List[TravelResponse])
def get_travels(db: Session = Depends(get_db)):
    return get_all_travels(db)

@router.get("/get/{travel_id}", response_model=TravelResponse)
def get_travel(travel_id: int, db: Session = Depends(get_db)):
    travel = get_travel_by_id(db, travel_id)
    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found")
    return travel

@router.put("/update/{travel_id}", response_model=TravelResponse)
def update_travel_route(travel_id: int, travel_data: TravelUpdate, db: Session = Depends(get_db)):
    travel = update_travel(db, travel_id, travel_data)
    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found")
    return travel


@router.delete("/delete/{travel_id}")
def delete_travel_route(travel_id: int, db: Session = Depends(get_db)):
    travel = delete_travel(db, travel_id)
    if not travel:
        raise HTTPException(status_code=404, detail="Travel not found")
    return {"detail": "Travel deleted successfully"}

