#水仙花数
#目标：求三到八位的水仙花数且支持重玩

ks=[]
y=0
while(1):
    kb=[]
    x=int(input("你想找出三到n？位的水仙花数？（仅支持最高八位）"))
    for i in range(100,10**x):                            #整体  三到八位
        for j in range(2,x):
            a=i//(10**j)#取出第一位
            a1=i%(10**j)#
            if(a>=1)and(a<10):
                ks.append(a)
                for g in range(1,8):
                    a=a1//(10**(j-g))
                    a1=a1%(10**(j-g))
                    ks.append(a)#依次取出每位数
                    if((j-g)==0):
                        break
                y=0

                for m in range(len(ks)):
                    y+=ks[m]**len(ks)#判断是否为水仙花数
        if(y==i):
            kb.append(i)
        ks=[]
    print(kb)


            
