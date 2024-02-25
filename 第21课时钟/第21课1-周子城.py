import datetime as d
import turtle as t

for i in range(60):
    t.tracer(False)
    t2=t.Pen()
    t2.hideturtle()
    t2.seth(i*6)
    t2.pensize(5)
    t2.pu()
    t2.fd(150)
    t2.pd()
    t2.fd(5)
    t2.pu()
    t2.goto(0,0)
    t.tracer(True)

for i in range(12):
    t.tracer(False)
    t3=t.Pen()
    t3.hideturtle()
    t3.color('red')
    t3.seth(i*30)
    t3.pensize(6)
    t3.pu()
    t3.fd(150)
    t3.pd()
    t3.fd(20)
    t3.pu()
    t3.goto(0,0)
    t.tracer(True)

def setting(length,width,name):
    t.reset()
    t.pu()
    t.begin_poly()
    t.tracer(False)
    t.hideturtle()
    t.fd(length*1.1)
    t.tracer(True)
    t.end_poly()
    t.register_shape(name,t.get_poly())
    hand=t.Pen()
    hand.shape(name)
    hand.shapesize(1,1,width)
    return hand

def tm():
    tm=d.datetime.today()
    t1.clear()
    t1.goto(0,-200)
    t1.write(tm.strftime('%Y-%m-%d'),align='center',font=('Courier',14,'bold'))


def hourr():
    global an
    t.tracer(False)
    second.seth(180-an)
    t.tracer(True)
    an+=6
    t.ontimer(hourr,1000)

def sp():
    global bn
    t.tracer(False)
    minute.seth(180-bn)
    t.tracer(True)
    bn+=0.1
    t.ontimer(sp,1000)

def ls():
    global cn
    t.tracer(False)
    hour.seth(180-cn)
    t.tracer(True)
    cn-=0.5/60
    t.ontimer(ls,1000)

tm1=d.datetime.today()    
an=(int(tm1.strftime('%S'))/60)*360
bn=(int(tm1.strftime('%M'))/60)*360
cn=(int(tm1.strftime('%H'))/12)*360+(int(tm1.strftime('%M'))/60)*30
second=setting(130,6,'second')
hourr()
minute=setting(110,6,'minute')
sp()
hour=setting(90,6,'hour')
ls()
t1=t.Pen()
t1.hideturtle()
t1.pu()
tm()

t.mainloop()
