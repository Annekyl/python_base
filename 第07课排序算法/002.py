# 冒泡排序
ls = [12, 40, 10, 9, 8, -1, 21, -6]
m = 0
for a in range(len(ls) - 1):
    for i in range(len(ls) - a - 1):
        if ls[i] > ls[i + 1]:
            ls[i], ls[i + 1] = ls[i + 1], ls[i]
            m += 1
print(ls)
print(f"共交换{m}次")
