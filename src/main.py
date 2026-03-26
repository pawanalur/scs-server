from fastapi import FastAPI
from routers import users_router

app = FastAPI(title = "SCS Server")
app.include_router(users_router.router)

@app.get("/")
async def root():
    return {"message": "API Running"}