def fun(x, a, b):
    if a == -1:
        v = float(x[b]) / (b + 1)
        for i in range(a + 1, b + 1):
            x[i] = int(v)
    elif b == -1:
        v = float(x[a]) / (len(x) - a)
        for i in range(a, len(x)):
            x[i] = int(v)
    else:
        v = (float(x[a]) + float(x[b])) / (b - a + 1)
        for i in range(a, b + 1):
            x[i] = int(v)
    return x


def replace(text):
    x = text.replace(" ", "").split(",")
    y = [i for i, v in enumerate(x) if v != '_']

    if y[0] != 0:
        y = [-1] + y

    if y[-1] != len(x) - 1:
        y = y + [-1]

    for (a, b) in zip(y[:-1], y[1:]):
        fun(x, a, b)
    return x


tests = [
    "_,_,_,24",
    "40,_,_,_,60",
    "80,_,_,_,_",
    "_,_,30,_,_,_,50,_,_"]

for i in tests:
    print(replace(i))