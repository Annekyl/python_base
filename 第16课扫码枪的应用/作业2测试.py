receive = input("请扫描收款码")
is_correct = receive[0:2:1]
is_correct = int(is_correct)

print(is_correct)
print(type(is_correct))