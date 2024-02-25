#————————————普通型选择排序——————————
ls=[12,40,10,9,8,-1,21,-6]
print(ls)
n=0
for j in range(len(ls)-1):
    for i in range(len(ls)-(j+1)):   
        if(ls[j]<ls[i+(j+1)]):

            ls[j],ls[i+(j+1)]=ls[i+(j+1)],ls[j]
            n+=1
print(ls)
print("普通型选择排序次数为%d"%n)
#————————————改进型选择排序——————————
ls=[12,40,10,9,8,-1,21,-6]
print(ls)
n=0

for j in range(len(ls)-1):
    f=j
    for i in range(len(ls)-(j+1)):   
        if(ls[f]<ls[i+(j+1)]):
            f=i+(j+1)

    ls[j],ls[f]=ls[f],ls[j]
    n+=1
print(ls)
print("改进型选择排序次数为%d"%n)
#————————————最优型选择排序——————————
ls=[12,40,10,9,8,-1,21,-6]
print(ls)
n=0

for j in range(len(ls)-1):
    f=j
    for i in range(len(ls)-(j+1)):   
        if(ls[f]<ls[i+j+1]):
            f=j+i+1
    if(f!=j):
        ls[j],ls[f]=ls[f],ls[j]
        n+=1
    
print(ls)
print("最优型选择排序次数为%d"%n)







