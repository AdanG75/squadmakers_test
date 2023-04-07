from typing import List

from fastapi import APIRouter, Path, Query
from starlette import status

from controller.number_controller import get_lcm_of_a_integer_list, add_one
from schemas.number_schema import NumberResponse

router = APIRouter(
    prefix='/numbers',
    tags=['numbers']
)


@router.get(
    path='/mcm/',
    status_code=status.HTTP_200_OK,
    response_model=NumberResponse
)
async def get_least_common_multiple(
        numbers: List[int] = Query(None, min_length=1, max_length=99)
):
    result: int = get_lcm_of_a_integer_list(numbers)

    return NumberResponse(
        operation="Least Common Multiple",
        result=result
    )


@router.get(
    path='/add-one/{number}/',
    status_code=status.HTTP_200_OK,
    response_model=NumberResponse
)
async def add_one(
        number: int = Path(...)
):
    result: int = add_one(number)

    return NumberResponse(
        operation="Add one",
        result=result
    )
