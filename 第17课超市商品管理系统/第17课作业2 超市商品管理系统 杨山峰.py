from random import randint
import turtle as t

t.hideturtle()
t.penup()
x = -200
y = 100
print("--------------超市商品录入与查询系统----------------")
point = 0
while point == 0:
    sel = input("1.登录 2.注册 3.退出")
    if sel == "2":
        f = open('超市系统登陆账户.txt', "a", encoding="UTF-8")
        m = input("请输入员工码")
        f.write("\n" + m + "\t")
        n = input("请输入密码")
        f.write(n)
        f.close()
    if sel == "1":
        f = open('超市系统登陆账户.txt', "r", encoding="UTF-8")
        m = input("请输入员工码")
        n = input("请输入密码")
        lock = randint(1000, 9999)
        q = int(input(f"请输入验证码{lock}"))
        total_users = f.readlines()
        for i in total_users:
            i = i.strip()
            if i == m + "\t" + n:
                print("登录成功！")
                point = 1
                break
        else:
            print("登录失败！")
    if sel == "3":
        break
while point == 1:
    a = int(input(
        "----------主菜单----------\n1.查询超市全部商品\n2.商品录入\n3.单个商品查询\n4.收银\n5.查看销售情况 6.退出\n"))
    if a == 1:
        f = open('商品统计.txt', "r", encoding="UTF-8")
        total_data = f.readlines()
        for i in total_data:  # 按行打印
            i = i.strip()  # 去除前后空格和换行符
            print(i)
        f.close()
    if a == 2:
        f = open('商品统计.txt', "a", encoding="UTF-8")
        new_id = input("请扫描商品条形码")

        f.write("\n" + new_id)
        new_name = input("请输入商品名称")
        f.write("\t" + new_name)
        new_price = input("请输入商品价格")
        f.write("\t" + new_price)
        new_number = input("请输入商品数量")
        f.write("\t" + new_number)
        print("商品已录入成功")
        f.close()
    if a == 3:
        select_id = input("请扫描商品的条形码")
        if select_id != "":
            f = open('商品统计.txt', "r", encoding="UTF-8")
            total_data = f.readlines()
            for i in total_data:
                now_i = i[0:13:1]
                if select_id == now_i:
                    print(i)
                    break
            else:
                print("商品不存在！")
            f.close()
    if a == 4:
        while 1:
            sale = input("请扫描商品条形码")
            if sale != "":
                f = open("商品统计.txt", "r", encoding="UTF-8")
                total_data = f.readlines()
                my_list = total_data
                f.close()
                for i in my_list:
                    i = i.strip()
                    is_sale = i[0:13:1]
                    if is_sale == sale:
                        print(i)
                        print("出库成功！")
                        f = open("销售额统计.txt", "a", encoding="UTF-8")
                        for line in f:
                            if is_sale == line[0:13:1]:
                                f
                        f.close()
                        t.goto(x, y)
                        t.write(i)
                        y -= 15
            else:
                break
    if a == 5:
        f = open("销售额统计.txt", "r", encoding="UTF-8")
        total_sale = f.readlines()
        for i in total_sale:
            i = i.strip()
            print(i)
        f.close()
    if a == 6:
        print("超市商品录入与查询系统已退出")
        break
