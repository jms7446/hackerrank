import sys
from dataclasses import dataclass
from typing import List


@dataclass
class Hotel:
    cost: int
    num_rooms: List[int]


def calc_min_cost(num_rooms_needed, budget, hotels: List[Hotel]):
    for hotel in sorted(hotels, key=lambda h: h.cost):
        total_cost = hotel.cost * num_rooms_needed
        if total_cost > budget:
            return None
        if max(hotel.num_rooms) >= num_rooms_needed:
            return total_cost


def main():
    stdin = sys.stdin
    N, B, num_hotels, num_weeks = [int(x) for x in stdin.readline().split()]
    hotels = []
    for _ in range(num_hotels):
        cost = int(stdin.readline())
        num_rooms = [int(x) for x in stdin.readline().split()]
        hotels.append(Hotel(cost, num_rooms))

    min_cost = calc_min_cost(N, B, hotels)
    if min_cost is not None:
        print(min_cost)
    else:
        print('stay home')


if __name__ == '__main__':
    main()


from util.result_check import get_output_with_stdin


def test_main():
    in_str = '''
3 1000 2 3
200
0 2 2
300
27 3 20    
    '''.strip()

    out_str = '''
900
'''.strip()
    assert get_output_with_stdin(main, in_str) == out_str
