num = int(input("请输入大于1的整数"))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num}不是素数")
            break
        else:
            print(f"{num}是素数")

else:
    print("输入错误")

num = int(input("请输入大于1的整数"))
if num > 1:
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            print(f"{num}不是素数")
            break
        else:
            print(f"{num}是素数")

else:
    print("输入错误")

num = int(input("请输入大于1的整数："))
if num > 1:
    if num == 2:
        print(f"{num}是素数")
    elif num % 2 == 0:
        print(f"{num}不是素数")
    else:
        for i in range(3, int(num ** 0.5 + 1), 2):
            if num % i == 0:
                print(f"{num}不是素数")
            else:
                print(f"{num}是素数")
