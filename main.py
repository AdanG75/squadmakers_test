
from fastapi import FastAPI, Path
from starlette import status

from controller import joke_controller
from schemas.joke import Joke
from schemas.joke_from import JokeFrom

app = FastAPI(
    title="SquadMakers Test",
    version="0.0.0"
)


@app.get(
    path='/'
)
async def root():
    return {"hello": "world"}


@app.get(
    path='/jokes/{repository}/',
    status_code=status.HTTP_200_OK,
    response_model=Joke
)
async def get_random_joke(
        repository: JokeFrom = Path(...)
):
    response = joke_controller.get_random_joke(repository)

    return response
