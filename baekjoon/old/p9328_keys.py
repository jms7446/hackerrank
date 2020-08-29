import sys


class BuildingSeeker:
    NEIGHBOR = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    def __init__(self, building_map, keys):
        self.building_map = building_map
        self.keys = keys
        self.height = len(building_map)
        self.width = len(building_map[0])

        self.visit_flags = [[False] * self.width for _ in range(self.height)]
        self.doc_count = 0
        self.blocked_map = {}
        self.visit_stack = []

    def seek(self):
        self.visit_stack.append((0, 0))
        while self.visit_stack:
            r, c = self.visit_stack.pop()
            self._visit(r, c)
        return self.doc_count

    def _visit(self, r, c):
        if self._is_invalid(r, c):
            return
        self.visit_flags[r][c] = True

        condition = self.building_map[r][c]
        if condition == ".":
            pass
        elif condition == "*":
            return
        elif condition == "$":
            self.doc_count += 1
        elif condition.isupper():
            key = condition.lower()
            if key not in self.keys:
                self.blocked_map.setdefault(key, []).append((r, c))
                self.visit_flags[r][c] = False
                return
        elif condition.islower():
            key = condition
            self.keys.add(key)
            if key in self.blocked_map:
                for blocked_r, blocked_c in self.blocked_map[key]:
                    self.visit_stack.append((blocked_r, blocked_c))

        for dr, dc in self.NEIGHBOR:
            nr, nc = r + dr, c + dc
            if not self._is_invalid(nr, nc):
                self.visit_stack.append((nr, nc))

    def _is_invalid(self, r, c):
        if not (0 <= c < self.width and 0 <= r < self.height):
            return True
        if self.visit_flags[r][c]:
            return True
        return False


def solution(building, keys):
    seeker = BuildingSeeker(building, keys)
    return seeker.seek()


def main():
    stdin = sys.stdin
    N = int(stdin.readline())
    for _ in range(N):
        height, width = [int(x) for x in stdin.readline().split()]
        building = [stdin.readline().strip() for _ in range(height)]
        building = ["." * (width + 2)] + ["." + row + "." for row in building] + ["." * (width + 2)]
        key_str = stdin.readline().strip()
        if key_str == "0":
            keys = set()
        else:
            keys = set(key_str)
        print(BuildingSeeker(building, keys).seek())


if __name__ == "__main__":
    main()
