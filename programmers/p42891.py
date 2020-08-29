from operator import itemgetter


def iter_gaps_with_indices(xs):
    idx_with_xs = sorted(enumerate(xs), key=itemgetter(1))
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
    return [idx for idx, remained in enumerate(remain_foods) if remained][nth] + 1


def test_main():
    assert solution([3, 1, 2], 5) == 1
