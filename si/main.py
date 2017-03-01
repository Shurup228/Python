import random, pprint
import time
from si import functions

running = 1
start = functions.array_gen()
pos = 3
while running == 1:
    start[4] = start[3]
    start[3] = start[2]
    start[2] = start[1]
    start[1] = start[0]
    start[0] = functions.array_gen()[0]
    start[4][pos] = "&"
    move = random.randrange(0, 2)
    if pos == 0:
        pos += 1
    elif pos == len(start[4]) - 1:
        pos -= 1
    elif move == 1:
        pos += 1
    else:
        pos -= 1
    for elem in start:
        print(elem, "\n")
    print("-----------------------------------")
    time.sleep(1)
    if start[3][pos] == "*":
        pass










