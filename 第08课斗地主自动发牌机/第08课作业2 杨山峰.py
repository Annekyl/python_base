import random
import turtle as t

t.hideturtle()
t.pensize(1)
t.speed(0)
t.color("black")
t.tracer(False)


def card(x, y, name):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(0)
    t.forward(45.6)
    t.right(90)
    t.forward(70.4)
    t.right(90)
    t.forward(45.6)
    t.right(90)
    t.forward(40.4)
    t.write(name, font=("微软雅黑", 12, "normal"))
    t.forward(30)


pk = ["红心A", "红心2", '红心3', '红心4', '红心5', '红心6', '红心7', '红心8', '红心9', '红心10',
      '红心J', '红心Q', '红心K', '方块A', '方块2', '方块3', '方块4', '方块5', '方块6',
      '方块7', '方块8', '方块9', '方块10', '方块J', '方块Q', '方块K', '黑桃A', '黑桃2',
      '黑桃3', '黑桃4', '黑桃5', '黑桃6', '黑桃7', '黑桃8', '黑桃9', '黑桃10', '黑桃J', '黑桃Q',
      '黑桃K', '梅花A', '梅花2', '梅花3', '梅花4', '梅花5', '梅花6', '梅花7', '梅花8', '梅花9',
      '梅花10', '梅花J', '梅花Q', '梅花K', '大王', '小王']
dz = []
nm1 = []
nm2 = []
# 每人先发出17张牌
for piece in range(20):
    list_num = random.randint(0, 53 - piece)  #
    dz.append(pk[list_num])  # 追加给人
    del pk[list_num]  # 删除牌库中对应的牌

for piece in range(17):  # 每人先发17张
    list_num = random.randint(0, 53 - piece - 20)  #
    nm1.append(pk[list_num])  # 追加给人
    del pk[list_num]  # 删除牌库中对应的牌

for piece in range(17):  # 每人先发17张
    list_num = random.randint(0, 53 - piece - 20 - 17)  #
    nm2.append(pk[list_num])  # 追加给人
    del pk[list_num]  # 删除牌库中对应的牌

m = -430
for i in range(20):
    list_one = dz[i]
    card(m, 300, list_one)
    m += 50

m = -400
for i in range(17):
    list_one = nm1[i]
    card(m, 0, list_one)
    m += 50

m = -400
for i in range(17):
    list_one = nm2[i]
    card(m, -100, list_one)
    m += 50
t.tracer(True)
t.mainloop()
