

def read_input_lines_with_count_header():
    import sys
    N = int(sys.stdin.readline())
    inputs = [line.rstrip() for line in sys.stdin.readlines()]
    assert len(inputs) == N
    return inputs
