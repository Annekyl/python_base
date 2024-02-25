#任务五：汉诺塔

def ad_ls(x,z):
    if x=='A':
        temp=a[len(a)-1]
        del a[len(a)-1]
    if x=='B':
        temp=b[len(b)-1]
        del b[len(b)-1]
    if x=='C':
        temp=c[len(c)-1]
        del c[len(c)-1]
    #print("temp=",temp)
    if z=='A':
        a.append(temp)
    if z=='B':
        b.append(temp)
    if z=='C':
        c.append(temp) 
    print(a,b,c)
    

def han(n,x,y,z):
    if n==1:
        print(x,'移动到',z)
        ad_ls(x,z)

    else:
        han(n-1,x,z,y) #1
        ad_ls(x,z)
        han(n-1,y,x,z) #2

a=[3,2,1]
b=[]
c=[]
print(a,b,c)
print()
han(3,'A','B','C')        


