from fastapi import APIRouter, HTTPException
from .models import Cargo
from datetime import datetime

router = APIRouter(prefix="/cargo", tags=["cargo"])

# In-memory store for demo purposes
_cargo_db = {}

@router.post("/book", response_model=Cargo)
async def book_cargo(cargo: Cargo):
    if cargo.id in _cargo_db:
        raise HTTPException(status_code=400, detail="Cargo ID already exists")
    cargo.status = "BOOKED"
    cargo.booking_date = datetime.utcnow()
    _cargo_db[cargo.id] = cargo
    return cargo

@router.get("/list", response_model=list[Cargo])
async def list_cargo():
    return list(_cargo_db.values())
