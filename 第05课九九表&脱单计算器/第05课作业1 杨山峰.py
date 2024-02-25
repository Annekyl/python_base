#  正九九乘法表
for i in range(1, 10):  # 从1取到9
    j = 1  # 重新赋值j等于1
    while j <= i:  # 第一个数字从1到i乘以i
        print(f"{j}*{i}={j * i}\t", end="")  # \t制表符，end起不换行的作用
        j += 1  # 将j加1后重新赋值给i
    print()  # 起到换行的作用
    i += 1  # 每次循环将后一个数字加1
print()  # 换行作用

print()

#  倒九九乘法表
j = 9
for number in range(9):  # 循环9次
    i = 1  # 每次循环都把i重新赋值为1
    while i <= j:
        print(f"{i}*{j}={i * j}\t", end='')
        i += 1  # 将i加1后重新赋值给i
    print()  # 换行
    j -= 1

print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}\t", end='')
    print()

print()

j = 9
for number in range(9):
    i = 0
    for a in range(j):
        i += 1
        print(f"{i}*{j}={i * j}\t", end='')
    j -= 1
    print()
