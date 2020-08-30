import sys
from itertools import count
from heapq import heappush, heappop
from copy import copy

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def search_positions(lines, target):
    return [(r, c) for r, line in enumerate(lines) for c, cell in enumerate(line) if cell == target]


def traverse(graph, start):
    queue = [(0, start, set())]
    while queue:
        acc_dist, node, visited = heappop(queue)
        visited.add(node)
        if len(visited) == len(graph):
            return acc_dist
        for next_node, dist in graph[node].items():
            if next_node not in visited and dist is not None:
                item = (acc_dist + dist, next_node, copy(visited))
                heappush(queue, item)
    return -1


def fill_graph_from_node(graph, src_node, M, R, C):
    targets = get_unknown_distance_nodes(graph, src_node)
    if not targets:
        return
    visited = [[False] * C for _ in range(R)]
    visited[src_node[0]][src_node[1]] = True

    stack = [src_node]
    for step in count(1):
        if not stack:
            break
        new_stack = []
        for sr, sc in stack:
            for dr, dc in directions:
                r, c = sr + dr, sc + dc
                if visited[r][c] or M[r][c] == 'x':
                    continue
                if M[r][c] == '*' and (r, c) in targets:
                    graph[src_node][(r, c)] = step
                    graph[(r, c)][src_node] = step
                    targets.remove((r, c))
                    if not targets:
                        return
                visited[r][c] = True
                new_stack.append((r, c))
        stack = new_stack


def get_unknown_distance_nodes(graph, src_node):
    return {pos for pos, dist in graph[src_node].items() if dist is None}


def add_padding(M, R, C, cell):
    v_pad = cell * (C + 2)
    h_padded = [cell + line + cell for line in M]
    M = [v_pad] + h_padded + [v_pad]
    return M, R + 2, C + 2


def solve(R, C, M):
    M, R, C = add_padding(M, R, C, 'x')
    dusts = search_positions(M, '*')
    starts = search_positions(M, 'o')
    nodes = dusts + starts
    start = starts[0]

    graph = {src: {dst: 0 if src == dst else None for dst in nodes} for src in nodes}
    fill_graph_from_node(graph, start, M, R, C)
    if get_unknown_distance_nodes(graph, start):
        return -1
    for node in dusts:
        fill_graph_from_node(graph, node, M, R, C)
    return traverse(graph, start)


def main():
    stdin = sys.stdin
    while True:
        C, R = [int(x) for x in stdin.readline().split()]
        if R == 0:
            break
        M = [stdin.readline().strip() for _ in range(R)]
        print(solve(R, C, M))


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
2 2
o*
**
7 5
.......
.o...*.
.......
.*...*.
.......
15 13
.......x.......
...o...x....*..
.......x.......
.......x.......
.......x.......
...............
xxxxx.....xxxxx
...............
.......x.......
.......x.......
.......x.......
..*....x....*..
.......x.......
10 10
..........
..o.......
..........
..........
..........
.....xxxxx
.....x....
.....x.*..
.....x....
.....x....
0 0
    '''.strip()
    out_str = '''
3
8
49
-1
    '''.strip()
    assert get_output_with_stdin(main, in_str) == out_str


def test_elapse_time():
    import time
    in_str = '''
15 13
.......x.......
...o...x....*..
.......x.......
.......x.......
.......x.......
...............
xxxxx.....xxxxx
...............
.......x.......
.......x.......
.......x.......
..*....x....*..
.......x.......
10 10
..........
..o.......
..........
..........
..........
.....xxxxx
.....x....
.....x.*..
.....x....
.....x....
0 0
        '''.strip()
    st = time.time()
    for i in range(1000):
        get_output_with_stdin(main, in_str)
    print(f'elapse time : {time.time() - st}', file=sys.stderr)
    assert False
