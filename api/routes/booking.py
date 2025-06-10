from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.booking import BookingCreate, BookingUpdate, Booking
from api.crud.booking import create_booking, get_booking, get_bookings_by_user, get_all_bookings, update_booking, delete_booking

router = APIRouter()

# ✅ Get all bookings route
@router.get("/all", response_model=list[Booking])
def get_all_bookings_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = get_all_bookings(db=db, skip=skip, limit=limit)
    return bookings

@router.post("/create", response_model=Booking)
def create_booking_route(booking: BookingCreate, db: Session = Depends(get_db)):
    return create_booking(db=db, booking=booking)

@router.get("/{booking_id}", response_model=Booking)
def get_booking_route(booking_id: int, db: Session = Depends(get_db)):
    db_booking = get_booking(db=db, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@router.get("/user/{user_id}", response_model=list[Booking])
def get_bookings_by_user_route(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    bookings = get_bookings_by_user(db=db, user_id=user_id, skip=skip, limit=limit)
    return bookings


@router.put("/{booking_id}", response_model=Booking)
def update_booking_route(booking_id: int, booking: BookingUpdate, db: Session = Depends(get_db)):
    db_booking = update_booking(db=db, booking_id=booking_id, booking=booking)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@router.delete("/{booking_id}", response_model=Booking)
def delete_booking_route(booking_id: int, db: Session = Depends(get_db)):
    db_booking = delete_booking(db=db, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking
