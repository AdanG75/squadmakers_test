from math import lcm
from typing import List

from controller.general_exceptions import NEGATIVE_NUMBER, LIST_TOO_BIG


def is_a_negative_number(number_list: List[int]) -> bool:
    for number in number_list:
        if number < 0:
            return True

    return False


def get_lcm_of_a_integer_list(number_list: List[int]) -> int:
    if len(number_list) > 99:
        raise LIST_TOO_BIG

    if is_a_negative_number(number_list):
        raise NEGATIVE_NUMBER

    return lcm(*number_list)


def add_one(number: int) -> int:
    return number + 1
