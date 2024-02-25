while(1):          #只用一个while语句以达到回到主菜单的效果
    print("\n请输入您要使用的系统：1.绩点计算器 2.BMI计算器")          
    print("\n（如果您的某单科成绩未达六十分，请不要使用绩点计算器系统）")
    s=input()      #通过变量s选择计算器1

        
    if(s=="1"):     
    #——————————绩点计算器——————————
        
        num = int(input("请输入你选修的科目数：\n"))  #通过输入的科目数字来决定循环次数
        credit=[]
        grade=[]                        #设置三个空列表
        gpa=[]
        b=0
        o=0                             #为循环数字设置初始量
        while (1<=num):
            for i in range(b,b+1):
                o=o+1
                m = f'name{i}'          #给m设置递增
                print("\n请输入第",o,"科学分")
                m = float(input())  
                credit.append(m)        #将m的值加入空列表
                #m为学分
                w= f'name{i}'           #给w设置递增          
                print("\n请输入第",o,"科成绩")
                w = float(input())
                #w的值用于计算n
                n = (w/10-5)       
                grade.append(n)         #将n的值加入grade
                p = f'name{i}'
                p=m*n
                #p为第X科的绩点
                gpa.append(p)  
            b=b+1             #根据b的数值循环
            num=num-1         #确保数据准确
        a=sum(credit)
        #a为学分总和
        g=sum(gpa)
        #g为各科成绩乘以各科学分总和
        average_gpa=g/a
        #计算加权平均绩点
        print("\n您的平均绩点为%.2f"%average_gpa)
        if(g<=1):
                print("\n不及格，小子！")#对使绩点小于1的数据不进行计算
        print("\n接下来您想做什么？")
        s=input("\n1.重新计算绩点  2.使用BMI计算器 3.返回主菜单 4.退出")
        if(s=="4"):
            print("\n感谢使用，祝您生活愉快！")#结束循环
            break

    if(s=="2"):
    #——————————BMI计算器——————————
        height = float(input("\n请输入你的身高（m）："))
        weight = float(input("\n请输入你的体重（Kg）："))
        bmi = (weight/(height**2))        #计算bmi
        print("\n(你的肥胖指数为%.2f)"%bmi)
        if (bmi<18):
            print("\n(要好好吃饭哦。)")
        if (bmi>=18) and (bmi<=24):
            print("\n(很理想哦。)")
        if (bmi>24) and (bmi<=28):
                print("\n(肥而不腻！)")
        if (bmi>28):
            print("\n宰相肚里能撑船！")   #根据bmi数据的大小输出结果
        print("\n接下来您想做什么？")
        s = input("\n1.使用绩点计算器 2.重新计算BMI 3.返回主菜单 4.退出")
        if(s=="4"):
            print("\n感谢使用，祝您生活愉快！")      #结束循环
            break
