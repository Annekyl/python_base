import turtle
import turtle as tl
import random as rd
pk=['红心A','黑桃A','梅花A','方片A','红心2','黑桃2','梅花2','方片2',
    '红心3','黑桃3','梅花3','方片3','红心4','黑桃4','梅花4','方片4',
    '红心5','黑桃5','梅花5','方片5','红心6','黑桃6','梅花6','方片6',
    '红心7','黑桃7','梅花7','方片7','红心8','黑桃8','梅花8','方片8',
    '红心9','黑桃9','梅花9','方片9','红心10','黑桃10','梅花10','方片10',
    '红心J','黑桃J','梅花J','方片J','红心Q','黑桃Q','梅花Q','方片Q',
    '红心K','黑桃K','梅花K','方片K','大王','小王']

tl.tracer(False)
tl.pencolor('black')
tl.pensize(2)

def pkp(x,y,z):
    tl.penup()
    tl.goto(x,y)
    tl.seth(0)
    tl.pendown()
    for i in range(2):
        tl.forward(70)
        tl.left(90)
        tl.forward(120)
        tl.left(90)
    tl.penup()
    tl.goto(x+5,y+50)
    tl.seth(0)
    tl.pendown()
    tl.write(pk[z],font=("黑体",18,"normal"))


for i in range(17):
    a=rd.randint(0,53-i)
    pkp(-700+80*i,200,a)
    del pk[a]


for i in range(17):
    a=rd.randint(0,53-17-i)
    pkp(-700+80*i,50,a)
    del pk[a]


for i in range(20):
    a=rd.randint(0,53-34-i)
    pkp(-800+80*i,-150,a)
    del pk[a]
turtle.mainloop()