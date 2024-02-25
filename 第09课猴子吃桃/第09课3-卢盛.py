print('抢三十作弊器')


b=input('由选择由谁先开始游戏：\n\n1.自己 2.对方')
n=1
if b=='1':
    for i in range(1,30):
        if i%3==0:
            n=i
            print(n,end='\t')

if b=='2':
    for i in range(1,30):
        if i%3==0:
            n=i
            print(n,end='\t')
print('\n试着去抢这些数，你会发现你肯定赢的')
