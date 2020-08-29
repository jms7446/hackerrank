import sys


def calc_active_count(states):
    return sum(s == 'Y' for s in states)


def encode_state(raw_states):
    # for right most bit represent node 0, we reverse the string.
    states = reversed(['1' if c == 'Y' else '0' for c in raw_states])
    return int(''.join(states), base=2)


def iter_by_active(state, n, cond=1):
    for i in range(n):
        if state % 2 == cond:
            yield i
        state //= 2


def iter_active(state, n):
    return iter_by_active(state, n, cond=1)


def iter_inactive(state, n):
    return iter_by_active(state, n, cond=0)


def solve(N, costs, raw_states, P):
    def loop(state, left):
        if left == 0:
            return 0

        if memory[state] is not None:
            return memory[state]

        candidates = []
        for src in iter_active(state, N):
            for dst in iter_inactive(state, N):
                next_state = state | (1 << dst)
                candidate = costs[src][dst] + loop(next_state, left - 1)
                candidates.append(candidate)
        memory[state] = min(candidates)
        return memory[state]

    memory = [None] * (2 ** N)
    active_count = calc_active_count(raw_states)
    if active_count >= P:
        return 0
    elif active_count == 0:
        return -1
    start_state = encode_state(raw_states)
    return loop(start_state, P - active_count)


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    costs = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    raw_states = stdin.readline().strip()
    P = int(stdin.readline())
    print(solve(N, costs, raw_states, P))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
3
0 10 11
10 0 12
12 13 0
YNN
3
""".strip()
    assert get_output_with_stdin(main, in_str) == "21"
