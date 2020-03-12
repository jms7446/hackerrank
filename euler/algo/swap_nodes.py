#!/bin/python3

import os
import sys


LEFT = 0
RIGHT = 1


# FIXME stack overflow 가 생김. recursion으로 구현된 것을 while 으로 풀어서 구현할 것


def swapNodes(indexes, queries):
    traversed_list = []
    for query in queries:
        swap_op(indexes, query)
        traversed = traverse(indexes)
        traversed_list.append(traversed)
    return traversed_list


def swap_op(indexes, query):
    def swap(node, depth):
        if node == -1:
            return
        node_idx = node - 1
        if depth % query == 0:
            indexes[node_idx].reverse()
        swap(indexes[node_idx][LEFT], depth + 1)
        swap(indexes[node_idx][RIGHT], depth + 1)

    swap(1, 1)


def traverse(indexes):
    def _loop(node):
        if node == -1:
            return
        idx = node - 1
        _loop(indexes[idx][LEFT])
        acc.append(node)
        _loop(indexes[idx][RIGHT])

    acc = []
    _loop(1)
    return acc


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()


def test_traverse():
    assert traverse([[2, 3], [-1, -1], [-1, -1]]) == [2, 1, 3]
    assert traverse([[2, 3], [4, -1], [-1, -1], [-1, -1]]) == [4, 2, 1, 3]


def test_swapNode0():
    indexes = [
        [2, 3],
        [-1, -1],
        [-1, -1],
    ]
    assert swapNodes(indexes, [1, 1]) == [[3, 1, 2], [2, 1, 3]]


def test_swapNode1():
    indexes = [
        [2, 3],
        [-1, 4],
        [-1, 5],
        [-1, -1],
        [-1, -1],
    ]
    assert swapNodes(indexes, [2]) == [[4, 2, 1, 5, 3]]


def test_swapNode2():
    indexes = [
        [2, 3],
        [4, 5],
        [6, -1],
        [-1, 7],
        [8, 9],
        [10, 11],
        [12, 13],
        [-1, 14],
        [-1, -1],
        [15, -1],
        [16, 17],
        [-1, -1],
        [-1, -1],
        [-1, -1],
        [-1, -1],
        [-1, -1],
        [-1, -1],
    ]
    expected = [
        [14, 8, 5, 9, 2, 4, 13, 7, 12, 1, 3, 10, 15, 6, 17, 11, 16],
        [9, 5, 14, 8, 2, 13, 7, 12, 4, 1, 3, 17, 11, 16, 6, 10, 15],
    ]
    assert swapNodes(indexes, [2, 3]) == expected
