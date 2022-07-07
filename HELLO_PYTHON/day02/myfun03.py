from random import random


def getHollJJak():
    ret = ""
    rnd = random()
    print(rnd)
    if rnd>0.5:
        ret="홀"
    else:
        ret="짝"
    return ret

com = getHollJJak()
print("com",com)
