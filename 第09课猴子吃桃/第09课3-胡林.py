a = input("选择抢1先手还是2后手：")
lst = []

if a == "2":
    for i in range(1, 31):
        if i % 3 == 0:
            lst.append(i)

print("保证倒数第二次以27收尾就行")
print(lst)
print("每次收尾都是列表中的数")
