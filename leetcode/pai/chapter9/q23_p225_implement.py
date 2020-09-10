from typing import List, Set, Dict
import pytest
from collections import deque


# naive O(n) implementation
# 28ms, 14MB (80%, 27%)
class MyStackNaive:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.aux_queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        last = self.queue.popleft()
        while self.queue:
            self.aux_queue.append(last)
            last = self.queue.popleft()
        self.queue, self.aux_queue = self.aux_queue, self.queue
        return last

    def top(self) -> int:
        """
        Get the top element.
        """
        last = self.pop()
        self.push(last)
        return last

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue


# one queue.
# top is O(1)!
class MyStackRefer:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


MyStack = MyStackRefer


@pytest.mark.parametrize(['in_', 'out'], [
    (1, 1),
])
def test1(in_, out):
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    assert obj.top() == 4
    assert obj.pop() == 4
    assert not obj.empty()
    assert obj.pop() == 3
    assert obj.pop() == 2
