
from collections import Counter
from heapq import heappop, heappush, heapify
from collections import deque
from typing import List, Iterator


################################################################################
# from util.tools
################################################################################

def iter_window_max(xs: List[int], k: int) -> Iterator[int]:
    queue = deque()
    for i in range(k):
        while queue and xs[queue[-1]] <= xs[i]:
            queue.pop()
        queue.append(i)
    yield xs[queue[0]]

    for i in range(k, len(xs)):
        if queue[0] == i - k:
            queue.popleft()
        while queue and xs[queue[-1]] <= xs[i]:
            queue.pop()
        queue.append(i)
        yield xs[queue[0]]

################################################################################


def solution_naive(stones, k):
    """window의 max중 min을 구하는 방식. 로직 자체가 성립하는지 확인 => 로직은 맞으나 timeout"""
    answer = max(stones[:k])
    for i in range(1, len(stones) - k + 1):
        cur_max = max(stones[i:i+k])
        answer = min(cur_max, answer)
    return answer


def solution_old(stones, k):
    """heap과 hashmap을 이용한 구현

    heap과 Counter를 동시에 사용한 이유.
     : size k인 윈도우의 최소값을 빨리 계산하고 싶다.
     : 1. heap을 사용하면 현재 최소값이 윈도우 범위를 벗어났을 때 그 다음 최소값을 바로 찾을 수 있다. heappop()
          하지만, 윈도우를 벗어나는 값을 heap에서 찾아서 제거하는 것은 불가능 (적어도 O(logN)에는 안됨, O(N) 걸림)
       2. Counter를 사용하면 윈도우에 들어오고 나가는 값을 바로 넣고 빼는 것이 가능하다.
          하지만 최소값이 범위를 벗어났을 때 다음 최소값을 찾기 위해서는 다시 O(K)의 탐색이 필요하다.
       => 1, 2에서의 각각의 장점을 결합해서 사용하도록 한다.
          윈도우 범위를 벗어나는 값은 Counter에 반영해서 현재 윈도우내에 존재하는 값이 무엇인지 O(1)에 바로 알 수 있도록 유지한다.
          최소값을 갱신할 때는 heap에서 꺼낸 값이 Counter를 확인해서 윈도우에 존재하는 값이 될 때까지 꺼낸다.

    - 로직
      - 1. size k인 윈도우에 포함된 값들을 hash map 형태의 counter로 저장한다. (매 반복마다 out을 빼고 in_을 넣어서 갱신한다)
      - 2. 빠지는 값이 counter에서 0이면 최소값을 갱신해야한다. 이 때 heap에서 counter에 유효한 값이 나올때까지 값을 추출한다.
           (한번당 O(logN), 최대 원 리스트의 크기반큼 추출될 수 있으므로 총 O(NlogN)의 복잡도가 된다.
        3. 반복마다 각 윈도우의 최소값을 update한다. 최종 구한 최소값을 리턴한다.

    - time complexity: O(NlogN)
    - python에 max heap이 없고 min heap만 있기 때문에, stones의 각 값을 음수로 변환해서 푼다.
    - size k인 윈도우에서 최소값을 구하고, 그 값들 중에서 최대값이 답이 된다. 최종 답에 다시 -1을 곱해 양수로 변환한다.
    """
    stones = [-x for x in stones]
    counter = Counter(stones[:k])
    heap = stones[:k]
    heapify(heap)
    answer = min(stones[:k])
    cur_min = answer
    for i in range(k, len(stones)):
        out = stones[i-k]
        in_ = stones[i]
        counter[out] -= 1
        counter[in_] += 1
        heappush(heap, in_)
        if in_ <= cur_min:
            cur_min = in_
        elif counter[out] == 0 and out == cur_min:
            candi = heappop(heap)
            while counter[candi] == 0:
                candi = heappop(heap)
            cur_min = candi
        answer = max(cur_min, answer)
    return -answer


