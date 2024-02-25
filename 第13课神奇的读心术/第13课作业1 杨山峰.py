import turtle as t
import time

t.hideturtle()


def p(x, y):
    global k
    k = 1


k = 0  # 屏幕检测
num = 0  # 起始数字
add = 0.04  # 每次递增0.04
while 1:
    num += add
    t.write("{:.2f}".format(num), font=("华文仿宋", 50, "normal"))
    t.onscreenclick(p)
    if k == 1:  # 判断是否点击
        break
    time.sleep(0.01)  # 画面停留0.01秒
    t.clear()  # 清空画面
t.mainloop()
