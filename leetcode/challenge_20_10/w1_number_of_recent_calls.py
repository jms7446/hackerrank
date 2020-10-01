from collections import deque


class RecentCounter:
    def __init__(self):
        self.calls = deque()

    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls and self.calls[0] < t - 3000:
            self.calls.popleft()
        return len(self.calls)
