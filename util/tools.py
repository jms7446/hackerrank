

def str_findall(ptn, s):
    idx = s.find(ptn)
    while idx != -1:
        yield idx
        idx = s.find(ptn, idx + 1)


def iter_pair_in_order(xs, ys):
    for x in xs:
        for y in ys:
            if x < y:
                yield x, y

