import time


h = 0
min = 0
sec = 0
while h <= 2:
    while min < 60:
        while sec < 60:
            print(h, min, sec)
            sec += 1
            time.sleep(.1)
        min += 1
        sec = 0
    h += 1
    min = 0
    sec = 0