
def quick_sorted(A):
    def _partition(lo, hi):
        left = lo
        pivot = hi
        for right in range(lo, hi):
            if A[right] < A[pivot]:
                A[left], A[right] = A[right], A[left]
                left += 1
        pivot = left
        A[pivot], A[hi] = A[hi], A[pivot]
        return pivot

    def _sort(lo, hi):
        if lo < hi:
            pivot = _partition(lo, hi)
            _sort(lo, pivot - 1)
            _sort(pivot + 1, hi)

    A = A.copy()
    _sort(0, len(A) - 1)
    return A
