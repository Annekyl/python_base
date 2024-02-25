import random as r
import turtle as t
#———————————————————————————————————————————————————————————————引入turtle和random库，并简单定义为首字母，方便输出
library1 = ['\u2665','\u2665','\u2665','\u2665','\u2665','\u2665','\u2665','\u2665','\u2665','\u2665','\u2665','\u2665','\u2665', \
           '\u2660','\u2660','\u2660','\u2660','\u2660','\u2660','\u2660','\u2660','\u2660','\u2660','\u2660','\u2660','\u2660', \
           '\u2666','\u2666','\u2666','\u2666','\u2666','\u2666','\u2666','\u2666','\u2666','\u2666','\u2666','\u2666','\u2666', \
           '\u2663','\u2663','\u2663','\u2663','\u2663','\u2663','\u2663','\u2663','\u2663','\u2663','\u2663','\u2663','\u2663', \
           '','']

library2 = ['A','2','3','4','5','6','7','8','9','10','J','Q','K', \
           'A','2','3','4','5','6','7','8','9','10','J','Q','K', \
           'A','2','3','4','5','6','7','8','9','10','J','Q','K', \
           'A','2','3','4','5','6','7','8','9','10','J','Q','K', \
           'J\nO\nK\nE\nR','J\nO\nK\nE\nR']

color = ['red','red','red','red','red','red','red','red','red','red','red','red','red', \
           'black','black','black','black','black','black','black','black','black','black','black','black','black', \
           'red','red','red','red','red','red','red','red','red','red','red','red','red', \
           'black','black','black','black','black','black','black','black','black','black','black','black','black', \
           'black','red']
#u2665红心 u2660黑桃 u2666方块 u2663
#———————————————————————————————————————————————————————————————定义牌的花型，颜色，与数字，分别对应
t.tracer(0)
t.ht()  #隐藏箭头
t.bgcolor('grey')
#———————————————————————————————————————————————————————————————画图前置工作，一键出图，隐藏箭头，设定背景颜色
def board(x):
        t.seth(90)
        t.color("black","white")
        t.begin_fill()
        for i in range(2):
            t.fd(40)
            t.right(90)
            t.fd(50)
            t.right(90)
            t.fd(40)
        t.end_fill()
#———————————————————————————————————————————————————————————————画方框,黑框白底
        a = r.randint(0,53-j-17*x)          #从牌库中挑选，这里所选择的a代表这上面的一一组合
        t.pencolor(color[a])
#定义颜色，红心为红色，黑桃为黑色
        t.pu()
        t.seth(90)
        t.fd(20)
        t.pd()              #移动开始绘画花型
        t.write(library1[a],font=('楷书',12,'normal'))
#绘制花型        
        t.pu()
        t.seth(-90)
        t.fd(14)
        t.seth(0)
        t.fd(2)
        t.pd()               #移动开始绘画数字和大小王
        if (library2[a]=='J\nO\nK\nE\nR'):
            t.pu()
            t.seth(-90)
            t.fd(35)
            t.pd()
            t.write(library2[a],font=('楷书',10,'normal'))        #因为大小王占位置很大，所以要单独设置
        else:
            t.write(library2[a],font=('楷书',12,'normal'))
#绘制数字
        del library1[a]
        del library2[a]
        del color[a]
#删除已用过的组合
def move(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
#定义移动
#————————————————————————————————————————————————————————————————主程序
for j in range(17):
    move(-400+j*15,120)
    board(0)
for j in range(17):
    move(100+j*15,120)
    board(1)
for j in range(20):
    move(-200+j*15,-100)
    board(2)
#————————————————————————————————————————————————————————————————
t.tracer(1)
#结束，tracer(1)显示线段
t.mainloop()