import sys
from heapq import heappop, heappush
from collections import namedtuple

People = namedtuple("People", ["start", "end"])


def solve(N, people):
    people = sorted(people, reverse=True)
    standby = []
    count = 0
    for n in range(N):
        while people and people[-1][0] == n:
            heappush(standby, people.pop()[1])
        while standby:
            if heappop(standby) >= n:
                count += 1
                break
    return count


def main():
    stdin = sys.stdin
    PN = int(stdin.readline())
    for _ in range(PN):
        N, M = [int(x) for x in stdin.readline().split()]
        people = [[int(x) - 1 for x in stdin.readline().split()] for _ in range(M)]
        print(solve(N, people))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin, iter_run


def test_main():
    in_str = """
1
2 3
1 2
1 2
1 2
""".strip()
    assert get_output_with_stdin(main, in_str) == "2"


def gen_prob(N, M):
    import random
    random.seed(3)
    people = [list(sorted([random.randint(0, N - 1) for _ in range(2)])) for _ in range(M)]
    return N, people


# iter_run(solve, loop=200, gen=lambda: gen_prob(1000, 800))
