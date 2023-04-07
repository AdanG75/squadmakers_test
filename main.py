
from fastapi import FastAPI, Path, Query, Depends
from sqlalchemy.orm import Session
from starlette import status

from controller import joke_controller
from core.settings import charge_settings
from data.local.database import get_db
from schemas.basic_response import BasicResponse
from schemas.joke import Joke
from schemas.joke_from import JokeFrom

app = FastAPI(
    title="SquadMakers Test",
    version="0.1.0"
)


@app.on_event("startup")
async def startup_event():
    settings = charge_settings()


@app.get(
    path='/',
    tags=['main']
)
async def root():
    return {"hello": "world"}


@app.get(
    path='/jokes/',
    status_code=status.HTTP_200_OK,
    response_model=Joke,
    tags=['jokes']
)
async def get_random_joke():
    response = joke_controller.get_random_joke()

    return response


@app.get(
    path='/jokes/{repository}/',
    status_code=status.HTTP_200_OK,
    response_model=Joke,
    tags=['jokes']
)
async def get_random_joke_by_repository(
        repository: JokeFrom = Path(...)
):
    response = joke_controller.get_random_joke(repository)

    return response


@app.post(
    path='/jokes/',
    status_code=status.HTTP_201_CREATED,
    response_model=Joke,
    tags=['jokes']
)
async def save_joke(
        joke: str = Query(None, min_length=4, max_length=999),
        db: Session = Depends(get_db)
):
    if joke is None:
        return joke_controller.get_random_joke()

    response = joke_controller.save_joke(db, joke)

    return response


@app.patch(
    path='/jokes/{id_joke}/',
    status_code=status.HTTP_200_OK,
    response_model=Joke,
    tags=['jokes']
)
async def update_joke(
        id_joke: int = Path(..., gt=0, lt=4294967296),
        joke: str = Query(None, min_length=4, max_length=999),
        db: Session = Depends(get_db)
):
    response = joke_controller.update_joke(db, id_joke, joke)

    return response


@app.delete(
    path='/jokes/{id_joke}/',
    status_code=status.HTTP_200_OK,
    response_model=BasicResponse,
    tags=['jokes']
)
async def delete_joke(
        id_joke: int = Path(..., gt=0, lt=4294967296),
        db: Session = Depends(get_db)
):
    result: bool = joke_controller.delete_joke(db, id_joke)

    return BasicResponse(
        operation="Deleted joke with id: {}".format(id_joke),
        successful=result
    )
