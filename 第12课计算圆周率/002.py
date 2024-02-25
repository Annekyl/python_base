from math import fabs

pai = 1
up = 1
down = 3
n = 1
a = 1
while fabs(a) >= 1e-6:
    a = (up / down) * (-1) ** n
    pai += a
    n += 1
    down += 2

print("Π的值为：{:.10f}".format(pai * 4))

total, s, n, t = 0, 1, 1, 1
while fabs(t) >= 1e-6:
    total += t
    n += 2
    s = -s
    t = s / n
k = total * 4
print("Π的值为{:.10f}".format(k))
