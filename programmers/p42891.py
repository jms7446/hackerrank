from operator import itemgetter


def iter_gaps_with_indices(xs):
    """

    ex) input  : [3, 1, 2]
        output : [(1, 1), (2, 1), (0, 1)]
    """
    idx_with_xs = sorted(enumerate(xs), key=itemgetter(1))   # ex) [(1, 1), (2, 2), (0, 3)]
    yield idx_with_xs[0]
    for (_, pt), (idx, t) in zip(idx_with_xs, idx_with_xs[1:]):
        yield idx, t - pt


def solution(food_times, k):
    remain_time = k
    remain_food_count = len(food_times)
    remain_foods = [True] * len(food_times)
    for idx, food_time in iter_gaps_with_indices(food_times):
        if food_time * remain_food_count > remain_time:
            break
        remain_time -= food_time * remain_food_count
        remain_food_count -= 1
        remain_foods[idx] = False
    else:
        return -1
    nth = remain_time % remain_food_count
    compact_indices = [idx for idx, remained in enumerate(remain_foods) if remained]
    result = compact_indices[nth]
    return result + 1     # convert to 1-start index


def test_solution():
    assert solution([3, 1, 2], 5) == 1
    assert solution([1, 2, 3, 4], 8) == 4
    assert solution([1, 1], 2) == -1
