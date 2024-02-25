from turtle import *
from time import *
from random import *

ls=['\u264B','\u2648','\u2649','\u264F','\u264E','\u264A','\u264D','\u2653','\u264C','\u264F','\u2648','\u2649']

def p(x,y):
    global k
    k=1


bgcolor("grey")
t1=Pen()
t1.hideturtle()
hideturtle()
tracer(0)
pu()
k=0


a=randint(0,11)
for b in range(10):
    for i in range(10):
        if((10*b+i)%9==0):
            goto(50*i-95,50*b-100)
            write(10*b+i,font=('楷体',15))
            goto(50*i-100,50*b-80)
            write(ls[a],font=('楷体',20))
        else:
            c=randint(0,11)
            goto(50*i-95,50*b-100)
            write(10*b+i,font=('楷体',15))
            goto(50*i-100,50*b-80)
            write(ls[c],font=('楷体',20))
            
onscreenclick(p)

while(True):
    goto(-600,-100)
    write("在心中默想一个数字\n先将此数字减去他的个位数\n再将其减去十位数",font=('楷体',25))
    goto(-400,100)
    pd()
    color("blue","blue")
    begin_fill()
    circle(150)
    end_fill()
    pu()
    if k==1:
        t1.pu()
        t1.pencolor("red")
        t1.goto(-475,175)
        t1.write(ls[a],font=('楷体',120))
