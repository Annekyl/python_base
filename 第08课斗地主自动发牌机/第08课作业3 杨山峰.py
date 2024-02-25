import random
import turtle as t

t.tracer(False)
t.hideturtle()
ch1 = '\u2665'
ch2 = '\u2660'
ch3 = '\u2666'
ch4 = '\u2663'


def card(x, y, name, color, fill):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(fill)
    t.seth(0)
    t.forward(45.6)
    t.right(90)
    t.forward(70.4)
    t.right(90)
    t.forward(45.6)
    t.right(90)
    t.forward(20.4)
    t.write(color, font=("微软雅黑", 12, "normal"))
    t.forward(20)
    t.write(name, font=("微软雅黑", 12, "normal"))
    t.forward(30)


pk = ["A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      "A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      "A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      "A", "2", '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
      '大', '小']
color = [ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1, ch1,
         ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2, ch2,
         ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3, ch3,
         ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4, ch4,
         "王", "王"]
fill = ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red",
        "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black",
        "black",
        "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red", "red",
        "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black",
        "black", "red", "red"]
dz_p = []
dz_c = []
dz_fill = []
nm1_p = []
nm1_c = []
nm1_fill = []
nm2_p = []
nm2_c = []
nm2_fill = []
# 每人先发出17张牌
for piece in range(20):
    list_num = random.randint(0, 53 - piece)  #
    dz_p.append(pk[list_num])  # 追加给人
    dz_c.append(color[list_num])
    dz_fill.append(fill[list_num])
    del pk[list_num]  # 删除牌库中对应的牌
    del color[list_num]
    del fill[list_num]

for piece in range(17):  # 每人先发17张
    list_num = random.randint(0, 53 - piece - 20)  #
    nm1_p.append(pk[list_num])  # 追加给人
    nm1_fill.append(fill[list_num])
    nm1_c.append(color[list_num])
    del pk[list_num]  # 删除牌库中对应的牌
    del color[list_num]
    del fill[list_num]

for piece in range(17):  # 每人先发17张
    list_num = random.randint(0, 53 - piece - 20 - 17)  #
    nm2_p.append(pk[list_num])  # 追加给人
    nm2_fill.append(fill[list_num])
    nm2_c.append(color[list_num])
    del pk[list_num]  # 删除牌库中对应的牌
    del color[list_num]
    del fill[list_num]

m = -430
for i in range(20):
    p = dz_p[i]
    c = dz_c[i]
    f = dz_fill[i]
    card(m, 300, p, c, f)
    m += 50

m = -400
for i in range(17):
    p = nm1_p[i]
    c = nm1_c[i]
    f = nm1_fill[i]
    card(m, 0, p, c, f)
    m += 50

m = -400
for i in range(17):
    p = nm2_p[i]
    c = nm2_c[i]
    f = nm2_fill[i]
    card(m, -100, p, c, f)
    m += 50
t.tracer(True)
t.mainloop()
