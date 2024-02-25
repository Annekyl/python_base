# win+R进入命令提示符，输入pip install tabulate 下载模块后程序方可运行
from tabulate import tabulate

print("--------------超市商品录入与查询系统----------------")
while 1:
    a = int(input("----------主菜单----------\n1.查询超市全部商品\n2.商品录入\n3.单个商品查询\n4.退出\n"))
    data = {"id": ['9787572218194', '9787544653114', '9787544654166', '9787530217610', '9787530221099'],
            "name": ['四级词汇书', '听力练习上册', '听力练习下册', '《兄弟》', "《文城》"],
            "price": ["48.00元", "40.00元", "40.00元", "68.00元", "59.00元"]}
    if a == 1:
        table = tabulate(data, headers="keys", showindex=True, tablefmt='simple', numalign='left')
        print(table)
    if a == 2:
        new_id = input("请扫描商品条形码")
        data["id"].append(new_id)
        new_name = input("请输入商品名称")
        data["name"].append(new_name)
        new_price = input("Q请输入商品价格")
        data["price"].append(new_price)
        print("商品已录入成功")
    if a == 3:
        choose = int(input("请选择:1.通过条形码查询 2.通过商品名查询"))
        if choose == 1:
            now_id = input("请扫描条形码")
            num = data["id"].index(now_id)
            print("商品id为:", data["id"][num])
            print("商品名称为:", data["name"][num])
            print("商品价格为：", data["price"][num])
        if choose == 2:
            now_name = input("请输入商品名")
            num = data["name"].index(now_name)
            print("商品id为:", data["id"][num])
            print("商品名称为:", data["name"][num])
            print("商品价格为：", data["price"][num])

    if a == 4:
        print("超市商品录入与查询系统已退出")
        break
