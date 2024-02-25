from random import random

total = 1000000
cir = 0
for i in range(total):
    x = random()
    y = random()
    long = (x ** 2 + y ** 2) * 0.5
    if long <= 1:
        cir += 1
pai = (cir / total) * 4
print(f"Π的值为：{pai}")

NUMS = 1000 * 1000
hits = 0.0
for i in range(NUMS):
    a, b = random(), random()
    dist = pow(a ** 2 + b ** 2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits / NUMS)
print(f"圆周率为{pi}")
