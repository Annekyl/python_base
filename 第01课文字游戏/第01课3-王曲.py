print("欢迎玩家来到长大武林")
a=input("敢问大侠名讳：")
b=input("见大侠一身黑袍，不知性别是？（男/女）：\n")
if (b=="男"):
    print("原来是独自闯荡长大的勇者",a,"啊！欢迎来到长大武林！")    
    c=int(input("不知勇者如今的年岁是："))
    if c<=20:
        print("居然是少年英雄，当真是英雄出少年啊！！")
    else:
        print("内心独白：（原来是江湖中的老油条了）")
else :
    print("原来是女神",a,"啊！欢迎来到长大武林！")
    c=int(input("不知女神如今的芳龄是："))
    if c<=20:
        print("居然是少女仙子，当真是英雄出少年啊！！")
    else:
        print("内心独白：（原来是江湖中的老油条了）")
print("我快步向前，来到了长大门口。")
print("              长大校园地图")
print()
print("食堂              宿舍楼            体育馆\n\n校医院            教区1             教区2\n\n                 大门\n")
point=1
while(1):
    if point==1:
        print("现在你在长大门口，你可以\n")
        t=int(input("1：向左校医院  2：中间教区1  3：右边教区2  4：后退出校"))
        q=("你现在在")
        if t==1:
            print(q,"校医院")
            point=2
        if t==2:
            print(q,"教区1")
            point=3
        if t==3:
            print(q,"教区2")
            point=4
        if t==4:
            print(q,"出去干嘛？")
            point=1
    if point==2:
        print("现在你在校医院，你可以\n")
        t=int(input("1：向前食堂  2：右边教区1  3：进入校医院 "))
        q=("你现在在")
        if t==1:
            print(q,"食堂")
            point=5
        if t==2:
            print(q,"教区1")
            point=3
        if t==3:
            print(q,"校医院内部，但是因为误入标本室被吓晕！！bad ending")
            break
    if point==3:
        print("现在你在教区1，你可以\n")
        t=int(input("1：向左校医院  2：右边教区2  3：后退出校"))
        q=("你现在在")
        if t==1:
            print(q,"校医院")
            point=2
        if t==2:
            print(q,"教区2")
            point=4
        if t==3:
            print(q,"出去干嘛？")
            point=1
    if point==4:  
        print("现在你在教区2，你可以\n")
        t=int(input("1：向前体育馆  2：左边宿舍楼  3：进入体育馆 4:后退"))
        q=("你现在在")
        if t==1:
            print(q,"体育馆")
            point=7
        if t==2:
            print(q,"宿舍楼")
            print("你获得了宿舍阿姨的帮助，她开车送你去你想去的终点")
            f=int(input("你选择：1：学校门口 2：校医院 3：教区1  4：教区2  5：体育馆  6：食堂"))
            if f==1:
                point=1
            if f==2:
                point=2
            if f==3:
                point=3
            if f==4:
                point=4
            if f==5:
                point=7
            if f==6:
                point=5
            point=5
        if t==3:
            print(q,"被飞来的篮球打晕，送去了校医院门口")
            point=2
    if point==5:
        print("现在你在食堂，你可以\n")
        t=int(input("1：向右宿舍楼  2：向左走后门出校  3：向后去校医院"))
        q=("你现在在")
        if t==1:
            print(q,"宿舍楼")
            point=6
        if t==2:
            print("你在校外玩的很开心！")
            break
        if t==3:
            print(q,"校医院")
    if point==6:
        print("现在你在宿舍楼，你可以\n")
        t=int(input("1：向左回到食堂  2：向右体育馆  3：通过教区1的后门去教区1"))
        q=("你现在在")
        if t==1:
            print(q,"食堂")
            point=5
        if t==2:
            print(q,"体育馆")
            point=7
        if t==3:
            print(q,"教区1")
            point=3
    if point==7:
        print("现在你在体育馆，你可以\n")
        t=int(input("1：向左宿舍楼  2：向后教区2"))
        q=("你现在在")
        if t==1:
            print(q,"宿舍楼")
            point=6
        if t==2:
            print(q,"教区2")
            point=4
