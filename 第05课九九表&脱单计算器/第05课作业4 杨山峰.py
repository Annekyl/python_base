# ------------模块设计---------------
def judge(a):  # 通过布尔类型判断是否为素数并将结果返回给子函数
    if a < 2:  # 1不是素数
        return False
    if a < 4:  # 2和3都是素数
        return True
    if a % 2 == 0:  # 能被2整除的数都不是素数
        return False
    for i in range(3, int(a ** 0.5) + 1, 2):  # 若为合数且为奇数，必定有一个比所给数开根号小的因子
        if a % i == 0:
            return False
    else:
        return True


# -------------主程序------------
x = 0  # 素数的个数
list = []
for num in range(1, 1001):  # 循环遍历从1到1000的数判断是否为素数
    if judge(num):  # 结果为True，输入该数并给x加1
        list.append(num)
        x += 1
print(list)
print(f"\n1到1000共有{x}个素数")  # 输出从1到1000共有多少素数
