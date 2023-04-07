from sqlalchemy.orm import Session

from data.local.models.jokes_db import DBJoke


def create_joke(db: Session, text_joke: str) -> DBJoke:
    new_joke = DBJoke(
        joke=text_joke
    )

    try:
        db.add(new_joke)
        db.commit()
        db.refresh(new_joke)
    except Exception as e:
        db.rollback()
        print(e)
        raise e

    return new_joke


def find_joke_by_id(db: Session, id_joke: int, mode: str = 'active') -> DBJoke:
    try:
        if mode == 'active':
            joke = db.query(DBJoke).where(
                DBJoke.id_joke == id_joke,
                DBJoke.dropped == False
            ).one_or_none()
        else:
            joke = db.query(DBJoke).where(
                DBJoke.id_joke == id_joke
            ).one_or_none()
    except Exception as e:
        print(e)
        raise e

    if joke is None:
        raise ValueError("Joke not found")

    return joke


def update_joke(db: Session, id_joke: int, text_joke: str) -> DBJoke:
    try:
        joke = find_joke_by_id(db, id_joke)
        joke.joke = text_joke

        try:
            db.commit()
            db.refresh(joke)
        except Exception as e:
            db.rollback()
            raise e

    except Exception as e:
        print(e.__cause__)
        raise e

    return joke


def delete_joke(db: Session, id_joke: int) -> DBJoke:
    try:
        joke = find_joke_by_id(db, id_joke)
        joke.dropped = True

        try:
            db.commit()
            db.refresh(joke)
        except Exception as e:
            db.rollback()
            raise e

    except Exception as e:
        print(e.__cause__)
        raise e

    return joke
