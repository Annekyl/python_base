def rank(mylist1):
    n = 0
    print(f"原列表为：\n{mylist1}")
    for num in range(len(mylist1) - 1):
        f = num
        for i in range(num + 1, len(mylist1)):
            if mylist1[f] > mylist1[i]:
                f = i
        if f != num:
            mylist1[num], mylist1[f] = mylist1[f], mylist1[num]
            n += 1
    print(f"排序后的列表为：\n{mylist1}")
    print(f"共交换{n}次\n")


mylist = [[12, 0, 8, 9, 6, 1, 21, 46], [3, 88, -2, 90, 100], [6, -3, 9, 12, 44, 0, 50, 70, -23, 8]]
for i in range(len(mylist)):
    list_one = mylist[i]
    rank(list_one)
