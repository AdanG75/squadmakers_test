import requests
from fastapi import HTTPException
from starlette import status

from controller.general_exceptions import NOT_FOUND_EXCEPTION, USER_ERROR, SERVER_ERROR
from schemas.joke import Joke
from schemas.joke_from import JokeFrom


def get_random_chuck_joke() -> Joke:
    response = requests.get("https://api.chucknorris.io/jokes/random")

    if response.status_code == status.HTTP_200_OK or response.status_code < status.HTTP_400_BAD_REQUEST:
        return Joke(
            id=None,
            joke=response.json()['value'],
            joke_from=JokeFrom.chuck
        )
    else:
        raise return_exception_based_on_code(response.status_code)


def get_random_dad_joke() -> Joke:
    response = requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'application/json'})

    if response.status_code == status.HTTP_200_OK or response.status_code < status.HTTP_400_BAD_REQUEST:
        return Joke(
            id=None,
            joke=response.json()['joke'],
            joke_from=JokeFrom.dad
        )
    else:
        raise return_exception_based_on_code(response.status_code)


def return_exception_based_on_code(status_code: int) -> HTTPException:
    if status_code == status.HTTP_404_NOT_FOUND:
        return NOT_FOUND_EXCEPTION
    elif status_code >= status.HTTP_500_INTERNAL_SERVER_ERROR:
        return SERVER_ERROR
    else:
        return USER_ERROR
