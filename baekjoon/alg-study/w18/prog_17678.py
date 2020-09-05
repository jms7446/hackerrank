# 셔틀버스



def time_to_int(t):
    h, m = [int(x) for x in t.split(':')]
    return h * 60 + m


def int_to_time(i):
    h, m = divmod(i, 60)
    return f'{h:02d}:{m:02d}'


def solution(n, t, m, timetable):
    line_up = sorted([time_to_int(t) for t in timetable])
    start_bus = time_to_int('09:00')
    last_bus = start_bus + t * (n - 1)
    if line_up[-1] <= last_bus:
        line_up.append(last_bus + 1)     # a late crew, this crew can never take a bus, and remain in the line_up

    next_crew = 0
    seat_left = 0
    for cur_bus in range(start_bus, last_bus + 1, t):
        seat_left = m
        while seat_left > 0 and line_up[next_crew] <= cur_bus:
            seat_left -= 1
            next_crew += 1

    # if last bus has underoccupied seat, just take last bus.
    # else 1 minute earlier than the last one who take the last bus.
    if seat_left > 0:
        return int_to_time(last_bus)
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
