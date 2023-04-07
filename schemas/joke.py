from pydantic import BaseModel, Field

from schemas.joke_from import JokeFrom


class Joke(BaseModel):
    id: int = Field(None, gt=0, lt=4294967296)
    joke: str = Field(..., min_length=2, max_length=999)
    joke_from: JokeFrom = Field(...)
