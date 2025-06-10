from pydantic import BaseModel
from typing import Optional

class BookingBase(BaseModel):
    from_location: str
    to_location: str
    seats: int
    price_per_seat: float
    total_price: float

class BookingCreate(BookingBase):
    user_id_fk: int

class BookingUpdate(BookingBase):
    from_location: Optional[str] = None
    to_location: Optional[str] = None
    seats: Optional[int] = None
    price_per_seat: Optional[float] = None
    total_price: Optional[float] = None

class Booking(BookingBase):
    id: int
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True
