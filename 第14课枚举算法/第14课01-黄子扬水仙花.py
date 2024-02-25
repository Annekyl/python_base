
def num(n):
    data=[]
    for i in range(10**(n-1),10**n):
        a=str(i)#str将i 带的数值转化位字符串
        b=0
        for j in a:
            num=int(j)
            b+=num**n
        if i==b:
            data.append(i)
    print(data)
    data=[]
while(1):
    x=1
    n=int(input("请选择水仙花数的位数（3-8）"))
    if x==1:
        num(n)
        x=int(input('是否继续使用1：继续使用  2：退出'))
    if x==2:
        break
#程序应该没问题，但是当n=8时无法显示，不知道是不是算力的问题  
  
#for i in range(10**(n-1),10**n):
    
