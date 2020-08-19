

def str_findall(c, s):
    idx = s.find(c)
    while idx != -1:
        yield idx
        idx = s.find(c, idx + 1)
