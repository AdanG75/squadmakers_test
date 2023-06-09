from typing import List

from fastapi import APIRouter, Path, Query
from starlette import status

from controller.number_controller import get_lcm_of_a_integer_list, add_one as add_one_c
from schemas.number_schema import NumberResponse

router = APIRouter(
    prefix='/numbers',
    tags=['numbers']
)


@router.get(
    path='/mcm/',
    status_code=status.HTTP_200_OK,
    response_model=NumberResponse,
    summary='Least Common Multiple'
)
async def get_least_common_multiple(
        numbers: List[int] = Query(None)
):
    """
    GET the least common multiple of all numbers passed as query parameters

    **Query parameter**
    - numbers(List[int]): List of integers numbers

    **Response**
    - Response body of type **NumberResponse** with status code 200
    """
    if numbers is not None and len(numbers) > 0:
        result: int = get_lcm_of_a_integer_list(numbers)
    else:
        result: int = 0

    return NumberResponse(
        operation="Least Common Multiple",
        result=result
    )


@router.get(
    path='/add-one/{number}/',
    status_code=status.HTTP_200_OK,
    response_model=NumberResponse,
    summary='Plus one'
)
async def add_one(
        number: int = Path(...)
):
    """
    GET the value of \'number\' plus one

    **Path parameter**
    - number(int): Value which the system will add one

    **Response**
    - Response body of type **NumberResponse** with status code 200
    """
    result: int = add_one_c(number)

    return NumberResponse(
        operation="Add one",
        result=result
    )
