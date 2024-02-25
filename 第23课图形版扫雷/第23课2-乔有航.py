import turtle as t
import random as r

t.hideturtle()
p1 = t.Pen()
t1 = t.Pen()
t1.hideturtle()
xx=None
yy=None

class Min():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.txt='■'
        self.stat=False
        self.star=0#邻居
        self.blank=0#空白
    
    def __str__(self)  :
        return ("mine%d%d"%(self.x,self.y))
    
    def dig(self):
        global Game
        if self.stat==True:
            Game=1
            p1.goto(-10, -100)
            p1.write('你没了 还打不打', font=("Arial", 30, 'normal'))
            print('game over')
            return
        if self.star!=0:
            self.txt=str(self.star)
        else:
            self.txt="□"
    
    def show(self, i, j):
        t1.up()
        t1.goto(i * 40, j * 40)
        t1.write(mines[i][j].txt, font=("微软黑体", 20, "normal"))

 

def con(a,b):#####内部三层调用
    if mines[a][b].star==0 and mines[a][b].blank==0:
        mines[a][b].blank=1
        for i in range(3):
            for j in range(3):
                if(0<=a-1+i<=9 and 0<=b-1+j<=9):
                    mines[a-1+i][b-1+j].dig()
                    a1=a-1+i
                    b1=b-1+j
                    con(a1,b1)

def click():
    print(xx)
    print(yy)
    for i in range(10):
        for j in range(10):
            if i*40-20 < xx < i*40+20 and j*40-20 < yy < j*40+20:
                mines[i][j].dig()
                con(i, j) 
            else:
                pass

mines=[[0 for _ in range(10)]for _ in range(10)]

for i in range(10):
    for j in range(10):
        mines[i][j]=Min(i,j)

def draw():
    t.tracer(0)
    for i in range(10):
        for j in range(10):
            mines[i][j].show(i, j)
    t.tracer(1)

def clik(x, y):
    global xx, yy  # 声明xx和yy为全局变量
    p1.clear()  # 清除之前的文本内容
    p1.goto(-10, -100)
    xx = float(x)
    yy = float(y)
    #tr1 = 'x' + str(x) + "   y=" + str(y)
    #p1.write(tr1, font=("Arial", 30, 'normal'))
    #print(xx)
    #print(yy)
    click()
    t1.clear()
    draw()

    while Game==0:
        screen = t.Screen()
        screen.onclick(clik)
        break
draw()
Game=0
sum=0
while(sum<10):
    a=r.randint(0,9)
    b=r.randint(0,9)
    if(mines[a][b].stat==False):
        mines[a][b].stat=True
        #mines[a][b].txt='*'
        sum+=1
        for i in range(3):
            for j in range(3):
                if(0<=a-1+i<=9 and 0<=b-1+j<=9):
                    mines[a-1+i][b-1+j].star=mines[a-1+i][b-1+j].star+1

screen = t.Screen()
screen.onclick(clik)
