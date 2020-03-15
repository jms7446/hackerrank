

def gen_prob(N, M):
    import random
    random.seed(3)
    people = [list(sorted([random.randint(0, N - 1) for _ in range(2)])) for _ in range(M)]
    return N, people

