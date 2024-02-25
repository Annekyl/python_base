import turtle as t
a=1
b=2
c=2
X=[a,b,c]
Y=[]
u=1


t.register_shape('河.gif')
t4 = t.Turtle()
t4.shape('河.gif')
t4.pu()

t.register_shape('船.gif')
t5 = t.Turtle()
t5.shape('船.gif')
t5.pu()

t.register_shape('狼.gif')
t1 = t.Turtle()
t1.shape('狼.gif')
t1.pu()
    
t.register_shape('羊.gif')
t2 = t.Turtle()
t2.shape('羊.gif')
t2.pu()

t.register_shape('菜.gif')
t3 = t.Turtle()
t3.shape('菜.gif')
t3.pu()
def tp(l,x,j,k,list1,list2):
    print(f'将{x}从{j}岸{k}岸')
    i=list1.index(l)
    list1.pop(i)
    list2.append(l)
def move1():
    for g in range(4):
        num=sum(X)
        if num==5 or num==1:
            tp(a,'羊','1','2',X,Y)
            t2.goto(0,0)
            t2.goto(300,0)
        elif num==4:
            tp(b,'狼','1','2',X,Y)
            t1.goto(0,0)
            t1.goto(300,300)
            
        else:
            tp(c,'菜','1','2',X,Y)
            t3.goto(0,0)
            t3.goto(300,-300)
        num2=sum(Y)
        if num2==3:
            tp(a,'羊','2','1',Y,X)
            t2.goto(0,0)
            t2.goto(-300,0)
def move2():
    for g in range(4):
            num=sum(X)
            if num==5 or num==1:
                tp(a,'羊','1','2',X,Y)
                t2.goto(0,0)
                t2.goto(300,0)
            elif num==4:
                tp(b,'菜','1','2',X,Y)
                t3.goto(0,0)
                t3.goto(300,-300)
            else:
                tp(c,'狼','1','2',X,Y)
                t1.goto(0,0)
                t1.goto(300,300)
            num2=sum(Y)
            if num2==3:
                tp(a,'羊','2','1',Y,X)
                t2.goto(0,0)
                t2.goto(-300,0)

while(u==1):
    t1.goto(-300,300)
    t2.goto(-300,0)
    t3.goto(-300,-300)
    X=[a,b,c]
    Y=[]
    s=int(input("您要选择：1.方案一  2.方案二\n"))
    if s==1:
        move1()
    if s==2:
        move2()
    u=int(input("您可以尝试：1.再玩一次  2.退出\n"))











t.done
