from pydantic import BaseModel, Field


class BasicResponse(BaseModel):
    operation: str = Field(..., min_length=4, max_length=999)
    successful: bool = Field(...)