def solution(stones, k):
    """O(N) 풀이

    min of max 을 찾는 알고리즘은 O(N)이 존재했다. deque(또는 stack)을 이용한 깔끔한 알고리즘. util.tools 로 재활용을 위해 분리함
    """
    return min(iter_window_max(stones, k))


def test():
    assert solution([3, 2, 2, 3, 3], 2) == 2
    assert solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3) == 3


import random
from util import *


def test_compare():
    def gen_prob():
        n = 10
        k = 4
        stones = [random.randint(1, 5) for _ in range(n)]
        return stones, k

    compare_func_results(solution, solution_naive, generate_probs(gen_prob, count=100))


def test_time():
    def gen_prob():
        n = 200000
        k = 100000
        stones = [random.randint(1, 200000000) for _ in range(n)]
        return stones, k

    random.seed(2)
    # 158ms
    timeit_lp(solution, gen_prob(), time_limit=1, funcs=[iter_window_max])
    # 326ms
    # timeit(solution_old, gen_prob(), time_limit=1)
    # 800ms
    # timeit(solution_ext, gen_prob(), time_limit=1)


def test_time_worse_case1():
    def gen_prob():
        n = 200000
        k = 100000
        stones = [random.randint(1, 1) for _ in range(n)]
        return stones, k

    random.seed(2)

    # 130ms
    timeit(solution, gen_prob(), time_limit=1)
    # 194ms
    # timeit(solution_old, gen_prob(), time_limit=1)
    # 5.6
    # timeit(solution_ext, gen_prob(), time_limit=1)


def test_time_worse_case2():
    def gen_prob():
        n = 200000
        k = 100000
        stones = [random.randint(200000000, 200000000) for _ in range(n)]
        return stones, k

    random.seed(2)
    # 131ms
    timeit(solution, gen_prob(), time_limit=1)
    # 106ms
    # timeit(solution_old, gen_prob(), time_limit=1)
    # 109ms
    # timeit(solution_ext, gen_prob(), time_limit=1)


def test_time_worse_case3():
    def gen_prob():
        n = 200000
        k = 100000
        stones = [random.randint(1, 10) for _ in range(n)]
        return stones, k

    random.seed(2)
    # 159ms
    timeit(solution, gen_prob(), time_limit=1)
    # 313ms
    # timeit(solution_old, gen_prob(), time_limit=1)
    # 57ms
    # timeit(solution_ext, gen_prob(), time_limit=1)


################################################################################
# for efficiency comparision
# from https://velog.io/@ansrjsdn/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level3-%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC-%EA%B1%B4%EB%84%88%EA%B8%B0-Python
################################################################################

def calc(stones, k, mid):  # 건널 수 있는지를 체크 하는 것
    now = 0
    for stone in stones:
        if (stone < mid):  # stone - mid 가 0이면 이번 회엔 건널 수 있다는 것임
            now += 1  # 즉 stone < mid 이면 전 사람 건널 때 0이 되어서 못 건너게 됐다는 것.
            # 건너 뛰는 것 값을 + 1 해준다.
        else:  # 연속으로 나온게 아니면 다시 0으로 만들어줌.
            now = 0
        if (now >= k):  # now가 k랑 같거나 커지면 못 건너는 것.
            return False
    return True


def solution_ext(stones, k):
    left = 1  # 최소 1명은 건널 수 있기 때문에
    right = max(stones) + 1  # 최고 값 + 1, 그래야 두개 더해서 // 할 때 내림을 하게 되기 때문에 제대로 됨.
    while (left < right - 1):  # 1차이 날 땐 더이상 가운데가 없기 때문에 left쪽이 답/ right에 넣는 mid는 불가능한 값으로 측정 되어있음
        mid = (left + right) // 2  # 중간의 값 정수가 나오게
        if (calc(stones, k, mid)):  # mid가 가능한지 확인
            left = mid
        else:
            right = mid

    return left

################################################################################
