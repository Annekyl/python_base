point=1
while(1):
    if point==1:
        n=int(input("请选择玩几位水仙花数？ (3-8)"))
        for i in range(10**(n-1),10**(n)):    #在十进制位次里找一个数
            a=str(i)                          #'str()'一次只放一个字符
            b=0
            for j in range(n):
                b=b+int(a[j])**n              #将str()里里面装的字符每个n次方后相加
                if b==i:
                    print(i)

        c=input('是否再来一次  1.是')
        if c=='1':
            point=1
        else:
            break
       
    
