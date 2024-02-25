# 求斐波那契数列前n个数字之和
def add(i):
    if i == 1:
        return 1
    if i == 2:
        return 1
    else:
        return add(i - 1) + add(i - 2)


num = int(input("请输入你要求和到第几位"))
total = 0
for a in range(1, num + 1):
    total += add(a)
print(f"结果为：{total}")
