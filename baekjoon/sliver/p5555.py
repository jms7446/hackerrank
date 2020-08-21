import sys


def has_ptn_in_ring(ptn, ring):
    return ptn in (ring * 2)


def main():
    stdin = sys.stdin
    target = stdin.readline().strip()
    num_ring = int(stdin.readline())
    rings = [line.strip() for line in stdin.readlines()]
    print(sum(has_ptn_in_ring(target, ring) for ring in rings))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
ABCD
3
ABCDXXXXXX
YYYYABCDXX
DCBAZZZZZZ
    '''.strip()

    out_str = '''
2
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main2():
    in_str = '''
XYZ
1
ZAAAAAAAXY
    '''.strip()

    out_str = '''
1
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main3():
    in_str = '''
PQR
3
PQRAAAAPQR
BBPQRBBBBB
CCCCCCCCCC
    '''.strip()

    out_str = '''
2
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
