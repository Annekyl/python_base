# 选择排序
my_list = [12, 40, 10, 9, 8, -1, 21, -6]
# -----------------普通方法--------------------
n = 0  # 交换次数
for j in range(len(my_list) - 1):
    for i in range(len(my_list) - 1 - j):
        if my_list[j] < my_list[i + j + 1]:
            my_list[j], my_list[i + j + 1] = my_list[i + j + 1], my_list[j]
            n += 1
print(my_list)
print(f"普通方法交换次数为{n}次")

# --------------------改进方法----------------------
my_list = [12, 40, 10, 9, 8, -1, 21, -6]
n = 0
for j in range(len(my_list) - 1):
    f = j
    for i in range(len(my_list) - 1 - j):
        if my_list[f] < my_list[j + i + 1]:
            f = j + i + 1
    my_list[j], my_list[f] = my_list[f], my_list[j]
    n += 1
print(my_list)
print(f"优化方法交换次数为{n}次")

# -------------------最优方法---------------------
my_list = [12, 40, 10, 9, 8, -1, 21, -6]
n = 0
for j in range(len(my_list) - 1):
    f = j
    for i in range(len(my_list) - 1 - j):
        if my_list[f] < my_list[j + i + 1]:
            f = j + i + 1
    if f != j:
        my_list[j], my_list[f] = my_list[f], my_list[j]
        n += 1
print(my_list)
print(f"最优方法交换次数为{n}次")


# --------------选择排序方法1-----------------------
my_list1 = [12, 40, 10, 9, 8, -1, 21, -6]
n = 0  # 定义n为交换次数
for num in range(len(my_list1) - 1):  # 共需排数的次数
    for i in range(num + 1, len(my_list1) - 1):
        if my_list1[num] < my_list1[i]:
            my_list1[num], my_list1[i] = my_list1[i], my_list1[num]
            n += 1
print(my_list1)
print(f"排序次数为{n}次")

# --------------选择排序方法2-----------------------
my_list2 = [12, 40, 10, 9, 8, -1, 21, -6]
n = 0  # 定义n为交换次数
for num in range(len(my_list2) - 1):  # 共需排数的次数
    f = num
    for i in range(num + 1, len(my_list2) - 1):
        if my_list2[f] < my_list2[i]:
            f = i
    my_list2[num], my_list2[f] = my_list2[f], my_list2[num]
    n += 1
print(my_list2)
print(f"排序次数为{n}次")

# --------------选择排序方法3-----------------------
my_list2 = [12, 40, 10, 9, 8, -1, 21, -6]
n = 0  # 定义n为交换次数
for num in range(len(my_list2) - 1):  # 共需排数的次数
    f = num
    for i in range(num + 1, len(my_list2) - 1):
        if my_list2[f] < my_list2[i]:
            f = i
    if num != f:
        my_list2[num], my_list2[f] = my_list2[f], my_list2[num]
        n += 1
print(my_list2)
print(f"排序次数为{n}次")
