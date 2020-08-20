# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, xs):
        if not xs:
            return None
        head = cls(xs[0])
        cur = head
        for x in xs[1:]:
            cur.next = cls(x)
            cur = cur.next
        return head

    def to_list(self):
        xs = [self.val]
        cur = self.next
        while cur:
            xs.append(cur.val)
            cur = cur.next
        return xs


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        length = self.calc_length(head)
        middle_idx = length - length // 2
        latter_half = self.split_list(head, middle_idx)
        latter_half = self.reverse(latter_half)
        self.weave_list(head, latter_half)

    @staticmethod
    def weave_list(l1, l2):
        """merge two list, assume that two list has the same length or len(l1) + 1 == len(l2)"""
        while l2:
            l1.next, l2.next, l1, l2 = l2, l1.next, l1.next, l2.next

    @staticmethod
    def calc_length(xs):
        count = 0
        while xs:
            count += 1
            xs = xs.next
        return count

    @staticmethod
    def split_list(head, idx):
        for _ in range(idx - 1):
            head = head.next
        new_head = head.next
        head.next = None
        return new_head

    @staticmethod
    def reverse(xs):
        if xs is None:
            return None
        (pre, cur) = (xs, xs.next)
        while cur:
            (cur.next, pre, cur) = (pre, cur, cur.next)
        xs.next = None
        return pre


def test1():
    xs = ListNode.from_list([1, 2, 3, 4])
    Solution().reorderList(xs)
    assert xs.to_list() == [1, 4, 2, 3]

    xs = ListNode.from_list([])
    Solution().reorderList(xs)
    assert xs is None

    xs = ListNode.from_list([1])
    Solution().reorderList(xs)
    assert xs.to_list() == [1]
