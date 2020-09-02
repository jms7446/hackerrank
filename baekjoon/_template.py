import sys


def solve():
    return -1


def main():
    stdin = sys.stdin
    T = int(stdin.readline())
    N, M = [int(x) for x in stdin.readline().split()]
    X = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    S = [stdin.readline().strip() for _ in range(H)]
    print(solve())


if __name__ == "__main__":
    main()


from util import *
import pytest


def test_main():
    in_str = """

    """.strip()
    out_str = """

    """.strip()
    assert mock_io(main)(in_str) == out_str


@pytest.mark.parametrize(('in_str', 'out_str'), [
    ('''
    
    '''.strip(),
     '''
     
     '''.strip()),
])
def test_main(in_str, out_str):
    assert mock_io(main)(in_str) == out_str
