# 逢三过
print("欢迎使用逢三过作弊器")
total = int(input("请输入游戏总人数"))
location = int(input("请输入你位于第几位："))
num1 = location  # 数字
speak = 1
while 1:
    if num1 % 3 == 0 or '3' in str(num1):
        input(f"第{speak}次不需要报数")
        num1 += total
        speak += 1
    elif num1 % 3 != 0:
        input(f"第{speak}次你要说的数字是：{num1}")
        num1 += total
        speak += 1
