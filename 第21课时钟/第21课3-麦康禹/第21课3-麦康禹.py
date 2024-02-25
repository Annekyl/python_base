from datetime import datetime as dt
import turtle as t

# 很奇怪,turtle指针旋转但图片并不会旋转
t1 = t.Turtle()
t.register_shape('1.gif')
t1.shape('1.gif')


# 定义一个类作为画笔
class Penx(t.Turtle):
    def _init_(self):
        t.Turtle._init_(self)

    def move_f(self, x, y):  # x是我们的指针长度，y是我们的旋转角度
        self.ht()
        self.seth(y + 90)
        self.pensize(10)
        self.fd(x * 34)
        self.home()


# ————模块化—————
def point():
    f = dt.now()
    sekunde = f.second + f.microsecond * 0.000001  # 秒针
    minute = f.minute + sekunde / 60.  # 分针
    stunde = f.hour + minute / 60.  # 时针
    t.tracer(0)
    t2.clear()
    t3.clear()
    t4.clear()
    t2.move_f(5, -6 * sekunde)  # 因为指针一开始都是默认向右的所以要加个90
    t3.move_f(3, -6 * minute)
    t4.move_f(2, -30 * stunde)
    t.tracer(1)
    t.ontimer(point, 100)  # 每过100毫秒就循环一次point函数


# ————主程序—————
t1 = Penx()  # 恒不变(或者长时间不变的量:钟框、数字等)
t2 = Penx()  # 秒针
t3 = Penx()  # 分针
t4 = Penx()  # 时针
t1.ht()
point()
t.mainloop()
