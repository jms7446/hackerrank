import sys

INF = 1000000000


def solve(N, edges):
    dists = [[INF] * N for _ in range(N)]
    for x in range(N):
        dists[x][x] = 0
    for x, y in edges:
        dists[x][y] = 1
        dists[y][x] = 1
    for v in range(N):
        for s in range(N):
            for e in range(N):
                dists[s][e] = min(dists[s][e], dists[s][v] + dists[v][e])

    scores = [max(ds) for ds in dists]
    min_score = min(scores)
    min_vs = [v for v, score in enumerate(scores) if score == min_score]
    return min_score, min_vs


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    edges = [[int(x) - 1 for x in line.split()] for line in stdin.readlines()][:-1]
    min_score, min_vs = solve(N, edges)
    min_vs = [v + 1 for v in min_vs]
    print(min_score, len(min_vs))
    print(*min_vs)


if __name__ == "__main__":
    main()

from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1
    """.strip()
    out_str = """
2 3
2 3 4
    """.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_add1():
    in_str = """
2
1 2
-1 -1
    """.strip()
    out_str = """
1 2
1 2
    """.strip()
    assert get_output_with_stdin(main, in_str) == out_str
