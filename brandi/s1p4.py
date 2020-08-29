import sys

"""

"""


def solve(N, d, xs):
    return -1


def main():
    stdin = sys.stdin
    N, d = [int(x) for x in stdin.readline().split()]
    xs = [int(line) for line in stdin.readlines()]
    print(solve(N, d, xs))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
6 2
0 0 0 0 0 1 
0 0 0 0 0 0 
0 0 0 0 0 0 
0 0 0 0 0 0 
0 0 1 0 0 0 
1 0 0 0 0 0 
    '''.strip()
    out_str = '''
13
    '''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main2():
    in_str = '''
5 3
0 0 0 0 0 
0 0 0 0 0 
0 0 0 1 0 
0 0 0 0 0 
1 0 0 0 0 
    '''.strip()
    out_str = '''
19
    '''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main3():
    in_str = '''
6 2
0 0 0 0 0 0 
0 0 0 0 0 0 
0 0 0 0 1 0 
0 0 0 0 0 0 
0 0 1 0 0 0 
0 0 0 0 0 0 
    '''.strip()
    out_str = '''
12
    '''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
