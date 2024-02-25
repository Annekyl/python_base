def yue(n,a,b,c):
    if n>0:
        yue(n-1,a,c,b)     #将A上n-1个盘移动到B上    
        print("Move disk %d frome %s to %s"%(n,a,c))
        yue(n-1,b,a,c)     #将B上n-1个盘移动到C上

n=int(input("请输入层数"))
yue(n,'A','B','C')
