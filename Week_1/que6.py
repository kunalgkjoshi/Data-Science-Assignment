import math


def getCor(s):
    first = s.split('x')
    a = float(first[0])

    second = first[1].split('y')
    b = float(second[0])
    c = float(second[1])

    return (a, b, c)


def getSide(t, p):
    cal = (t[0] * p[0]) + (t[1] * p[1]) + (t[2])

    if cal > 0:
        return 1
    elif cal < 0:
        return -1
    elif cal == 0:
        return 0
    return -2


def getAns(red, blue, line):
    sign_red = getSide(getCor(line), red[0])
    sign_blue = getSide(getCor(line), blue[0])

    for j in range(len(red)):
        if sign_red != getSide(getCor(line), red[j]):
            return 'no'

    for j in range(len(blue)):

        if sign_blue != getSide(getCor(line), blue[j]):
            return 'no'
    return 'Yes'


Red = [(1, 1), (2, 1), (4, 2), (2, 4), (-1, 4)]
Blue = [(-2, -1), (-1, -2), (-3, -2), (-3, -1), (1, -3)]
Lines = ["1x+1y+0", "1x-1y+0", "1x+0y-3", "0x+1y-0.5"]

for i in Lines:
    ans = getAns(Red, Blue, i)
    print(ans)