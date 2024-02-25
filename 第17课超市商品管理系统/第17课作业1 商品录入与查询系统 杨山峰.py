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
while point == 1:
    a = int(input("----------主菜单----------\n1.查询超市全部商品\n2.商品录入\n3.单个商品查询\n4.退出\n"))
    if a == 1:
        f = open('商品统计.txt', "r", encoding="UTF-8")
        total_data = f.readlines()
        for i in total_data:
            i = i.strip()
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
        print("超市商品录入与查询系统已退出")
        break
