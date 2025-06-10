from sqlalchemy.orm import Session
from api.database.models.booking import Booking
from api.database.schemas.booking import BookingCreate, BookingUpdate

def create_booking(db: Session, booking: BookingCreate):
    # Corrected variable names to match schema
    db_booking = Booking(
        user_id_fk=booking.user_id_fk,
        from_location=booking.from_location,  # Corrected from 'form' to 'from_location'
        to_location=booking.to_location,  # Corrected from 'to' to 'to_location'
        seats=booking.seats,
        price_per_seat=booking.price_per_seat,
        total_price=booking.total_price
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

# ✅ Get all bookings function (removed duplicate)
def get_all_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Booking).offset(skip).limit(limit).all()

def get_booking(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.id == booking_id).first()

def get_bookings_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Booking).filter(Booking.user_id_fk == user_id).offset(skip).limit(limit).all()

def update_booking(db: Session, booking_id: int, booking: BookingUpdate):
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if db_booking:
        if booking.from_location:
            db_booking.from_location = booking.from_location
        if booking.to_location:
            db_booking.to_location = booking.to_location
        if booking.seats:
            db_booking.seats = booking.seats
        if booking.price_per_seat:
            db_booking.price_per_seat = booking.price_per_seat
        if booking.total_price:
            db_booking.total_price = booking.total_price
        db.commit()
        db.refresh(db_booking)
    return db_booking

def delete_booking(db: Session, booking_id: int):
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if db_booking:
        db.delete(db_booking)
        db.commit()
    return db_booking
