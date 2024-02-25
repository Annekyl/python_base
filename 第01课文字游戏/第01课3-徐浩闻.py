
a=input("请输入你的姓名：")
b=input("请输入你的性别：(1男 2女)")
c=input("请输入你的年龄：")
d=int(c)
if(b=="1"):
    if(d>20):
        print("欢迎你，老江湖勇士")
    else:
        print("欢迎你，少年英雄勇士")
elif(b=="2"):
     if(d>20):
        print("欢迎你，老江湖女神")
     else:
        print("欢迎你，少年英雄女神")
print("\n欢迎来到长江大学")
point=0                          #定义位置0为大门口

while(1):
  if(point==0):
        t=input("\n你来到了大门口。你的选择是（填入数字）：1左边三教 2中间一教 3右边二教")#选择
        if(t=="1"):
          print("\n你选择了左边三教")
          point=1                            #定义位置1为三教
        elif(t=="2"):
          print("\n你选择了中间一教")
          point=2                            #定义位置2为一教
        elif(t=="3"):
          print("\n你选择了右边二教")
          point=3                            #定义位置3为二教
        elif():
          print("\n别瞎搞，看清选项好好选")
  elif(point==1):
       t=input("\n你来到了三教门口 你的选择是（填入数字）：1进入教学楼 2向左进入农科大楼 0返回大门口")
       if(t=="1"):
          print("\n你选择了进入教学楼")
          point=4                            #定义位置4为三教教学楼
          print("\n教学楼里黑灯瞎火，前方的黑暗使你望而却步")
          point=1
          print("请重新选择：")
       elif(t=="2"):
          print("\n你选择了向左进入农科大楼")
          point=5                            #定义位置5为农科大楼
          print("\n你遇见了门口坐着的保安大爷，他向你询问你为何来这")
          x=input("\n你回答：1我来上课 2我没课，我来瞎转悠")
          if(x=="1"):
              print("\n大爷说：老师都回家了，这里有什么课上？回宿舍去")
              print("\n你悻悻地走出了大楼")
              point=1
          elif(x=="2"):
              print("\n大爷说：大晚上的乱晃什么，回宿舍去")
              print("\n大爷直接摇来了另一个大爷把你押送回宿舍")
              point=9
       elif(t=="0"):
          print("\n你选择了返回大门口")
          point=0
       elif():
          print("\n别瞎搞，看清选项好好选")
  elif(point==2):
        print("\n你来到了一教门口")
        print("\n你发现教学楼的门锁上了")
        point=0
        print("\n请重新选择（填入数字）：1左边三教  3右边二教")
        if(t=="1"):
          print("\n你选择了左边三教")            
        elif(t=="3"):
          print("\n你选择了右边二教")
          point=3
        elif():
          print("\n别瞎搞，看清选项好好选")
  elif(point==3):
        t=input("\n你来到了二教门口 你的选择是（填入数字）：1进入教学楼 2进入篮球场 0返回大门口")
        if(t=="1"):
          print("\n你选择了进入教学楼")
          point=6                            #定义位置6为一教教学楼
          print("\n你看见了大四同学在教室李认真复习，你羞愧难当,决定立刻回宿舍————睡觉！")
          point=9
        elif(t=="2"):
          print("\n你选择了进入篮球场")
          point=7                            #定义位置7为篮球场
          print("\n糟糕！你碰见了国旗护卫队的招新同学们，他们要硬拉你入伙。")
          y=input("\n快跑！你选择：1跑回宿舍 2跑回寝室 3 上床睡觉")
          if(y=="1"):
            point=9
          elif(y=="2"):
            point=9
          elif(y=="3"):
            point=9
        elif(t=="0"):
          print("\n你选择了返回大门口")
          point=0
        elif():
          print("\n别瞎搞，看清选项好好选")
  elif(point==9):
    print("\n你“被迫”回了宿舍")            #定义位置9为宿舍
    break
print("\nGame Over")
input()

      
      


    
      
