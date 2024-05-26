from osupyparser import OsuFile
import time
import random

data = OsuFile(
    "/Users/runxuanliu/Downloads/473491 Usami Hiyori - Tenkiame copy 2/Usami Hiyori - Tenkiame ([R]) [Futsuu].osu").parse_file()
info = data.__dict__
hit_objects = None
timing_points = None
for d, e in info.items():
    if d == 'hit_objects':
        hit_objects = e  # Prints all members of the class.
    if d == 'timing_points':
        timing_points = e

time_stamp = []
for element in hit_objects:
    time_stamp.append(element.start_time)

intervals = []
for n in range(len(time_stamp) - 1):
    intervals.append(time_stamp[n + 1] - time_stamp[n])



start_time = time.time()  # 1119999
interval = 2000


def millisecond_conversion(time_currently):
    return round(time_currently * 1000)


index = 0
while index < len(time_stamp):
    elapsed = time.time() - start_time
    if time_stamp[index] - 50 < millisecond_conversion(elapsed) < time_stamp[index] + 50:
        red_or_blue = random.randint(0, 1)
        # 0 represents red, 1 represents Blue
        if red_or_blue == 0:
            print(f'RED... {time_stamp[index]}')
        else:
            print(f'BLUE... {time_stamp[index]}')
        index += 1

# for element in timing_points:
#     print(element)

# According to TimingPoint
# 1. all circles move in the same velocity 2. beat length is different
