import sys


class Energy:
    def __init__(self, L):
        self.L = L
        self.amount = 0

    def inc(self):
        if self.amount < self.L:
            self.amount += 1

    def down(self):
        self.amount = -self.L

    def reset(self):
        self.amount = 0

    def is_full(self):
        return self.amount == self.L

    def is_ok(self):
        return self.amount >= 0


def is_valid_road(road, L):
    energy = Energy(L)
    energy.inc()
    for prev, cur in zip(road, road[1:]):
        diff = cur - prev
        if diff == 0:
            pass
        elif diff == 1 and energy.is_full():
            energy.reset()
        elif diff == -1 and energy.is_ok():
            energy.down()
        else:
            return False
        energy.inc()
    return energy.is_ok()


def decline(road_list, L):
    return sum(is_valid_road(road, L) for road in road_list)


def main():
    stdin = sys.stdin
    L = int(stdin.readline().split()[1])
    horizontal_roads = [tuple([int(x) for x in line.split()]) for line in stdin.readlines() if line.strip()]
    vertical_roads = list(zip(*horizontal_roads))
    road_list = horizontal_roads + vertical_roads
    print(decline(road_list, L))


if __name__ == "__main__":
    main()
