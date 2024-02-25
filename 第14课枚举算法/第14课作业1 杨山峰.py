point = 1
while point == 1:
    a = int(input("请选择你要求的水仙花数的位数"))
    for num in range(10 ** (a - 1), 10 ** a):
        num_str = str(num)
        num_sum = 0
        for i in num_str:
            num_sum += int(i) ** a
        if num_sum == num:
            print(num)
    point = int(input("你还要继续吗？1.继续 2.结束"))
