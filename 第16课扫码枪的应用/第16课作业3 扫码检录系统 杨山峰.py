print("运动会扫码检录系统")
total = 0
my_dict = {"id": [], "name": []}
while 1:
    new_id = input("请对照自己的学号扫描条形码")
    new_name = input("请输入你的名字")
    for i in my_dict["id"]:
        if i == new_id:
            print("请勿重复扫码！")
            break
    else:
        my_dict["id"].append(new_id)
        my_dict["name"].append(new_name)
        print("签到成功，欢迎你！")
        total += 1
    print(f"目前已到场{total}人")
