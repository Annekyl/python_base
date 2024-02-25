import turtle
import turtle as tl
import random as rd

ch1='\u2665'
ch2='\u2660'
ch3='\u2666'
ch4='\u2663'

ys=["red","black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black","red","black","red","black","red","black","red","black","red",
    "black","red","black"]

hs=[ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,
    ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,
    ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,ch1,ch2,ch3,ch4,
    ch1,ch2,ch3,ch4,"大","小"]

pk=['A','A','A','A','2','2','2','2','3','3','3','3','4','4','4','4',
    '5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8',
    '9','9','9','9','10','10','10','10','J','J','J','J','Q','Q','Q','Q',
    'K','K','K','K','王','王']

tl.tracer(False)

tl.pensize(2)

def pkp(x,y,z):
    tl.penup()
    tl.goto(x,y)
    tl.seth(0)
    tl.pendown()
    tl.pencolor('black')
    for i in range(2):
        tl.forward(70)
        tl.left(90)
        tl.forward(120)
        tl.left(90)
    tl.penup()
    tl.goto(x+5,y+50)
    tl.seth(0)
    tl.pendown()
    tl.pencolor(ys[z])
    tl.write(hs[z],font=("黑体",18,"normal"))
    tl.penup()
    tl.goto(x+25,y+50)
    tl.seth(0)
    tl.pendown()
    tl.write(pk[z],font=("黑体",18,"normal"))   
    


for i in range(17):
    a=rd.randint(0,53-i)
    pkp(-700+80*i,200,a)
    del pk[a]
    del hs[a]
    del ys[a]


for i in range(17):
    a=rd.randint(0,53-17-i)
    pkp(-700+80*i,50,a)
    del pk[a]
    del hs[a]
    del ys[a]


for i in range(20):
    a=rd.randint(0,53-34-i)
    pkp(-800+80*i,-150,a)
    del pk[a]
    del hs[a]
    del ys[a]
turtle.mainloop()
