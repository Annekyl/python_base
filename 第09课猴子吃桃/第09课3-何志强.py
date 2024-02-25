s = 1
while s==1:
    x = input("你是A.先手 B.后手")
    if x=='A':
        for i in range(30):
            if i%3==0:
                print(f"出{i},应该能赢")
    if x=='B':
        for i in range(30):
            if i % 3 == 0:
                print(f"出{i},应该能赢")
    s =int(input("1.再玩一次2.退出"))



1





