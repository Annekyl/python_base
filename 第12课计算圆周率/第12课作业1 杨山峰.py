from math import fabs
import random

while 1:
    sel = int(input("请选择计算Π的方法 1.BBP公式 2.公式法2 3.概率法"))

    if sel == 1:
        pai = 0
        for i in range(100):
            pai += 1 / pow(16, i) * ((4 / (8 * i + 1)) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
        print("Π的值为：{:.10f}".format(pai))

    if sel == 2:
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

    if sel == 3:
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

    sel2 = input("还要继续吗 1.继续 2.结束")
    if sel2 == "1":
        continue
    if sel2 == "2":
        break
