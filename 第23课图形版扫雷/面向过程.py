import turtle
import random

# 游戏板大小
BOARD_SIZE = 10

# 方块大小
BLOCK_SIZE = 30

# 雷的数量
NUM_MINES = 10

# 创建游戏板
board = [[{"mine": False, "opened": False} for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# 创建乌龟画笔
pen = turtle.Turtle()
turtle.tracer(0)

def draw_square(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

def draw_text(x, y, text, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.write(text, align="center", font=("Arial", 12, "normal"))

def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * BLOCK_SIZE - BOARD_SIZE * BLOCK_SIZE / 2
            y = row * BLOCK_SIZE - BOARD_SIZE * BLOCK_SIZE / 2
            if board[row][col]["opened"]:
                color = "white"
            else:
                color = "gray"
            draw_square(x, y, BLOCK_SIZE, color)
    turtle.update()

def draw_mines():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col]["mine"] and board[row][col]["opened"]:
                x = col * BLOCK_SIZE - BOARD_SIZE * BLOCK_SIZE / 2
                y = row * BLOCK_SIZE - BOARD_SIZE * BLOCK_SIZE / 2
                draw_square(x, y, BLOCK_SIZE, "red")
    turtle.update()

def draw_numbers():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if not board[row][col]["mine"]:
                count = count_adjacent_mines(row, col)
                if count > 0 and board[row][col]["opened"]:
                    x = col * BLOCK_SIZE - BOARD_SIZE * BLOCK_SIZE / 2 + BLOCK_SIZE / 2
                    y = row * BLOCK_SIZE - BOARD_SIZE * BLOCK_SIZE / 2 + BLOCK_SIZE / 4
                    draw_text(x, y, str(count), "black")
    turtle.update()

def count_adjacent_mines(row, col):
    count = 0
    for i in range(max(0, row - 1), min(row + 2, BOARD_SIZE)):
        for j in range(max(0, col - 1), min(col + 2, BOARD_SIZE)):
            if board[i][j]["mine"]:
                count += 1
    return count

def place_mines():
    mines_placed = 0
    while mines_placed < NUM_MINES:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        if not board[row][col]["mine"]:
            board[row][col]["mine"] = True
            mines_placed += 1

def open_block(row, col):
    if not board[row][col]["opened"]:
        board[row][col]["opened"] = True
        if board[row][col]["mine"]:
            game_over()
        elif count_adjacent_mines(row, col) == 0:
            for i in range(max(0, row - 1), min(row + 2, BOARD_SIZE)):
                for j in range(max(0, col - 1), min(col + 2, BOARD_SIZE)):
                    open_block(i, j)

def game_over():
    draw_mines()
    draw_text(0, -200, "Game Over", "red")

def on_click(x, y):
    col = int((x + BOARD_SIZE * BLOCK_SIZE / 2) // BLOCK_SIZE)
    row = int((y + BOARD_SIZE * BLOCK_SIZE / 2) // BLOCK_SIZE)
    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
        open_block(row, col)
        draw_board()
        draw_numbers()

# 初始化游戏
place_mines()
draw_board()

# 绑定鼠标点击事件
turtle.onscreenclick(on_click)

# 进入主循环
turtle.mainloop()
