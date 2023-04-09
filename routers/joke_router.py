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
    tags=['jokes'],
    summary="Get random Joke"
)
async def get_random_joke():
    """
    GET a random joke from Dad or Chuck repository

    **Response**
    - Return a response body of type \'Joke\' with status code 200
    """
    response = joke_controller.get_random_joke()

    return response


@router.get(
    path='/{repository}/',
    status_code=status.HTTP_200_OK,
    response_model=Joke,
    tags=['jokes'],
    summary='Get random joke based on repository'
)
async def get_random_joke_by_repository(
        repository: JokeFrom = Path(...)
):
    """
    GET a random joke based on the repository passed as path parameter

    **Path parameter**
    - repository (Dad | Chuck): String with value \'Chuck\' or \'Dad\' which specify the repository where system fetch

    **Response**
    - Return a response body of type \'Joke\' with status code 200
    """
    response = joke_controller.get_random_joke(repository)

    return response


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    response_model=Joke,
    tags=['jokes'],
    summary='Save Joke'
)
async def save_joke(
        joke: str = Query(None, min_length=4, max_length=999),
        db: Session = Depends(get_db)
):
    """
    POST a joke into the system

    **Query parameter**
    - joke(str): String which represents the joke to be saved

    **Response**
    - Return a response body of type \'Joke\' with the joke sent it as query parameter. As the same way,
    the response body have a status code 201
    """
    if joke is None:
        return joke_controller.get_random_joke()

    response = joke_controller.save_joke(db, joke)

    return response


@router.patch(
    path='/{number}/',
    status_code=status.HTTP_200_OK,
    response_model=Joke,
    tags=['jokes'],
    summary='Update joke'
)
async def update_joke(
        number: int = Path(..., gt=0, lt=4294967296),
        joke: str = Query(None, min_length=4, max_length=999),
        db: Session = Depends(get_db)
):
    """
    PATCH a saved joke with id equal to \'number\' and replacing the joke using the passed as query parameter

    **Path parameter**
    - number(int): Integer number which represents the identifier of the joke

    **Query parameter**
    - joke(str): The text of the joke which replace the old joke saved

    **Response**
    - Return a response body of type \'Joke\' with the joke sent it as query parameter. As the same way,
    the response body have a status code 200
    """
    response = joke_controller.update_joke(db, number, joke)

    return response


@router.delete(
    path='/{number}/',
    status_code=status.HTTP_200_OK,
    response_model=BasicResponse,
    tags=['jokes'],
    summary='Delete joke'
)
async def delete_joke(
        number: int = Path(..., gt=0, lt=4294967296),
        db: Session = Depends(get_db)
):
    """
    Delete a saved joke with id equal to \'number\'

    **Path parameter**
    - number(int): Integer number which represents the identifier of the joke

    **Response**
    - A response body of type **Basic Response** and status code with value 200
    """
    result: bool = joke_controller.delete_joke(db, number)

    return BasicResponse(
        operation="Deleted joke with id: {}".format(number),
        successful=result
    )
