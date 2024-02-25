# 任务1：求年龄
def age(n):
    if n == 5:
        return 10
    else:
        return age(n + 1) + 2


t = age(1)
print(f"第1个人的年龄为：{t}")


# 任务2：猴子吃桃
def num(n):
    if n == 10:
        return 1
    else:
        return (num(n + 1) + 1) * 2


a = num(1)
print(a)


# 任务3：求阶乘
def jc(i):
    if i == 1:
        return 1
    else:
        return jc(i - 1) * i


b = jc(5)
print(b)


# 任务4：斐波那契数列
def fbnq(i):
    if i == 1:
        return 1
    if i == 2:
        return 1
    else:
        return fbnq(i - 2) + fbnq(i - 1)


c = fbnq(15)
print(c)


# 任务5：求值并保留小数点后四位
def add(i):
    if i == 1:
        return 1
    else:
        return add(i - 2) + 1 / i


d = add(11)
print("{:.4f}".format(d))


# 任务6：正负整数相加
def jiajian1(i):
    if i == 1:
        return 1
    else:
        return jiajian1(i - 1) + (i * 2 - 1) * (-1) ** (i - 1)


print(jiajian1(8))


# 任务7：正负分数相加并保留四位小数
def jiajian2(i):
    if i == 1:
        return 1
    else:
        return jiajian2(i - 1) + (-1) ** (i - 1) * (1 / (i * 2 - 1))


print("{:.4f}".format(jiajian2(7)))
