import turtle as t
import datetime as dt

class Pen1(t.Pen):
    def __init__(self):
        t.Pen.__init__(self)
    def shape(self,length,width,name):#自定义画笔
        t.reset()
        t.penup()
        t.begin_poly()
        t.fd(length*1)
        t.end_poly()
        t.register_shape(name,t.get_poly())
        hand=t.Pen()
        hand.shape(name)
        hand.shapesize(1,1,width)
        return hand

    def clock(self):#画钟
        t.tracer(False)
        self.pensize(10)
        self.penup()
        self.goto(0,-200)
        self.pendown()
        self.circle(200)
        self.pensize(5)
        self.ht()
        x=0
        y=90
        for i in range(61):
            self.penup()
            self.goto(0,0)
            self.seth(x)
            self.fd(190)
            self.pendown()
            self.fd(10)
            x+=6
        for i in range(12):
            i+=1
            y-=30
            self.penup()
            self.goto(0,0)
            self.seth(y)
            self.fd(220)
            self.pendown()
            self.write(i,align='center',font=('Courier',14,'bold'))
        t.tracer(True)
def time():
    global a,b,c
    tm=dt.datetime.today()#获取时间
    a=tm.strftime('%H')#时针
    b=tm.strftime('%M')#分针
    c=tm.strftime('%S')#秒针
    a=int(a)
    b=int(b)
    c=int(c)
    hour1.seth(180-((b/60+c/3600)*6)-a*30 )#确定角度
    hour2.seth(180-(c/60+b)*6)
    hour3.seth(180-c*6)
    t1.write(tm.strftime('%Y-%m-%d'),align='center',font=('Courier',14,'bold'))
    t.ontimer(time,1000)、
#————————主程序——————
t1=Pen1()
sp=Pen1()
hour1=sp.shape(100,7,'hour1')
hour2=sp.shape(140,7,'hour2')
hour3=sp.shape(170,7,'hour3')
t1.clock()
t1.penup()
t1.goto(0,250)
t1.pendown()
time()

