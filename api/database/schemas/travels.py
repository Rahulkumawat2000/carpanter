from pydantic import BaseModel
from datetime import datetime

class TravelBase(BaseModel):
    image: str
    from_location: str
    to_location: str
    time: str
    seats: int
    price: float

class TravelCreate(TravelBase):
    pass

class TravelUpdate(TravelBase):
    pass

class TravelResponse(TravelBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes= True
