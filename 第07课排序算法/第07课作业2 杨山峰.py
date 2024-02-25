# ---------------冒泡排序--------------
my_list = [12, 40, 10, 9, 8, -1, 21, -6]
m = 0  # m为交换次数
for num in range(len(my_list) - 1):  # 共需排数的次数
    for i in range(len(my_list) - 1 - num):
        if my_list[i] < my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            m += 1
print(my_list)
print(f"共交换{m}次")
