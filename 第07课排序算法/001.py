# 选择排序
ls = [12, 40, 10, 9, 8, -1, 21, -6]
ls2 = []
print(ls)
# 普通方法
n = 0  # 交换次数
for j in range(len(ls) - 1):
    for i in range(len(ls) - 1 - j):
        if ls[j] > ls[i + j + 1]:
            ls[j], ls[i + j + 1] = ls[i + j + 1], ls[j]
            n += 1
            '''
            tmp = ls[0]
            ls[0] = ls[i + 1]
            ls[i + 1] = tmp
            '''
print(ls)
print(f"普通方法交换次数为{n}次")

# 改进方法
ls = [12, 40, 10, 9, 8, -1, 21, -6]
n = 0
for j in range(len(ls) - 1):
    f = j
    for i in range(len(ls) - 1 - j):
        if ls[f] > ls[j + i + 1]:
            f = j + i + 1
    ls[j], ls[f] = ls[f], ls[j]
    n += 1
print(ls)
print(f"优化方法交换次数为{n}次")

# 最优方法
ls = [12, 40, 10, 9, 8, -1, 21, -6]
n = 0
for j in range(len(ls) - 1):
    f = j
    for i in range(len(ls) - 1 - j):
        if ls[f] > ls[j + i + 1]:
            f = j + i + 1
    if f != j:
        ls[j], ls[f] = ls[f], ls[j]
        n += 1
print(ls)
print(f"最优方法交换次数为{n}次")
