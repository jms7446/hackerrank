import sys
import random
import string
import subprocess


def solve(N, K, words):
    pass

    return -1


def main():
    stdin = sys.stdin
    N, K = [int(x) for x in stdin.readline().split()]
    words = [stdin.readline().strip() for _ in range(N)]
    print(solve(N, K, words))


def make_prob(N, M, K):
    def make_word_core():
        return "".join(random.choices(string.ascii_lowercase, k=random.randint(0, M)))

    words = list(set(["anta" + make_word_core() + "tica" for _ in range(N)]))
    N = len(words)
    words_str = "\n".join(words)
    prob_str = f"{N} {K}\n{words_str}"
    return prob_str


def main2():
    T = 100
    # cmds = ["/Users/msjung/dev/go/bin/p1062", "/Users/msjung/dev/go/src/ccwithgo/baejoon/silver/p1062/a.out"]
    # cmds = ["/Users/msjung/dev/go/bin/p1062", "/usr/bin/wc"]
    cmds = ["/Users/msjung/dev/go/bin/p1062", "/Users/msjung/dev/go/src/ccwithgo/baejoon/silver/p1062/a.out"]
    for i in range(T):
        N = random.randint(1, 10)
        K = random.randint(0, 10)
        M = random.randint(0, 4)
        # N, K, M = 40, 20, 7
        prob_str = make_prob(N, M, K)

        outs = []
        for cmd in cmds:
            p = subprocess.Popen([cmd], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            p.stdin.write(prob_str.encode())
            p.stdin.close()
            out = p.stdout.read()
            outs.append(out)

        if i % 100 == 0:
            print()
        print(".", end="")

        if outs[0] != outs[1]:
            print()
            print(outs, file=sys.stderr)
            print(prob_str, file=sys.stderr)
            break


if __name__ == "__main__":
    main2()
