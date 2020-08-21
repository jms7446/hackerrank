import sys


def calc_min_combination(xs, ws):
    xs = sorted(xs)
    ws = sorted(ws, reverse=True)
    return sum(w * x for w, x in zip(ws, xs))


def main():
    stdin = sys.stdin
    _ = stdin.readline().strip()
    xs = [int(x) for x in stdin.readline().split()]
    ws = [int(x) for x in stdin.readline().split()]
    print(calc_min_combination(xs, ws))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
5
1 1 1 6 0
2 7 8 3 1
    '''.strip()

    out_str = '''
18
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
