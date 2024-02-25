# 下面是使用Python的Turtle库绘制一个时钟的示例代码。在这个示例中，我们使用图片作为时钟的指针，同时美化时钟面板的刻度。
import turtle

# 创建一个窗口和画布
window = turtle.Screen()
window.title("时钟")
window.bgcolor("white")

canvas = turtle.Turtle()
canvas.hideturtle()
canvas.speed(0)
canvas.penup()

# 绘制时钟面板外圈
canvas.goto(0, -200)
canvas.pendown()
canvas.circle(200)

# 绘制时钟面板刻度
canvas.penup()
canvas.goto(0, 0)
for i in range(12):
    canvas.forward(160)
    canvas.pendown()
    canvas.forward(20)
    canvas.penup()
    canvas.goto(0, 0)
    canvas.right(30)

# 加载时钟指针图片
turtle.register_shape("hour_hand.gif")
turtle.register_shape("minute_hand.gif")
turtle.register_shape("second_hand.gif")

# 绘制时钟指针
hour_hand = turtle.Turtle()
hour_hand.shape("hour_hand.gif")
hour_hand.penup()
hour_hand.speed(1)

minute_hand = turtle.Turtle()
minute_hand.shape("minute_hand.gif")
minute_hand.penup()
minute_hand.speed(1)

second_hand = turtle.Turtle()
second_hand.shape("second_hand.gif")
second_hand.penup()
second_hand.speed(1)


# 更新时钟指针位置
def update_clock():
    import time
    t = time.localtime()
    hour = t.tm_hour % 12
    minute = t.tm_min
    second = t.tm_sec

    hour_hand.setheading(-30 * hour - 30 * (minute / 60))
    minute_hand.setheading(-6 * minute)
    second_hand.setheading(-6 * second)

    turtle.ontimer(update_clock, 1000)


update_clock()

# 运行绘制
turtle.done()
