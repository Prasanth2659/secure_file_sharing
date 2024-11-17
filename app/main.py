from fastapi import FastAPI
from app.routes.ops_routes import router as ops_router
from app.routes.client_routes import router as client_router
from app.db import Base, engine

# Initialize the database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure File Sharing System",
    description="A secure REST API for file sharing between ops and client users",
    version="1.0.0",
)

# Include routers
app.include_router(ops_router, prefix="/ops", tags=["Ops User"])
app.include_router(client_router, prefix="/client", tags=["Client User"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Secure File Sharing System API!"}
