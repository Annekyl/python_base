def hanoi(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
        return
    else:
        hanoi(n-1,a,c,b)
        hanoi(1,a,b,c)
        hanoi(n-1,b,a,c)
n=int(input('请输入汉诺塔的层数'))
h(n,'A','B','C')
