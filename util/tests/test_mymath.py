from util import mymath


def test_number_to_digits():
    assert mymath.number_to_digits(12) == [1, 2]
    assert mymath.number_to_digits(12, base=3) == [1, 1, 0]
    assert mymath.number_to_digits(12, base=3, length=5) == [0, 0, 1, 1, 0]


def test_digits_to_number():
    assert mymath.digits_to_number([1, 2]) == 12
    assert mymath.digits_to_number([1, 1, 0], base=3) == 12
