import math      #导入库
def sushu(x):
    flag=0
    c=int(math.sqrt(x))+1
    for i in range(2,c):
        if(x%i==0):
            flag  =1
            break
        if(flag==1):
            return False
        if(flag==0):
            return True
list=[]
for a in range(1,1000):
  sushu(a)  
  if(sushu(a)==True):
        list.append(a)
print("1到1000内的素数为")
print(list)
print("个数为",len(list))
