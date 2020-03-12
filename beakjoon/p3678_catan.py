# https://www.acmicpc.net/problem/3678
# success

HEX = 6
NUM_RESOURCE = 5
CENTER_RESOURCE = 0


def flatten_list(xs_list):
    return [x for xs in xs_list for x in xs]


class ResourceCounter:
    def __init__(self, num_resource):
        self.counter = [0] * num_resource

    def select_resource(self, excludes):
        candidates = sorted(enumerate(self.counter), key=lambda x: (x[1], x[0]))
        for resource, _ in candidates:
            if resource not in excludes:
                return resource

    def increase(self, resource):
        self.counter[resource] += 1

    def __str__(self):
        return str(self.counter)
        # return str(list(enumerate(self.counter)))


def init_katan_table(num_layers):
    counter = ResourceCounter(NUM_RESOURCE)
    layers = [[CENTER_RESOURCE]]
    counter.increase(CENTER_RESOURCE)

    for layer_idx in range(1, num_layers + 1):
        pre_layer = layers[layer_idx - 1]
        line_len = layer_idx
        layer = [None] * (line_len * HEX)
        pos_in_layer = 0
        pos_in_pre_layer = 0
        for line_idx in range(HEX):
            for idx in range(line_len):
                excludes = []
                if pos_in_layer > 0:
                    excludes.append(layer[pos_in_layer - 1])
                    excludes.append(pre_layer[pos_in_pre_layer - 1])
                else:
                    excludes.append(pre_layer[-1])

                if idx < line_len - 1:
                    excludes.append(pre_layer[pos_in_pre_layer])
                    pos_in_pre_layer += 1
                elif line_idx == HEX - 1:
                    excludes.append(layer[0])

                selected_resource = counter.select_resource(excludes)
                # print(f"{layer_idx:02d} - {pos_in_layer:03d} : {selected_resource} selected, counter: {counter}, exclude: {excludes}")
                layer[pos_in_layer] = selected_resource
                counter.increase(selected_resource)

                pos_in_layer += 1
        layers.append(layer)

    return flatten_list(layers)


def calc_num_layers(pos):
    cur_pos = 1
    num_layers = 0
    while cur_pos < pos:
        num_layers += 1
        cur_pos += num_layers * HEX
    return num_layers


def katan(pos_list):
    max_pos = max(pos_list)
    num_layers = calc_num_layers(max_pos)
    num_layers = 80
    table = init_katan_table(num_layers)
    return [table[pos - 1] + 1 for pos in pos_list]


def read_input_lines_with_count_header():
    import sys
    N = int(sys.stdin.readline())
    inputs = [line.rstrip() for line in sys.stdin.readlines()]
    return inputs


def main():
    res = katan([int(x) for x in read_input_lines_with_count_header()])
    for x in res:
        print(x)
    # print("\n".join(str(x) for x in res))


if __name__ == "__main__":
    main()
