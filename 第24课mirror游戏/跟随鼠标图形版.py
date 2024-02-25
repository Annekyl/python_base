import turtle

# 初始化turtle
t = turtle.Turtle()
t.speed(0)  # 设置速度为最快


# 定义一个函数，用于将画笔移动到指定位置并返回对象
def move_turtle(x, y):
    t.ondrag(None)  # 暂时取消事件绑定，避免拖动鼠标时重复触发
    t.goto(x, y)
    t.ondrag(move_turtle)  # 重新绑定事件
    return None


# 绑定鼠标拖动事件
turtle.onscreenclick(move_turtle)

# 运行主循环
turtle.mainloop()
