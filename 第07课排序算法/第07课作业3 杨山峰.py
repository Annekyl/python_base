def rank(mylist1):  # 定义子函数排序
    n = 0  # n为交换次数
    print(f"原列表为：\n{mylist1}")
    for num in range(len(mylist1) - 1):  # 一共需要排的次数
        f = num  # f为每次循环的列表元素最小值的下标索引
        for i in range(num + 1, len(mylist1)):
            if mylist1[f] > mylist1[i]:
                f = i
        if f != num:  # 如果后面的元素比num小则交换
            mylist1[num], mylist1[f] = mylist1[f], mylist1[num]
            n += 1
    print(f"排序后的列表为：\n{mylist1}")
    print(f"共交换{n}次\n")


mylist = [[12, 0, 8, 9, 6, 1, 21, 46], [3, 88, -2, 90, 100], [6, -3, 9, 12, 44, 0, 50, 70, -23, 8]]
for i in range(len(mylist)):  # 循环次数为列表中嵌套列表的数量
    list_one = mylist[i]  # 取出嵌套的列表
    rank(list_one)  # 对取出的列表排序
