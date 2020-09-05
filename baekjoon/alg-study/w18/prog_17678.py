# 셔틀버스



def time_to_int(t):
    h, m = [int(x) for x in t.split(':')]
    return h * 60 + m


def int_to_time(i):
    h, m = divmod(i, 60)
    return f'{h:02d}:{m:02d}'


def solution(n, t, m, timetable):
    start_bus = time_to_int('09:00')
    line_up = sorted([time_to_int(t) for t in timetable])
    line_up.append(time_to_int('23:59'))    # this late crew can never take a bus, and remains in the line_up.

    next_crew = 0
    seat_left = 0
    cur_bus = start_bus
    for i in range(n):
        cur_bus = start_bus + t * i
        seat_left = m
        while seat_left > 0 and line_up[next_crew] <= cur_bus:
            seat_left -= 1
            next_crew += 1

    # if last bus has underoccupied seat, just take last bus.
    # else 1 minute earlier than the last one who take the last bus.
    if seat_left > 0:
        return int_to_time(cur_bus)
    else:
        return int_to_time(line_up[next_crew - 1] - 1)


def test_main():
    assert solution(2, 10, 2, ["09:10", "09:09", "08:00"]) == '09:09'
    assert solution(1, 1, 5, ['08:00', '08:01', '08:02', '08:03']) == '09:00'
    assert solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]) == '00:00'
    assert solution(3, 21, 7, ['17:38', '19:41', '07:42']) == '09:42'


def test_time_to_int():
    assert time_to_int('08:00') == 8 * 60 + 0


def test_int_to_time():
    assert 8 * 60 + 0 == time_to_int('08:00')
