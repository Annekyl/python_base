# 1. 条件表达式
"""
a = int(input("请输入a值："))
b = int(input("请输入b值："))
c = a if a > b else b  # 条件表达式
print("a和b中大的数字为：{}".format(c))
print("a和b中小的数字为：{}".format(a if a < b else b))
"""
# 2. for表达式
'''
my_list1 = [x for x in range(5)]
print(my_list1)
'''
# 3. for表达式+条件表达式
my_list2 = [x for x in range(5) if x > 2]
print(my_list2)
# 除与整除
print(100 / 3)
print(100 // 3)
