def f(n):
    if(n==1 or n==2):
        return(1)
    else:
        return f(n-1)+f(n-2)



while(1):
    n=int(input("请输入n的值为"))
    y=0
    for i in range(1,n+1):
       y=y+f(i)
    print(y)
