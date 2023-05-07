
from .maths import odd_numbers


def test_odd_numbers_has_the_correct_length():
    result = odd_numbers(1,100)
    assert(50 == len(result))

def test_odd_numbers_has_the_correct_first_element():
    result = odd_numbers(1,100)
    assert(1 == result[0])

def test_odd_numbers_has_the_correct_last_element():
    result = odd_numbers(1,100)
    assert(99 == result[-1])
