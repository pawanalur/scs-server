from fastapi import FastAPI
from routers import users_router
from database import engine, Base
# Registering models before create_all
import models  # type: ignore
import warnings
from sqlalchemy.exc import SAWarning

warnings.filterwarnings(
    "ignore",
    message="Unrecognized server version info",
    category=SAWarning,
)


Base.metadata.create_all(bind=engine)
app = FastAPI(title = "SCS Server")
app.include_router(users_router.router)

@app.get("/")
async def root():
    return {"message": "API Running"}