from leetcode.data_structure import *


# failed, but I don't know why.
class CodecFirst:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
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
        return str(xs).replace('None', 'null')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.replace('null', 'None')
        xs = eval(data)
        if not xs:
            return None
        xs = list(reversed(xs))
        root = TreeNode(xs.pop())
        queue = deque([root])
        while queue and xs:
            node = queue.popleft()
            if node:
                node.left = TreeNode(xs.pop()) if xs else None
                node.right = TreeNode(xs.pop()) if xs else None
                queue.append(node.left)
                queue.append(node.right)
        return root


Codec = CodecFirst


def test1():
    codec = Codec()
    root = list_to_btree([5,2,3,None,None,2,4,None,None,None,None,3,1])
    serialized = codec.serialize(root)
    recover = codec.deserialize(serialized)
    assert btree_to_list(root) == btree_to_list(recover)


def test2():
    codec = Codec()
    root = list_to_btree([])
    serialized = codec.serialize(root)
    recover = codec.deserialize(serialized)
    assert btree_to_list(root) == btree_to_list(recover)


def test3():
    codec = Codec()
    root = list_to_btree([1,2,3,None,None,4,5])
    serialized = codec.serialize(root)
    recover = codec.deserialize(serialized)
    assert btree_to_list(root) == btree_to_list(recover)
