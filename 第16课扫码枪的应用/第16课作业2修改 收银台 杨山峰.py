# win+R进入命令提示符，输入pip install tabulate 下载模块后程序方可运行
from tabulate import tabulate
from random import randint

print("--------------超市商品录入与查询系统----------------")
m = input("请输入员工码")
n = input("请输入密码")
lock = randint(1000, 9999)
q = int(input(f"请输入验证码{lock}"))
point = 0
if m == "1" and n == "1" and q == lock:
    point = 1
else:
    print("验证失败！")
data = {"id": ['9787572218194', '9787544653114', '9787544654166', '9787530217610', '9787530221099'],
        "name": ['四级词汇书', '听力练习上册', '听力练习下册', '《兄弟》', "《文城》"],
        "price": [48.00, 40.00, 40.00, 68.00, 59.00],
        "number": [40, 56, 30, 14, 37]}
while point == 1:
    a = int(input("----------主菜单----------\n1.查询超市全部商品\n2.商品录入\n3.单个商品查询\n4.收银\n5.退出\n"))
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
    if a == 3:
        choose = int(input("请选择:1.通过条形码查询 2.通过商品名查询"))
        if choose == 1:
            now_id = input("请扫描条形码")
            num = data["id"].index(now_id)
            print("商品id为:", data["id"][num])
            print("商品名称为:", data["name"][num])
            print("商品价格为：{:.2f}元".format(data['price'][num]))
        if choose == 2:
            now_name = input("请输入商品名")
            num = data["name"].index(now_name)
            print("商品id为:", data["id"][num])
            print("商品名称为:", data["name"][num])
            print("商品价格为：{:.2f}元".format(data['price'][num]))
    if a == 4:
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
            else:
                print("付款失败！")
        else:
            print("付款失败！")
    if a == 5:
        print("超市商品录入与查询系统已退出")
        break
