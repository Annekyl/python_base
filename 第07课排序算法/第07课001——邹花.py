
#——————————---------普通选择排序————————————————————
p=[12,40,10,9,8,-1,21,-6]#数据
n=0
for j in range(len(p)-1):
    for i in range(len(p)-(j+1)):
        if p[j]>p[i+(j+1)]:
            p[j],p[i+(j+1)]=p[i+(j+1)],p[j]
            n+=1
            print(p)
print("普通选择排序数据交换次数为：",n)
print()

#——————————---------改进型选择排序————————————————————
p=[12,40,10,9,8,-1,21,-6]#数据
n=0
for j in range(len(p)-1):
    f=j
    for i in range(len(p)-(j+1)):
        if (p[f]>p[i+(j+1)]):
            f=i+(j+1)
    p[j],p[f]=p[f],p[j]
    n+=1
    print(p)
print("改进型选择排序数据交换次数为：",n)
print()

#——————————---------最优选择排序————————————————————
p=[12,40,10,9,8,-1,21,-6]#数据
n=0
for j in range(len(p)-1):
    f=j
    for i in range(len(p)-(j+1)):
        if (p[f]>p[i+(j+1)]):
            f=i+(j+1)
    if(f!=j):
        p[j],p[f]=p[f],p[j]
        n+=1
    print(p)
print("改进型选择排序数据交换次数为：",n)


