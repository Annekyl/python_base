import turtle
import random

BOARD_SIZE = 10  # 游戏板大小
BLOCK_SIZE = 30  # 方块大小
NUM_MINES = 10  # 雷的数量


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mine = False
        self.opened = False

    def draw(self, pen):
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()
        if self.opened:
            color = "white"
        else:
            color = "gray"
        pen.color(color)
        pen.begin_fill()
        for _ in range(4):
            pen.forward(BLOCK_SIZE)
            pen.right(90)
        pen.end_fill()


class MinesweeperGame:
    def __init__(self):
        self.board = [[Block(col * BLOCK_SIZE - BOARD_SIZE * BLOCK_SIZE / 2,
                             row * BLOCK_SIZE - BOARD_SIZE * BLOCK_SIZE / 2)
                       for col in range(BOARD_SIZE)]
                      for row in range(BOARD_SIZE)]
        self.pen = turtle.Turtle()
        turtle.tracer(0)

    def draw_board(self):
        for row in self.board:
            for block in row:
                block.draw(self.pen)
        turtle.update()

    def place_mines(self):
        mines_placed = 0
        while mines_placed < NUM_MINES:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            block = self.board[row][col]
            if not block.mine:
                block.mine = True
                mines_placed += 1

    def count_adjacent_mines(self, row, col):
        count = 0
        for i in range(max(0, row - 1), min(row + 2, BOARD_SIZE)):
            for j in range(max(0, col - 1), min(col + 2, BOARD_SIZE)):
                if self.board[i][j].mine:
                    count += 1
        return count

    def open_block(self, row, col):
        block = self.board[row][col]
        if not block.opened:
            block.opened = True
            if block.mine:
                self.game_over()
            elif self.count_adjacent_mines(row, col) == 0:
                for i in range(max(0, row - 1), min(row + 2, BOARD_SIZE)):
                    for j in range(max(0, col - 1), min(col + 2, BOARD_SIZE)):
                        self.open_block(i, j)

    def game_over(self):
        self.draw_board()
        self.pen.penup()
        self.pen.goto(0, -200)
        self.pen.pendown()
        self.pen.color("red")
        self.pen.write("Game Over", align="center", font=("Arial", 12, "normal"))

    def on_click(self, x, y):
        col = int((x + BOARD_SIZE * BLOCK_SIZE / 2) // BLOCK_SIZE)
        row = int((y + BOARD_SIZE * BLOCK_SIZE / 2) // BLOCK_SIZE)
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            self.open_block(row, col)
            self.draw_board()

    def start(self):
        self.place_mines()
        self.draw_board()
        turtle.onscreenclick(self.on_click)
        turtle.mainloop()


game = MinesweeperGame()
game.start()
