import sys
from heapq import heappush, heappop


def solve(cranes, boxes):
    crane_heap = []
    cranes = sorted(cranes)
    boxes = sorted(boxes, reverse=True)
    if cranes[-1] < boxes[0]:
        return -1

    for box in boxes:
        while cranes and cranes[-1] >= box:
            heappush(crane_heap, (0, cranes.pop()))
        count, crane = heappop(crane_heap)
        heappush(crane_heap, (count + 1, crane))

    return max(crane_heap)[0]


def main():
    stdin = sys.stdin
    _ = stdin.readline()
    cranes = [int(x) for x in stdin.readline().split()]
    _ = stdin.readline()
    boxes = [int(x) for x in stdin.readline().split()]
    print(solve(cranes, boxes))


if __name__ == "__main__":
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = """
3
6 8 9
5
2 5 2 4 7    
""".strip()
    assert get_output_with_stdin(main, in_str) == "2"
