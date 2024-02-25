#任务五：汉诺塔

def han(n,x,y,z):
    if n==1:
        #print(x,'移动到',z)
        z.append(x[len(x)-1])
        del x[len(x)-1]
        print(a,b,c)
    else:
        han(n-1,x,z,y) #1
        #print(x,'移动到',z)
        z.append(x[len(x)-1])
        del x[len(x)-1]
        print(a,b,c)
        han(n-1,y,x,z) #2

a=[3,2,1]
b=[]
c=[]
print(a,b,c)
print()
han(3,a,b,c)



