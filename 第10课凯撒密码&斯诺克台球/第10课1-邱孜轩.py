c="1"
while(c=="1"):
    stt=input("请输入您要加密的数：")
    for i in stt:
        a=ord(i)+3
        b=chr(a)
        print(b,end="")
    print()
    stt=input("请输入您要解密的数：")
    for i in stt:
        a=ord(i)-3
        b=chr(a)
        print(b,end="")
    c=input("是否重来：1.重来    2.退出")
