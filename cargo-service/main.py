from fastapi import FastAPI
from .routes import router as cargo_router

app = FastAPI(title="Sea Freight Cargo Service")
app.include_router(cargo_router)
