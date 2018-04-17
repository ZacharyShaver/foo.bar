from math import log
def answer(n):
    f = int(n)
    opps = 0
    while f != 1:
        x = bin(int(f))
        opps += 1
        if x[-1:] == '0':
            f /= 2
        elif x[-2:] == '01' or f == 3:
            f -= 1
        else:
            f += 1
    return opps

print(answer('3421243'))
