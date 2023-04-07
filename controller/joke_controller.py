import random
from typing import Optional

from sqlalchemy.orm import Session

from controller.general_exceptions import USER_ERROR, NOT_FOUND_EXCEPTION, SERVER_ERROR
from data.local.models.jokes_db import DBJoke
from data.local.orm import jokes_orm
from data.remote.get_remote_jokes import get_random_dad_joke, get_random_chuck_joke
from schemas.joke import Joke
from schemas.joke_from import JokeFrom


def get_random_joke(repository: Optional[JokeFrom] = None) -> Joke:
    if repository is None:
        repository = random.choice((JokeFrom.dad, JokeFrom.chuck))

    if repository == JokeFrom.dad:
        return get_random_dad_joke()
    elif repository == JokeFrom.chuck:
        return get_random_chuck_joke()
    else:
        raise USER_ERROR


def save_joke(db: Session, text_joke: str) -> Joke:
    try:
        new_joke: DBJoke = jokes_orm.create_joke(db, text_joke)
    except Exception:
        raise SERVER_ERROR

    return Joke(
        id=new_joke.id_joke,
        joke=new_joke.joke,
        joke_from=JokeFrom.user
    )


def update_joke(db: Session, id_joke: int, text_joke: str) -> Joke:
    try:
        updated_joke: DBJoke = jokes_orm.update_joke(db, id_joke, text_joke)
    except ValueError:
        raise NOT_FOUND_EXCEPTION
    except Exception:
        raise SERVER_ERROR

    return Joke(
        id=updated_joke.id_joke,
        joke=updated_joke.joke,
        joke_from=JokeFrom.user
    )


def delete_joke(db: Session, id_joke: int) -> bool:
    try:
        deleted_joke: DBJoke = jokes_orm.delete_joke(db, id_joke)
    except ValueError:
        raise NOT_FOUND_EXCEPTION
    except Exception:
        raise SERVER_ERROR

    if not deleted_joke.dropped:
        raise USER_ERROR

    return deleted_joke.dropped
