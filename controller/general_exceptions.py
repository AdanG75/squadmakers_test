from fastapi import HTTPException
from starlette import status

NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Impossible get joke in this moment. Please try later"
)

SERVER_ERROR = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="An internal error occurs. Please contact the platform administrator"
)

USER_ERROR = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Request not valid. Check it, please"
)

NEGATIVE_NUMBER = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Only positive integer numbers are allowed to obtain least common multiple"
)
