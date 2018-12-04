import re
from collections import defaultdict

day = 4

def algo1(data):
    guards = defaultdict(lambda: defaultdict(list))
    data.sort()

    current_guard = -1
    current_sleep_time = 0

    for entry in data:
        if "begins shift" in entry:
            m = re.search(r' Guard #(?P<guard>\d+) ', entry)  # Don't care when they started, just who in the stream
            current_guard = int(m['guard'])
        elif "falls asleep" in entry:
            m = re.search(r'\[1518-(?P<date>\d\d-\d\d) \d\d:(?P<minute>\d\d)\]', entry)
            current_sleep_time = int(m['minute'])
        elif "wakes up" in entry:
            m = re.search(r'\[1518-(?P<date>\d\d-\d\d) \d\d:(?P<minute>\d\d)\]', entry)
            guards[current_guard][m['date']].append((current_sleep_time, int(m['minute'])))

    sleep_totals = defaultdict(int)
    sleep_minutes = defaultdict(list)
    for gid, gdata in guards.items():
        for day in gdata.values():
            for nap in day:
                sleep_totals[gid] += (nap[1] - nap[0])
                sleep_minutes[gid].extend(range(nap[0], nap[1]))

    sleepiest_guard = max(sleep_totals.keys(), key=(lambda gid: sleep_totals[gid]))
    sleepiest_minute = max(set(sleep_minutes[sleepiest_guard]), key=sleep_minutes[sleepiest_guard].count)

    return sleepiest_guard * sleepiest_minute



def algo2(data):
    guards = defaultdict(lambda: defaultdict(list))
    data.sort()

    current_guard = -1
    current_sleep_time = 0

    for entry in data:
        if "begins shift" in entry:
            m = re.search(r' Guard #(?P<guard>\d+) ', entry)  # Don't care when they started, just who in the stream
            current_guard = int(m['guard'])
        elif "falls asleep" in entry:
            m = re.search(r'\[1518-(?P<date>\d\d-\d\d) \d\d:(?P<minute>\d\d)\]', entry)
            current_sleep_time = int(m['minute'])
        elif "wakes up" in entry:
            m = re.search(r'\[1518-(?P<date>\d\d-\d\d) \d\d:(?P<minute>\d\d)\]', entry)
            guards[current_guard][m['date']].append((current_sleep_time, int(m['minute'])))

    sleep_minutes = defaultdict(list)
    sleep_minutes_frequency = {}
    for gid, gdata in guards.items():
        for day in gdata.values():
            for nap in day:
                sleep_minutes[gid].extend(range(nap[0], nap[1]))

    for gid, gdata in guards.items():
        sleepiest_minute = max(set(sleep_minutes[gid]), key=sleep_minutes[gid].count)
        freq = sleep_minutes[gid].count(sleepiest_minute)
        sleep_minutes_frequency[gid] = {
            'minute': sleepiest_minute,
            'freq': freq,
        }

    sleepiest_guard = max(sleep_minutes_frequency.keys(), key=(lambda gid: sleep_minutes_frequency[gid]['freq']))
    return sleepiest_guard * sleep_minutes_frequency[sleepiest_guard]['minute']


if __name__ == "__main__":
    test1_input = [
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:55] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:40] falls asleep",
        "[1518-11-02 00:50] wakes up",
        "[1518-11-03 00:05] Guard #10 begins shift",
        "[1518-11-03 00:24] falls asleep",
        "[1518-11-03 00:29] wakes up",
        "[1518-11-04 00:02] Guard #99 begins shift",
        "[1518-11-04 00:36] falls asleep",
        "[1518-11-04 00:46] wakes up",
        "[1518-11-05 00:03] Guard #99 begins shift",
        "[1518-11-05 00:45] falls asleep",
        "[1518-11-05 00:55] wakes up",
    ]
    test1_answer = 240
    if algo1(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = [
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:55] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:40] falls asleep",
        "[1518-11-02 00:50] wakes up",
        "[1518-11-03 00:05] Guard #10 begins shift",
        "[1518-11-03 00:24] falls asleep",
        "[1518-11-03 00:29] wakes up",
        "[1518-11-04 00:02] Guard #99 begins shift",
        "[1518-11-04 00:36] falls asleep",
        "[1518-11-04 00:46] wakes up",
        "[1518-11-05 00:03] Guard #99 begins shift",
        "[1518-11-05 00:45] falls asleep",
        "[1518-11-05 00:55] wakes up",
    ]
    test2_answer = 4455
    if algo2(test2_input) == test2_answer:
        print("Second Question Test Passed")
    else:
        print("Second Question Test FAILED")

    with open(f"{day}.txt", encoding='utf-8', errors='ignore') as f:
        input_data = [line.rstrip() for line in f]

    print("Answer 1: ", algo1(input_data))
    print("Answer 2: ", algo2(input_data))
