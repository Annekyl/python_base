print("请输入盘子数量")
n=int(input())
def hannuo(n,x,y,z):
    if n==1:
        print(x,'~~',z)
        return
    hannuo(n-1,x,y,z)
    hannuo(1,x,y,z)
    hannuo(n-1,y,x,z)
print(hannuo(n,1,2,3))
    
