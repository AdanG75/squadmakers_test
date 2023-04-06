from fastapi import FastAPI

app = FastAPI(
    title="SquadMakers Test",
    version="0.0.0"
)


@app.get(
    path='/'
)
async def root():
    return {"hello": "word"}
