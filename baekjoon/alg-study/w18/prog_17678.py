# 셔틀버스


def time_to_int(t):
    h, m = [int(x) for x in t.split(':')]
    return h * 60 + m


def int_to_time(i):
    h, m = divmod(i, 60)
    return f'{h:02d}:{m:02d}'


def solution(n, t, m, timetable):
    time_table = sorted([time_to_int(t) for t in timetable])
    start_bus = time_to_int('09:00')
    last_bus = start_bus + t * (n - 1)

    next_idx = 0
    left = m
    cur_bus = start_bus
    for i in range(n):
        cur_bus = start_bus + t * i
        left = m
        while left > 0 and next_idx < len(time_table) and time_table[next_idx] <= cur_bus:
            left -= 1
            next_idx += 1

    if next_idx == 0 or left > 0 or cur_bus < last_bus:
        return int_to_time(last_bus)
    return int_to_time(time_table[next_idx - 1] - 1)


def test_main():
    assert solution(2, 10, 2, ["09:10", "09:09", "08:00"]) == '09:09'
    assert solution(1, 1, 5, ['08:00', '08:01', '08:02', '08:03']) == '09:00'
    assert solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]) == '00:00'
    assert solution(3, 21, 7, ['17:38', '19:41', '07:42']) == '09:42'


def test_time_to_int():
    assert time_to_int('08:00') == 8 * 60 + 0


def test_int_to_time():
    assert 8 * 60 + 0 == time_to_int('08:00')
