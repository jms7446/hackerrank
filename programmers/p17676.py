# 추석 트래픽
import datetime
from dateutil import parser


def parse_log_line(line):
    dt_str, et_str = line.rsplit(' ', 1)
    end = parser.parse(dt_str)
    elapse_time = datetime.timedelta(seconds=float(et_str[:-1]))
    begin = end - elapse_time + datetime.timedelta(milliseconds=1)
    return begin, end


def max_overlap_count(begin_ends, gap):
    begins, ends = zip(*begin_ends)

    END, BEGIN = range(2)       # BEGIN must be larger than END for sorting
    begins = [(t, BEGIN) for t in begins]
    ends = [(t + gap, END) for t in sorted(ends)]

    max_count, count = 0, 0
    for _, pos in sorted(begins + ends):
        if pos == BEGIN:
            count += 1
        else:
            count -= 1
        max_count = max(max_count, count)
    return max_count


def solution(lines):
    begin_ends = [parse_log_line(line) for line in lines]
    return max_overlap_count(begin_ends, datetime.timedelta(seconds=1))


import pytest


@pytest.mark.parametrize(['in_', 'out'], [
    (["2016-09-15 00:00:00.000 3s"], 1),
    (["2016-09-15 23:59:59.999 0.001s"], 1),
    (["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"], 1),
    (["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"], 2),
    (["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"], 7),
    (["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"], 1),
])
def test1(in_, out):
    assert solution(in_) == out


def test_max_overlap_count():
    assert max_overlap_count([(0, 1), (1, 2)], 0) == 1
    assert max_overlap_count([(0, 1), (1, 2)], 1) == 2