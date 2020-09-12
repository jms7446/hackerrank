
class BinaryHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def push(self, k):
        self.items.append(k)
        self._percolate_up()

    def pop(self):
        if not self:
            return None

        item = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return item

    def _percolate_up(self):
        items = self.items
        i = len(self)
        while i > 1:    # while i is not root
            parent = i // 2
            if items[i] >= items[parent]:
                break
            items[i], items[parent] = items[parent], items[i]
            i = parent

    def _percolate_down(self, idx):
        items = self.items
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and items[left] < items[smallest]:
            smallest = left
        if right <= len(self) and items[right] < items[smallest]:
            smallest = right
        if smallest != idx:
            items[smallest], items[idx] = items[idx], items[smallest]
            self._percolate_down(smallest)


def test():
    heap = BinaryHeap()
    heap.push(1)
    heap.push(3)
    heap.push(2)
    assert heap.pop() == 1
    assert heap.pop() == 2
    assert heap.pop() == 3
    assert not heap

