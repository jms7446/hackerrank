from typing import List, Set, Dict


# 32ms, 13.9MB (57%, 40%)
class MyQueueFirst:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.out_stack:
            self._prepare()
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.out_stack:
            self._prepare()
        return self.out_stack[-1]

    def _prepare(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.out_stack and not self.in_stack


MyQueue = MyQueueFirst


def test1():
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    assert obj.peek() == 1
    assert obj.pop() == 1
    assert not obj.empty()
