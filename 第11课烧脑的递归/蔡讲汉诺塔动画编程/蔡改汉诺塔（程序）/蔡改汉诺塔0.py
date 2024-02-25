# 文字版汉诺塔递归原程序

def han(x, a, b, c):
    if x == 1:
        print(a, '移动到', c)
    else:
        han(x - 1, a, c, b)  # 1
        print(a, '移动到', c)
        han(x - 1, b, a, c)  # 2


han(3, 'A', 'B', 'C')
