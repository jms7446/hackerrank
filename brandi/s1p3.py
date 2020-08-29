import sys

INF = float('inf')


def solve(N, edges):
    """Bellman-ford"""

    def relax(fr, to, dist):
        new_dist = dists[fr] + dist
        if new_dist < dists[to]:
            dists[to] = new_dist
            return True
        return False

    START, END = 0, N - 1
    dists = [INF] * N
    dists[START] = 0
    for _ in range(N - 1):
        for n1, n2, dist in edges:
            relax(n1, n2, dist)

    # check reachable
    if dists[END] == INF:
        return -1

    # check negative cycle
    for n1, n2, dist in edges:
        if relax(n1, n2, dist):
            return -1

    return dists[END]


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    xs = [[int(x) for x in stdin.readline().split()] for _ in range(M)]
    xs = [(x[0] - 1, x[1] - 1 , x[2]) for x in xs]
    print(solve(N, xs))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
3 3
1 2 10
1 3 9
2 3 -3
    '''.strip()
    out_str = '''
7
    '''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main2():
    in_str = '''
4 4
1 2 -1
2 3 -3
1 1 -1
3 4 1
    '''.strip()
    out_str = '''
-1
    '''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_main3():
    in_str = '''
3 1
1 2 10
    '''.strip()
    out_str = '''
-1
    '''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
