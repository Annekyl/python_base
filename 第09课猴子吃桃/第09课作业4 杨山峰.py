# 求闰年数量
print("欢迎使用闰年计算器\n")
while 1:
    start = int(input("请输入起始年份:\n"))
    end = int(input("请输入结束年份:\n"))
    all_years = []
    num = 0
    print("闰年有：", end='')
    for year in range(start, end + 1):
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, end=',')
                num += 1
                continue
        elif year % 100 != 0 and year % 4 == 0:
            print(year, end=',')
            num += 1
        else:
            pass
    print(f"在{start}和{end}之间共有{num}个闰年")
    a = input("您还要再玩一次吗？ 1:继续 2.不玩了")
    if a == '2':
        print("\n闰年计算器已关闭")
        break
