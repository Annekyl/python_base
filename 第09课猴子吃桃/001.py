num = 100
str1 = str(num)
my_list = []
for i in str1:
    my_list.append(i)
print(my_list)
j = int(my_list.pop(-1))
print(j)
print(type(j))
