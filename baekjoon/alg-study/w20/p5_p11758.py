import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __sub__(self, other: 'Point'):
        """return (self - other)"""
        return Point(self.x - other.x, self.y - other.y)

    @staticmethod
    def cross_product_z(p1: 'Point', p2: 'Point'):
        """return z(3rd) element of cross product (p1 X p2 = (0, 0, z)"""
        return p1.x * p2.y - p1.y * p2.x


def sign(x):
    return (x > 0) - (x < 0)


def solve(vectors):
    p1, p2, p3 = [Point(*vector) for vector in vectors]
    z = Point.cross_product_z(p2 - p1, p3 - p2)
    return sign(z)


def main():
    stdin = sys.stdin
    points = [[int(x) for x in stdin.readline().split()] for _ in range(3)]
    print(solve(points))


if __name__ == "__main__":
    main()

from util import *
import pytest


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
1 1
5 5
7 3
    '''.strip(), '-1'.strip()),
    ('''
1 1
3 3
5 5
    '''.strip(), '0'.strip()),
    ('''
1 1
7 3
5 5
    '''.strip(), '1'.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
