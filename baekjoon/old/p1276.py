import sys


def solve2(bridges):
    width = max(bridges, key=lambda b: b[2])[2]
    heights = [0] * width
    bridges = sorted(bridge for bridge in bridges)
    result = 0
    for y, x1, x2 in bridges:
        result += y - heights[x1]
        result += y - heights[x2 - 1]
        for x in range(x1, x2):
            heights[x] = y
    return result


def solve(bridges):
    bridges = sorted(bridge for bridge in bridges)
    result = 0
    for i, (y, x1, x2) in enumerate(bridges):
        result += 2 * y
        for j in reversed(range(i)):
            b = bridges[j]
            if b[1] <= x1 < b[2]:
                result -= b[0]
                break
        for j in reversed(range(i)):
            b = bridges[j]
            if b[1] <= x2 - 1 < b[2]:
                result -= b[0]
                break

    return result


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    bs = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    print(solve(bs))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin, iter_run


def test_main():
    in_str = """
3
1 5 10
3 1 5
5 3 7
""".strip()
    assert get_output_with_stdin(main, in_str) == "14"


def gen(N, M):
    import random
    random.seed(1)

    def f(m, x1, w):
        return m, x1, x1 + w

    bs = [f(m, random.randint(1, M), random.randint(1, M)) for m in range(N)]
    return bs,


# if __name__ == "__main__":
#     iter_run(solve, loop=100, gen=lambda: gen(100, 5000))

