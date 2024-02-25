import turtle as t
import datetime as dt
import threading
R = t.Screen()
tm=dt.datetime.today()
t4=t.Pen()
t4.hideturtle()
an1=(int(tm.strftime('%S'))/60)*360
an2=(int(tm.strftime('%M'))/60)*360
an3=(int(tm.strftime('%H'))/12)*360

class Penx(t.Pen):
    global an1
    global an2
    global an3
    def draw(self,length,width,long,color2,name1):
        self.reset()
        t.tracer(False)
        self.hideturtle()
        self.color(color2)
        self.begin_poly()#画图部分,用参数搞定它
        self.pensize(width)
        self.begin_fill()
        self.fd(length)
        self.seth(90)
        self.fd(long/2)
        self.rt(120)
        self.fd(long)
        self.rt(120)
        self.fd(long)
        self.rt(120)
        self.fd(long/2)
        self.end_fill()        
        self.end_poly()
        t.tracer(True)
        t.register_shape(name1,self.get_poly())
        self.clear()
        hand=t.Pen()
        hand.shape(name1)
        hand.color(color2)
        hand.shapesize(1,1,width)
        return hand
def auto_renew1():
    global an1
    t.tracer(False)
    s_a.seth(180-an1)
    t.tracer(True)
    an1+=6
    t.ontimer(auto_renew1,1000)
def auto_renew2():
    global an2
    t.tracer(False)
    s_b.seth(180-an2)
    t.tracer(True)
    an2+=0.1
    t.ontimer(auto_renew2,1000)
def auto_renew3():
    global an3
    t.tracer(False)
    s_c.seth(180-an3)
    t.tracer(True)
    an3-=0.1/60
    t.ontimer(auto_renew3,1000)

def jump(distanz, winkel=0):
    t4.penup()
    t4.right(winkel)
    t4.forward(distanz)
    t4.left(winkel)
    t4.pendown()
def clockface(radius):
    t.tracer(False)
    t4.reset()
    t4.pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            t4.fd(25)
            jump(-radius-25)
        else:
            t4.dot(3)
            jump(-radius)
        t4.rt(6)
    t.tracer(True)   
#-----------------------------主程序-----------------------------------    
s_a=Penx().draw(150,5,30,'red','s_a')

s_b=Penx().draw(120,5,30,'blue','s_b')

s_c=Penx().draw(90,5,30,'green','s_c')

clockface(180)
pen1 = threading.Thread(target=auto_renew1)
pen1.start()
pen2 = threading.Thread(target=auto_renew2)
pen2.start()
pen3 = threading.Thread(target=auto_renew3)
pen3.start()
R.mainloop()
