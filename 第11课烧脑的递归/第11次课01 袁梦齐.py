#年龄
def age(n):
    if (n==1):
     return (10)
    else:
     return age(n-1)+2

t=age(5)
print(t)

#桃子数
def tao(n):
    if(n==10):
        return (1)
    else:
        return (tao(n+1)+1)*2
t=tao(1)
print(t)

#阶乘
def ch(n):
    if(n==1):
        return (1)
    else:
        return ch(n-1)*n
t=ch(5)
print(t)

#斐波那契数
def fei(n):
    if (n==1):
        return (1)
    if (n==2):
        return (1)
    else:
        return fei(n-1)+fei(n-2)
t=fei(15)
print(t)

#分数和
def shu(n):
    if(n==1):
        return(1)
    else:
        return shu(n-1)+1/(2*n-1)


print('{:.4f}'.format(shu(6)))

#正负数和
def a(n):
    if(n==1):
        return(1)
    else:
        return a(n-1)+(-1)**(n-1)*(2*n-1)
print(a(8))

#正负分数和
def b(n):
    if(n==1):
        return(1)
    else:
        return b(n-1)+(-1)**(n-1)*(1/(2*n-1))

print('{:.4f}'.format(b(7)))
     
















    

