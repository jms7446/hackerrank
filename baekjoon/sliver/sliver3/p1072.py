import sys


def calc(x, y):
    if x == 0:
        return 1
    p = int(100 * y / x)
    if p >= 99:
        return -1
    a, b = divmod((p + 1) * x - 100 * y, 99 - p)
    if b != 0:
        a += 1
    return a


def main():
    stdin = sys.stdin
    X, Y = [int(s) for s in stdin.readline().split()]
    print(calc(X, Y))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


import random


def naive_solution(x, y):
    if x == 0:
        return 1
    p = int(100 * y / x)
    if p >= 99:
        return -1
    for i in range(1, 2000000):
        if int(100 * (y + i) / (x + i)) != p:
            return i
    else:
        raise Exception(f'{x}, {y} exceed limit of for loop')


def gen_test_set():
    N = 10000000
    x = random.randint(0, N)
    y = random.randint(0, x)
    return x, y


def _test_compare():
    for _ in range(10):
        x, y = gen_test_set()
        s1 = naive_solution(x, y)
        s2 = calc(x, y)
        if s1 != s2:
            print(x, y, s1, s2)
            assert False


def test_main():
    in_str = '''
10 8
    '''.strip()

    out_str = '''
1
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main2():
    in_str = '''
100 80
    '''.strip()

    out_str = '''
6
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main3():
    in_str = '''
0 0
    '''.strip()

    out_str = '''
1
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main4():
    in_str = '''
1000000000 999999999
    '''.strip()

    out_str = '''
-1
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main5():
    in_str = '''
5 5
    '''.strip()

    out_str = '''
-1
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main6():
    in_str = '''
5377378 4800373
    '''.strip()

    out_str = '''
392672
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
