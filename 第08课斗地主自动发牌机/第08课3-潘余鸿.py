import random as r
import turtle as t
t.tracer(False)
t.bgcolor('blue')

ch1='\u2665'    #红心
ch2='\u2660'    #黑桃
ch3='\u2666'    #方块    
ch4='\u2663'    #梅花

pk=['\u2665','\u2665','\u2665','\u2665','\u2665','\u2665','\u2665','\u2665', \
    '\u2665','\u2665','\u2665','\u2665','\u2665','', \
    '\u2666','\u2666','\u2666', \
    '\u2666','\u2666','\u2666','\u2666','\u2666','\u2666','\u2666','\u2666', \
    '\u2666','\u2666', \
    '\u2660','\u2660','\u2660','\u2660','\u2660', \
    '\u2660','\u2660','\u2660','\u2660','\u2660','\u2660','\u2660','\u2660', \
    '\u2663','\u2663','\u2663','\u2663','\u2663','\u2663','\u2663', \
    '\u2663','\u2663','\u2663','\u2663','\u2663','\u2663','']

pk2=['A','2','3','4','5','6','7','8', \
    '9','10','J','Q','K','J\nO\nK\nE\nR','A','2','3', \
    '4','5','6','7','8','9','10','J', \
    'Q','K','A','2','3','4','5', \
    '6','7','8','9','10','J','Q','K', \
    'A','2','3','4','5','6','7', \
    '8','9','10','J','Q','K','J\nO\nK\nE\nR']

color=['red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red', \
       'black','black','black','black','black','black','black','black','black','black','black','black', \
       'black','black','black','black','black','black','black','black','black','black','black','black','black','black','black',]


nong1=[]
nong2=[]
di=[]


def square(x,y,z,z1):
    t.color('black','white')
    t.begin_fill()
    t.pu()
    t.goto(x,y)
    t.seth(0)
    t.pd()
    for i in range(2):
        t.fd(60)
        t.rt(90)
        t.fd(90)
        t.rt(90)
    t.end_fill()
    t.pu()
    if(z1=='J\nO\nK\nE\nR'):                        #为大小王定制位置和字体大小
        t.goto(x+3,y-92)
        t.pencolor(color[a])
        t.write(z1,font=("微软雅黑",10,"normal"))
    else:
        t.goto(x+3,y-21)
        t.pencolor(color[a])
        t.write(z1,font=("微软雅黑",13,"normal"))
    t.pu()
    t.goto(x+6,y-85)
    t.pencolor(color[a])
    t.write(z,font=("微软雅黑",50,"normal"))
    t.pu()
    t.goto(x+1,y-35)
    t.pencolor(color[a])
    t.write(z,font=("微软雅黑",15,"normal"))

for i in range(0,50,3):
    a=r.randint(0,50-i)
    nong1.append(pk[a])
    square(15*i-450,300,pk[a],pk2[a])
    del pk[a]
    del pk2[a]
    del color[a]
    a=r.randint(0,49-i)
    nong2.append(pk[a])
    square(15*i-450,100,pk[a],pk2[a])
    del pk[a]
    del pk2[a]
    del color[a]
    a=r.randint(0,48-i)
    di.append(pk[a])
    square(15*i-580,-100,pk[a],pk2[a])
    del pk[a]
    del pk2[a]
    del color[a]
for i in range(0,3):
    a=r.randint(0,2-i)
    di.append(pk[a])
    square(185+40*i,-100,pk[a],pk2[a])
    del pk[a]
    del pk2[a]
    del color[a]



print("农民1：",nong1)
print("农民2：",nong2)
print("地主：",di)
