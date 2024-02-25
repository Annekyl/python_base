import random

total = 1000000
cir = 0
for i in range(total):
    x = random.random()
    y = random.random()
    long = (x ** 2 + y ** 2) ** 0.5
    if long <= 1:
        cir += 1
pai = (cir / total) * 4
print(f"Π的值为：{pai}")
