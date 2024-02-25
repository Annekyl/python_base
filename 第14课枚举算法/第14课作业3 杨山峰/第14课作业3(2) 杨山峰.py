import turtle

axis = [[-300, 200], [-300, 0], [-300, -200], [300, 200], [300, 0], [300, -200]]
wolf = turtle.Turtle()  # 狼
sheep = turtle.Turtle()  # 羊
food = turtle.Turtle()  # 菜
turtle.hideturtle()
print(turtle.getshapes())
turtle.register_shape("狼.gif")
turtle.register_shape("羊.gif")
turtle.register_shape("菜.gif")
wolf.shape("狼.gif")
sheep.shape("羊.gif")
food.shape("菜.gif")
print(turtle.shape())
wolf.pu()
sheep.pu()
food.pu()
wolf.goto(axis[0][0], axis[0][1])
sheep.goto(axis[1][0], axis[1][1])
food.goto(axis[2][0], axis[2][1])
name = ['猎人', '狼', '羊', '菜']
num = 0


def judge(position):  # 用于判断移动后是否符合要求
    if position[1] == position[2] and position[0] != position[1]:  # 狼和羊在同一边并且人不在
        # print("狼吃羊")
        return False
    elif position[2] == position[3] and position[0] != position[2]:  # 羊和菜在同一边并且人不在
        # print("羊吃菜")
        return False
    else:
        return True


def search_all_next_position(position):  # 找到下一步移动的全部情况
    next_position_list = []  # 将情况统计在同一个列表中
    for i in range(0, 4):  # 循环遍历全部方法
        if position[0] != position[i]:  # 位置不同，不能带走，跳过当前循环
            continue
        next_position = [not position[0], position[1], position[2], position[3]]  # 反转船的位置
        if i != 0:  # 如果船带走一样物品，物品也需要反转
            next_position[i] = next_position[0]
        if judge(next_position):  # 判断是否符合要求
            next_position_list.append(next_position)  # 追加到总情况中
    return next_position_list  # 返回全部情况


def show_position(position, bull):
    """
    将物品分到两岸
    :param position:全部物体的位置
    :param bull: 通过布尔类型来分开
    :return: 返回分开后的结果
    """
    result = ""
    for i in range(4):
        if position[i] == bull:
            if len(result) != 0:
                result += ","
            result += name[i]

    return '[' + result + ']'


def is_finish(position):  # 用于判断是否完成目的
    return position[0] and position[1] and position[2] and position[3]


def draw_picture(position):
    if position[1]:
        wolf.goto(axis[3][0], axis[3][1])
    if not position[1]:
        wolf.goto(axis[0][0], axis[0][1])
    if position[2]:
        sheep.goto(axis[4][0], axis[4][1])
    if not position[2]:
        sheep.goto(axis[1][0], axis[1][1])
    if position[3]:
        food.goto(axis[5][0], axis[5][1])
    if not position[3]:
        food.goto(axis[2][0], axis[2][1])


def search(all_position):
    global num
    current_position = all_position[len(all_position) - 1]
    next_position_list = search_all_next_position(current_position)

    for next_position in next_position_list:  # 循环遍历所有可能的步骤
        if next_position in all_position:  # 将重复的跳过
            continue
        all_position.append(next_position)  # 将本次的位置加入位置过程统计列表中

        if is_finish(next_position):  # 判断是否已经完成目的
            num += 1
            print(f"第{num}种方法开始")
            for position in all_position:
                print(show_position(position, False), '=====', show_position(position, True))
                draw_picture(position)
            print(f"第{num}种方法结束")

        else:
            search(all_position)
            # 后退一个位置进行另外步骤的尝试
            del all_position[len(all_position) - 1]


position = [False, False, False, False]  # False表示在河岸左边，True表示在河岸右边
all_position = [position]  # 统计全过程
search(all_position)

turtle.mainloop()
