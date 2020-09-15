from collections import deque


################################################################################
# ListNode
################################################################################

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        l = list_node_to_list(self)
        return str(l)


def list_node_to_list(list_node: ListNode):
    ret = []
    while list_node:
        ret.append(list_node.val)
        list_node = list_node.next
    return ret


def list_to_list_node(xs):
    if not xs:
        return None
    head = ListNode(xs[0])
    node = head
    for x in xs[1:]:
        node.next = ListNode(x)
        node = node.next
    return head


def test_list_node_convert():
    assert list_node_to_list(list_to_list_node([1, 2, 3])) == [1, 2, 3]


l2ln = list_to_list_node
ln2l = list_node_to_list


################################################################################
# Tree
################################################################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        left = self.left.val if self.left else '_'
        right = self.right.val if self.right else '_'
        return f'TN({self.val}, {left}, {right})'


def list_to_btree(xs):
    if not xs:
        return None
    xs = list(reversed(xs))
    root = TreeNode(xs.pop())
    queue = deque([root])
    while queue and xs:
        node = queue.popleft()
        if node:
            left = xs.pop() if xs else None
            if left is not None:
                left = TreeNode(left)
            node.left = left
            queue.append(node.left)

            right = xs.pop() if xs else None
            if right is not None:
                right = TreeNode(right)
            node.right = right
            queue.append(node.right)
    return root


def btree_to_list(root):
    xs = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            xs.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            xs.append(None)
    while xs and xs[-1] is None:
        xs.pop()
    return xs


def test_TreeNode():
    xs = [3, 9, 2, None, None, 1, 7]
    assert btree_to_list(list_to_btree(xs)) == xs
