import turtle as t
import time
game=t.Screen()
game.title('走迷宫')
game.bgcolor('black')
game.setup(800,600)
t1=t.Pen()#计时器
t1.pencolor('yellow')
t1.penup()
t1.goto(400,400)  
t1.pendown()
t2=t.Pen()
t2.pencolor('yellow')
t2.penup()
t2.goto(400,350)
t2.pendown()
ball=t.Pen()
ball.color('white')
ball.shape('circle')
ball.penup()
ball.setx(-600)
ball.sety(0)
t.speed(0)
t1.ht()
t.ht()
t2.ht()
maze_boundaries = [
    (-600, 100, 20, 200),
    (-600, 300, 1200, 20),
    (-400, -200, 20, 500),
    (0, -200, 20, 500),
    (400, -200, 20, 500),
    (580, 100, 20, 200),
    (-600, -300, 20, 200),
    (-600, -300, 1200, 20),
    (-200, -300, 20, 500),
    (200, -300, 20, 500),
    (580, -300, 20, 200)
]
def create_maze():
    for boundary in maze_boundaries:
        x, y, m, n = boundary
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.color('yellow', 'yellow')
        for _ in range(2):
            t.fd(m)
            t.left(90)
            t.fd(n)
            t.left(90)
        t.end_fill()

def move_up():
    x, y = ball.xcor(), ball.ycor()
    ball.sety(ball.ycor()+5)
    check_collision()

    
def move_down():
    x, y = ball.xcor(), ball.ycor()
    ball.sety(ball.ycor()-5)
    check_collision()

def move_right():
    x, y = ball.xcor(), ball.ycor()
    ball.setx(ball.xcor()+5)
    check_collision()

def move_left():
    x, y = ball.xcor(), ball.ycor()
    ball.setx(ball.xcor()-5)
    check_collision()
    
def check_collision():
    x, y = ball.xcor(), ball.ycor()
    for boundary in maze_boundaries:
        x1, y1, w, h = boundary
        if x1-10 <= x <= x1 + w+10 and y1 - 10 <= y <= y1 + h + 10:
            ball.goto(-600, 0)

def begin():
    game.listen()
    game.onkeypress(move_up,'Up')
    game.onkeypress(move_down,'Down')
    game.onkeypress(move_right,'Right')
    game.onkeypress(move_left,'Left')

second=0.00
while(1):
    k=0
    second+=0.06
    create_maze()
    begin()
    t1.write('计时器',font=('楷书',50))
    t2.write('{:.2f}'.format(second),font=('楷书',20))
    time.sleep(0.01)
    t2.clear()
    
