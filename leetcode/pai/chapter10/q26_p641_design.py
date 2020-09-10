from typing import List, Set, Dict
import pytest


# 72ms, 13.9MB (85%, 97%)
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.queue = [0] * k
        self.head = 0
        self.tail = 0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.head = (self.head - 1) % self.k
        self.count += 1
        self.queue[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % self.k
        self.count -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1) % self.k]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.count == self.k


def test():
    obj = MyCircularDeque(3)
    assert obj.insertLast(1)
    assert obj.insertLast(2)
    assert obj.insertFront(3)
    assert not obj.insertFront(4)
    assert obj.getRear() == 2
    assert obj.isFull()
    assert obj.deleteLast()
    assert obj.insertFront(4)
    assert obj.getFront() == 4

