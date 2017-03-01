import time

debugTickrate = 1
tickrateGlobal = 0

def addTick(tickrate):
    if tickrate == 3:
        tickrate = 0
    tickrate += 1
    if debugTickrate == 1:
        print("tick"+" "+str(tickrate))
    time.sleep(0.25)
    addTick(tickrate)


def globalTiming(tick):
    tick += 1
    print(tick)
    time.sleep(0.25)
    globalTiming(tick)


def startTiming():
    addTick(0)





