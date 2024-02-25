print("欢迎使用凯撒法加密与解密器")

while 1:
    a = int(input("\n请选择：1.加密 2.解密 "))

    if a == 1:
        write = input("请输入你要加密的内容：")

        print("加密后的内容为：")
        for i in write:
            num1 = ord(i) + 3
            re_write = chr(num1)
            print(re_write, end='')

    if a == 2:
        write = input("请输入你要解密的内容：")

        print("解密后的内容为：")
        for i in write:
            num1 = ord(i) - 3
            re_write = chr(num1)
            print(re_write, end='')

    b = int(input("\n你还要继续使用吗？ 1.继续 2.结束"))
    if b == 1:
        continue
    if b == 2:
        break
