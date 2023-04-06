from controller.general_exceptions import USER_ERROR
from data.remote.get_remote_jokes import get_random_dad_joke, get_random_chuck_joke
from schemas.joke import Joke
from schemas.joke_from import JokeFrom


def get_random_joke(repository: JokeFrom) -> Joke:
    if repository == JokeFrom.dad:
        return get_random_dad_joke()
    elif repository == JokeFrom.chuck:
        return get_random_chuck_joke()
    else:
        raise USER_ERROR
