from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from api.database.connection import Base

class Travels(Base):
    __tablename__ = "travels"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String(255), nullable=True)  # 👈 image ka column add kiya, maximum length 255
    from_location = Column(String(100), nullable=False)  # 👈 length 100
    to_location = Column(String(100), nullable=False)    # 👈 length 100
    time = Column(String(50), nullable=False)         # 👈 length 50 (time ka format jyada bada nahi hota)
    seats = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
