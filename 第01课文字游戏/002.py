#print("请输入收款人姓名：")
#a=input()
a=input("请输入收款人姓名")
print("请输入性别")
b=input()
#c=int(b)


print("\n\n   微信收款凭证\n")
print("金额:",b)
print("收款人",a)

if(b=="男"):
    print("大款在你眼前，推VIP")
    print("加油勇士")
else:
    print("正常女客户")


print("Hero,你已经来到了地狱门口")
point=1

while(1):       #循环
    if(print==1):
        t=input("请选择：1左边3教   2中间1教  3右边2教")
        if(t=="1"):
            print("你选择了左边3教")
            point==3
        if(t=="2"):
            print("你选择了中间1教")
            point=0
        if(t=="3"):
            print("你选择了右边2教")
            point=2
        
    if(print==2):
        t=input("请选择：1向前6教   2返回大门")
        if(t=="1"):
            print("你选择了6教")
            point=6
        if(t=="2"):
            print("你回到了大门口")
            point=1
