from turtle import *  
from datetime import *
import threading
  
t1 = Pen()                                 
time = datetime.today()  
s = 360 * (int(time.strftime('%S')) / 60)  
m = 360 * (int(time.strftime('%M')) / 60)  
h = 360 * (int(time.strftime('%H')) / 12)  
  
def biaopan(r):                       
    t1.ht()  
    tracer(0)  
    for i in range(60):  
        t1.pu()  
        t1.fd(r)  
        t1.pd()  
        if i % 5 == 0:                         
            t1.pensize(5)  
            t1.fd(20)  
        else:  
            t1.pensize(1)  
            t1.fd(5)  
        t1.rt(6)  
        t1.pu()  
        t1.goto(0, 0)  
        t1.pd()  
    tracer(1)  
  
def zhizhen(leng, wide, colors, name):    
    reset()                                 
    begin_poly()                          
    tracer(0)  
    fd(leng)  
    tracer(1)  
    ht()  
    end_poly()                            
    register_shape(name, get_poly())  
    clear()  
    hand = Pen()  
    hand.color(colors)               
    hand.shape(name)  
    hand.shapesize(1, 1, wide)  
    return hand  
  
def hour():                               
    global h  
    tracer(0)  
    hr.seth(180 - h)  
    tracer(1)  
    h += 6 / 3600  
    ontimer(hour, 1000)  
def minute():  
    global m  
    tracer(0)  
    me.seth(180 - m)  
    tracer(1)  
    m += 6 / 60  
    ontimer(minute, 1000)  
def second():  
    global s  
    tracer(0)  
    sd.seth(180 - s)  
    tracer(1)  
    s += 6  
    ontimer(second, 1000)  
  
biaopan(150)   
hr=zhizhen(90,11,'black',"hr")
me=zhizhen(110,9,'black',"me")
sd=zhizhen(130,7,'black',"sd")

a=5
hour()
minute()
second()
done()
