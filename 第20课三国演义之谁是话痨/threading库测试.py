import threading
import turtle

t1 = turtle.Turtle()
# t1.pu()
t2 = turtle.Turtle()
# t2.pu()

# t2.goto(0, -200)
# t2.pd()
# t2.right(60)
# t1.goto(0, 200)
# t1.pd()

def qianjin():
    t1.fd(500)
    t1.pu()


def right():
    t2.fd(500)


threading1 = threading.Thread(target=qianjin())
threading2 = threading.Thread(target=right())
threading1.start()
threading2.start()
