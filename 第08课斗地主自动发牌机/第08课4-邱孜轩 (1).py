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
    ch1,ch2,ch3,ch4,"",""]

pk=['A','A','A','A','2','2','2','2','3','3','3','3','4','4','4','4',
    '5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8',
    '9','9','9','9','10','10','10','10','J','J','J','J','Q','Q','Q','Q',
    'K','K','K','K','J\nO\nK\nE\nR','J\nO\nK\nE\nR']

tl.tracer(False)
tl.hideturtle()
tl.bgcolor('grey')

tl.pensize(2)

def pkp(x,y,z):
    tl.penup()
    tl.goto(x,y)
    tl.seth(0)
    tl.pendown()
    tl.color('black','white')
    tl.begin_fill()
    for i in range(2):
        tl.forward(70)
        tl.left(90)
        tl.forward(120)
        tl.left(90)
    tl.end_fill()
    tl.penup()
    tl.goto(x+3,y+65)
    tl.seth(0)
    tl.pendown()
    tl.pencolor(ys[z])
    tl.write(hs[z],font=("黑体",20,"normal"))
    if(pk[z]=='J\nO\nK\nE\nR'): 
        tl.penup()
        tl.goto(x+7,y)
        tl.seth(0)
        tl.pendown()
        tl.write(pk[z],font=("黑体",18,"normal"))
    else:
        tl.penup()
        tl.goto(x+7,y+85)
        tl.seth(0)
        tl.pendown()
        tl.write(pk[z],font=("黑体",25,"normal"))
    tl.penup()
    tl.goto(x+13,y+30)
    tl.seth(0)
    tl.pendown()
    tl.pencolor(ys[z])
    tl.write(hs[z],font=("黑体",60,"normal"))
    

for i in range(17):
    a=rd.randint(0,53-i)
    if(i<=9):
        pkp(-700+40*i,200,a)
        del pk[a]
        del hs[a]
        del ys[a]
    else:
        pkp(-700+40*(i-10),140,a)
        del pk[a]
        del hs[a]
        del ys[a]


for i in range(17):
    a=rd.randint(0,53-17-i)
    if(i<=9):
        pkp(0+40*i,200,a)
        del pk[a]
        del hs[a]
        del ys[a]
    else:
        pkp(0+40*(i-7),140,a)
        del pk[a]
        del hs[a]
        del ys[a]


for i in range(20):
    a=rd.randint(0,53-34-i)
    pkp(-500+40*i,-150,a)
    del pk[a]
    del hs[a]
    del ys[a]
turtle.mainloop()