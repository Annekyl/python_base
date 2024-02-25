import turtle

turtle.shape("turtle")
turtle.penup()


def motion(event):
    x, y = event.x, event.y
    turtle.goto(x-430, y-404)
    print(f"鼠标位置：{x}, {y}")


screen = turtle.Screen()
canvas = screen.getcanvas()
canvas.bind('<Motion>', motion)  # <Motion> 是 Tkinter 中用于表示鼠标移动的事件类型的标准字符串,将鼠标移动事件（<Motion>）与一个名为 motion 的函数绑定在一起

screen.mainloop()
