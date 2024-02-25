import datetime as dt
import turtle as t

t1=t.Pen()
t2=t.Pen()
t3=t.Pen()
t4=t.Pen()
t5=t.Pen()
t.tracer(0)
t1.pensize(3)
t2.pensize(3)
t3.pensize(6)
t4.pensize(9)
t1.hideturtle()
t3.hideturtle()
t4.hideturtle()
t5.hideturtle()
for i in range(17):
    t1.left(90)
    t1.fd(10)
    t1.left(180)
    t1.fd(10)
    t1.left(90)
    t1.circle(100,30)
t1.penup()
t1.goto(-35,50)
t5.penup()
t5.goto(-20,150)
while 1:
    ma=dt.datetime.today()
    mb=ma.strftime('%S')
    mc=ma.strftime('%M')
    md=ma.strftime('%H')
    t1.write(ma.strftime('%Y-%m-%d'),font=('楷体',10))
    t5.write(ma.strftime('%A'),font=('楷体',10))
    t2.penup()
    t2.goto(0,100)#秒针
    t2.seth(90-int(mb)*6)
    t2.pendown()
    t2.clear()
    t2.fd(80)
    t3.penup()
    t3.goto(0,100)#分针
    t3.seth(90-int(mc)*6)
    t3.pendown()
    t3.clear()
    t3.fd(70)
    t4.penup()
    t4.goto(0,100)#分针
    t4.seth(90-int(md)*30)
    t4.pendown()
    t4.clear()
    t4.fd(50)    
    t.update()
    
    

    
