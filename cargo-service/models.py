from pydantic import BaseModel
from datetime import datetime

class Cargo(BaseModel):
    id: int
    description: str
    weight: float
    origin_port: str
    destination_port: str
    booking_date: datetime
    status: str
