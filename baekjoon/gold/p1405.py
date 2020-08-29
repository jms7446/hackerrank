import sys

directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def solve(N, probs):
    def loop(n, pos, prob):
        if n == 0:
            return prob

        prob_sum = 0
        x, y = pos
        for dx, dy, d_prob in dir_probs:
            nx, ny = x + dx, y + dy
            if not visited[nx][ny]:
                visited[nx][ny] = True
                prob_sum += loop(n - 1, (nx, ny), prob * d_prob)
                visited[nx][ny] = False
        return prob_sum

    probs = [p / 100 for p in probs]
    dir_probs = [(x, y, p) for (x, y), p in (zip(directions, probs))]
    S = 2 * N + 1
    visited = [[False] * S for _ in range(S)]
    visited[N][N] = True
    return loop(N, (N, N), 1)


def main():
    stdin = sys.stdin
    xs = [int(x) for x in stdin.readline().split()]
    N = xs[0]
    probs = xs[1:]
    print(solve(N, probs))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
2 25 25 25 25
    """.strip()
    assert get_output_with_stdin(main, in_str) == "0.75"
