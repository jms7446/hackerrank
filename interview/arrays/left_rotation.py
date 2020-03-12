#!/bin/python3

import os


# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:] + a[:d]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


def test_rotLeft():
    assert rotLeft([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
    assert rotLeft([1, 2, 3, 4, 5], 4) == [5, 1, 2, 3, 4]
