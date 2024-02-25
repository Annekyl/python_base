#原版
ls=[12,40,10,9,8,-1,21,6]
n=0
for j in range(len(ls)-1):
    for i in range(len(ls)-1-j):
        if(ls[j]<ls[i+j+1]):
            ls[j],ls[i+j+1]=ls[i+j+1],ls[j]
            n+=1
print(ls)
print("共算了",n,"次")
#进阶版???
ls=[12,40,10,9,8,-1,21,6]
n=0
for j in range(len(ls)-1):
    f=j
    for i in range(len(ls)-1-j):
        if(ls[f]<ls[i+j+1]):
            f=i+j+1
    ls[j],ls[f]=ls[f],ls[j]
    n+=1       
print(ls)
print("共算了",n,"次")
#超级进阶版???
ls=[12,40,10,9,8,-1,21,6]
n=0
for j in range(len(ls)-1):
    f=j
    for i in range(len(ls)-1-j):
        if(ls[f]<ls[i+j+1]):
            f=i+j+1
    if(f!=j):
        ls[j],ls[f]=ls[f],ls[j]
        n+=1       
print(ls)
print("共算了",n,"次")
