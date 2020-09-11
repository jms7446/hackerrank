

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return 'N({self.value})'


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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



















