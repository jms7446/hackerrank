

def liar(checker_list, party_list):
    checker_set = set(checker_list)
    party_list = [set(party) for party in party_list]
    while True:
        pre_num_checker = len(checker_set)
        for party in party_list:
            if party.intersection(checker_set):
                checker_set = checker_set.union(party)
        if len(checker_set) == pre_num_checker:
            break
    return sum(party.isdisjoint(checker_set) for party in party_list)


def main():
    import sys
    stdin = sys.stdin
    _ = stdin.readline()
    checker_list = [int(x) for x in stdin.readline().split()[1:]]
    party_list = [[int(x) for x in line.split()[1:]] for line in stdin.readlines()]
    print(liar(checker_list, party_list))


if __name__ == "__main__":
    main()
