# win+R输入cmd进入命令提示符，输入pip install tabulate下载模块
import json
from random import randint
from tabulate import tabulate

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

f = open("商品统计2.txt", "r", encoding="UTF-8")
js_data = f.readlines()
data = {}
for i in js_data:
    data = json.loads(i)
# print(data)
f.close()
while point == 1:
    a = int(input(
        "----------主菜单----------\n1.查询超市全部商品\n2.商品录入\n3.单个商品查询\n4.收银\n5.查看销售额 6.退出\n"))
    if a == 1:
        table = tabulate(data, headers="keys", showindex=True, tablefmt='simple', numalign='left')
        print(table)
    if a == 2:
        new_id = input("请扫描商品条形码")
        data["id"].append(new_id)
        new_name = input("请输入商品名称")
        data["name"].append(new_name)
        new_price = float(input("请输入商品价格"))
        data["price"].append(new_price)
        new_number = int(input("请输入商品数量"))
        data["number"].append(new_number)
        print("商品已录入成功")
        f = open("商品统计2.txt", "w", encoding="UTF-8")
        js_data = json.dumps(data)
        f.write(js_data)
        f.close()
    if a == 3:
        choose = int(input("请选择:1.通过条形码查询 2.通过商品名查询"))
        if choose == 1:
            now_id = input("请扫描条形码")
            num = data["id"].index(now_id)
            print("商品id为:", data["id"][num])
            print("商品名称为:", data["name"][num])
            print("商品价格为：{:.2f}元".format(data['price'][num]))
            print(f"商品数量为：{data['number'][num]}")
        if choose == 2:
            now_name = input("请输入商品名")
            num = data["name"].index(now_name)
            print("商品id为:", data["id"][num])
            print("商品名称为:", data["name"][num])
            print("商品价格为：{:.2f}元".format(data['price'][num]))
            print(f"商品数量为：{data['number'][num]}")
    if a == 4:
        print("显示小票时点击窗口即可关闭")
        judge = 1  # 判断是否重复收银
        total_price = 0
        now_data = {"id": [], "name": [], "price": [], "number": []}
        while judge == 1:
            now_id = input("请扫描商品条形码")
            num = data["id"].index(now_id)
            total_price += data["price"][num]
            data["number"][num] = data["number"][num] - 1  # 商品数量减1
            # 是否同一个商品购买多次
            for i in now_data["id"]:
                if i == now_id:
                    v = now_data["id"].index(i)
                    now_data["number"][v] = now_data["number"][v] + 1
                    break
            else:
                now_data["id"].append(data["id"][num])
                now_data["name"].append(data["name"][num])
                now_data["price"].append(data["price"][num])
                now_data["number"].append(1)
            judge = int(input("是否继续 1.继续 2.结束扫码"))

        receive = input("请扫描收款码")
        is_correct = receive[0:2:1]
        is_correct = int(is_correct)
        if is_correct == 10 or is_correct == 11 or is_correct == 12 or is_correct == 13 \
                or is_correct == 14 or is_correct == 15:
            if len(receive) == 18:
                print("付款成功，谢谢惠顾！")
                table = tabulate(now_data, headers="keys", showindex=True, tablefmt='simple', numalign='center')
                print(table)
                print("总金额为{:.2f}元".format(total_price))
                import turtle as t

                t.hideturtle()
                t.pensize(30)
                t.penup()
                t.goto(-200, 100)
                t.write(table, font=("华文仿宋", 20, "normal"))
                t.exitonclick()
            else:
                print("付款失败！")
        else:
            print("付款失败！")
        f = open("商品统计2.txt", "w", encoding="UTF-8")
        js_data = json.dumps(data)
        f.write(js_data)
        f.close()
        f = open("销售额统计2.txt", "w", encoding="UTF-8")
        js_sale_data = json.dumps(now_data)
        f.write(js_sale_data)
        f.close()
    if a == 5:
        f = open("销售额统计2.txt", "r", encoding="UTF-8")
        js_sale_data = f.readlines()
        sale_data = {}
        for i in js_sale_data:
            sale_data = json.loads(i)
        f.close()
        table = tabulate(sale_data, headers="keys", showindex=True, tablefmt='simple', numalign='left')
        print(table)
    if a == 6:
        print("超市商品录入与查询系统已退出")
        break
