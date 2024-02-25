def c(a, s):  #定义一个加密模块
    r = ""   
    for i in range(len(a)):  
        h = a[i]
        if h.islower():  #找小写字母
            r += chr((ord(h)+s - 97)%26 + 97)
        elif h.isupper():#找大写字母
            r += chr((ord(h)+s - 65)%26 + 65)
        elif h.isdigit():#找数字
            r +=chr((ord(h)+s - 48)%10 + 48)#根据ascii表把可打印字符分为几大块
        elif ord(h)>122:
            r +=chr((ord(h)+s-123)%5+123)
        elif ord(h)>90:
            r +=chr((ord(h)+s-91)%6+91)
        elif ord(h)>57:
            r +=chr((ord(h)+s-58)%7+58)
        elif ord(h)>31:
            r +=chr((ord(h)+s-32)%16+32)
        else:
            print("?")
    return r#每一次循环都会存下r的结果，便于添加字符和打印出来
   

m="1"
while(m=="1"):
    a = input("\n无论数字，大小写字母和符号，输入您需要加密的文本：\n") #a是你输入的文本 
    s=int(input("\n无论正负，请您添加一个偏移量加密您的代码：\n"))    #s是前后推的值，你改成几就是往后推几
    print("\n您加密后的文本为：\n"+c(a,s))#直接使用+把函数输出打印出来
    print("\n您需要重玩吗？您可以通过将偏移量设置为相反数得到您加密前的文本哦。)")
    m=input("\n1.重玩  2.退出")






