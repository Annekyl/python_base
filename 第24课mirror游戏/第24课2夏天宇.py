import turtle as t
import random
import threading


screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("white")
#鼠标
t1 = t.Turtle()
t2 = t.Turtle()
#方块
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()
t7 = t.Turtle()
t8 = t.Turtle()
#画笔初始化
t1.speed(0)
t2.speed(0)
t1.shape('circle')
t2.shape('circle')
t2.up()
t1.up()

color = ["pink", "purple", "red", "green", "blue", "bisque", "bisque", \
         "yellow", "pink", "purple", "deeppink"]#颜色


class Falling(threading.Thread):#####导入多线程可以让笔同时跑
    def __init__(self, turtle):
        super().__init__()#初始化 速度 颜色 大小
        self.turtle = turtle
        self.dd = random.randint(-350, 300)
        self.ss = random.randint(1, 2)
        self.cc = random.randint(0, len(color) - 1)
        self.ff = random.randint(2, 3)
        self.turtle.shape('square')
        self.turtle.shapesize(1, self.ff)
        self.turtle.up()
        self.turtle.color(color[self.cc])
        self.turtle.speed(0)
        self.turtle.goto(self.dd, 400)
        self.turtle.speed(self.ss)
        self.turtle.seth(-90)

    def run(self):#跑动 用循环跑
        for i in range(10):
            self.turtle.fd(700)
            self.dd = random.randint(-300, 300)
            self.turtle.goto(self.dd, -400)#跑到下面改变位置
            self.turtle.color(color[self.cc])#改变颜色
            self.turtle.fd(-700)
            self.turtle.goto(self.dd, 400)#跑到上面改变位置
          
    def check_distance(self):#开始判断距离
        distance1 = self.turtle.distance(t1)
        distance2 = self.turtle.distance(t2)
        if distance1<25 or distance2<25:
            t.bye()#直接退出画布
        
        # 继续检查距
        t.ontimer(self.check_distance, 100)


def motion(x, y):##画笔跟随
    t1.goto(x - 300, -y + 310)
    t2.goto(-x + 300, -y + 310)
    if x - 300 < 0:#颜色改变
        t1.color('red')
        t2.color('green')
    elif x - 300 > 0:
        t2.color('red')
        t1.color('green')


def update_motion():
    x, y = screen.getcanvas().winfo_pointerxy()#这个用来找到鼠标的位置  这个自己查查
    motion(x - 330, y - 130)
    t.ontimer(update_motion, 50)######一系列的延迟方便图的刷新
    t.ontimer(hb.check_distance, 50)
    t.ontimer(tt.check_distance, 50)
    t.ontimer(hb1.check_distance, 50)
    t.ontimer(tt1.check_distance, 50)
    t.ontimer(hb2.check_distance, 50)
    t.ontimer(tt2.check_distance, 50)
    
####程序执行
hb = Falling(t3)
tt = Falling(t4)
hb1 = Falling(t5)
tt1= Falling(t6)
hb2 = Falling(t7)
tt2= Falling(t8)

hb1.start()
tt1.start()
hb2.start()
tt2.start()
hb.start()
tt.start()
update_motion()###重要  
t.mainloop()