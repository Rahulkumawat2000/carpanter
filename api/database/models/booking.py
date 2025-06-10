from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from api.database.connection import Base

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    user_id_fk = Column(Integer, ForeignKey('users.id'), nullable=False)
    from_location = Column(String(100), nullable=False)  # Added length (e.g., 100)
    to_location = Column(String(100), nullable=False)    # Added length (e.g., 100)
    seats = Column(Integer, nullable=False)
    price_per_seat = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(String(50), default="CURRENT_TIMESTAMP", nullable=False)
    updated_at = Column(String(50), default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP", nullable=False)

    user = relationship("User", back_populates="bookings")