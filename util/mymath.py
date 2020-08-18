import operator as op
from functools import reduce


def number_to_digits(num, base=10, length=None):
    digits = []
    while num > 0:
        digits.append(num % base)
        num //= base
    if length is not None:
        padding = [0] * (length - len(digits))
        digits += padding

    return list(reversed(digits))


def digits_to_number(digits, base=10):
    num = 0
    for digit in digits:
        num = num * base + digit
    return num


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom
