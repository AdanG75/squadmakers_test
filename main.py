from fastapi import FastAPI

from core.settings import charge_settings
from routers import joke_router, number_router

app = FastAPI(
    title="SquadMakers Test",
    version="0.3.2"
)


@app.on_event("startup")
async def startup_event():
    settings = charge_settings()


# Adding routers
app.include_router(router=joke_router.router)
app.include_router(router=number_router.router)


@app.get(
    path='/',
    tags=['main']
)
async def root():
    return {"hello": "world"}
