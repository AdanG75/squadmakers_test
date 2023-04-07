from fastapi import APIRouter, Path, Query, Depends
from sqlalchemy.orm import Session
from starlette import status

from controller import joke_controller
from data.local.database import get_db
from schemas.basic_response import BasicResponse
from schemas.joke import Joke
from schemas.joke_from import JokeFrom

router = APIRouter(
    prefix='/jokes',
    tags=['jokes']
)


@router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    response_model=Joke,
    tags=['jokes']
)
async def get_random_joke():
    response = joke_controller.get_random_joke()

    return response


@router.get(
    path='/{repository}/',
    status_code=status.HTTP_200_OK,
    response_model=Joke,
    tags=['jokes']
)
async def get_random_joke_by_repository(
        repository: JokeFrom = Path(...)
):
    response = joke_controller.get_random_joke(repository)

    return response


@router.post(
    path='/',
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


@router.patch(
    path='/{number}/',
    status_code=status.HTTP_200_OK,
    response_model=Joke,
    tags=['jokes']
)
async def update_joke(
        number: int = Path(..., gt=0, lt=4294967296),
        joke: str = Query(None, min_length=4, max_length=999),
        db: Session = Depends(get_db)
):
    response = joke_controller.update_joke(db, number, joke)

    return response


@router.delete(
    path='/{number}/',
    status_code=status.HTTP_200_OK,
    response_model=BasicResponse,
    tags=['jokes']
)
async def delete_joke(
        number: int = Path(..., gt=0, lt=4294967296),
        db: Session = Depends(get_db)
):
    result: bool = joke_controller.delete_joke(db, number)

    return BasicResponse(
        operation="Deleted joke with id: {}".format(number),
        successful=result
    )
