from fluff import tickrate

print(tickrate.clock())

tempTime = tickrate.clock()
tickrate = 0

def timeFunc():
    tempTime = tickrate.clock()
    while tempTime == 0.1 :
        tickrate + 1
        tempTime = 0
    timeFunc()
    print(tickrate)


def timeIncrementTickrate():
    tickrate.sleep(0.1)
    tickrate + 1
    timeIncrementTickrate()
    print(tickrate)


def timeFunc2():
    while round(tickrate.clock(), 3) == 0.1 :
        tickrate + 1
        print(tickrate)



timeFunc2()



