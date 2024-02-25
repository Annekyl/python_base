# 测试鼠标右击
from turtle import *


def skip(x, y):
    up()
    goto(x, y)
    down()


shape('circle')
# onscreenclick(goto)
onscreenclick(skip, btn=3)
listen()
done()
