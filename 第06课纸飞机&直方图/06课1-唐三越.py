#-----------------------引入数据库----------------
import turtle as t

t.pensize(5)
t.speed(100)
t.hideturtle()
#------------------------定义函数------------------
def straw_tri(x1,y1,x2,y2,x3,y3):#画三角
    t.begin_fill()
    t.penup()
    t.color('black','blue')
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x1,y1)
    t.end_fill()

def draw_line(x1,y1,x2,y2):#画线
    t.penup()
    t.color('black')
    t.goto(x1,y1)
    t.pendown()
    t.goto(x2,y2)
    
#------------------------------数据库--------------------
tri_1=[[-300,150],[-125,-125],[-50,-50]]#三角
tri_2=[[-300,150],[0,0],[100,50]]
tri_3=[[-50,-50],[-85,-85],[-30,-125]]

line_1=[[-80,-125],[120,-200]]#线
line_2=[[10,-80],[100,-150]]
line_3=[[50,-5],[250,-30]]
line_4=[[75,25],[200,0]]
line_5=[[-30,-125],[0,0]]
#-----------------------------开画-----------------------------
straw_tri(tri_1[0][0],tri_1[0][1],tri_1[1][0],tri_1[1][1],tri_1[2][0],tri_1[2][1])#画三角
straw_tri(tri_2[0][0],tri_2[0][1],tri_2[1][0],tri_2[1][1],tri_2[2][0],tri_2[2][1])
straw_tri(tri_3[0][0],tri_3[0][1],tri_3[1][0],tri_3[1][1],tri_3[2][0],tri_3[2][1])

draw_line(line_1[0][0],line_1[0][1],line_1[1][0],line_1[1][1])#画线
draw_line(line_2[0][0],line_2[0][1],line_2[1][0],line_2[1][1])
draw_line(line_3[0][0],line_3[0][1],line_3[1][0],line_3[1][1])
draw_line(line_4[0][0],line_4[0][1],line_4[1][0],line_4[1][1])
draw_line(line_5[0][0],line_5[0][1],line_5[1][0],line_5[1][1])

t.penup()
t.begin_fill()
t.goto(250,200)
t.pendown()
t.color('red','red')
t.circle(50,360)
t.end_fill()
t.mainloop()