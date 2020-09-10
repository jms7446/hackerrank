from typing import List, Set, Dict
from util import *


# 72ms, 14MB (80%, 84%)
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        self.queue = [0] * k
        self.count = 0
        self.head = self.tail = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1) % self.k]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.k


def test():
    obj = MyCircularQueue(3)
    assert obj.enQueue(1)
    assert obj.enQueue(2)
    assert obj.enQueue(3)
    assert not obj.enQueue(4)
    assert obj.Rear() == 3
    assert obj.isFull()
    assert obj.deQueue()
    assert obj.enQueue(4)
    assert obj.Rear() == 4

    assert obj.Front() == 2
    assert not obj.isEmpty()

