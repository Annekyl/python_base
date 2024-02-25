import turtle
import random

# 游戏板的大小
BOARD_SIZE = 10

# 每个方块的大小
BLOCK_SIZE = 30

# 雷的数量
NUM_MINES = 10

# 游戏结束标志
GAME_OVER = False

class Block:
    def __init__(self, x, y, pen):
        self.x = x
        self.y = y
        self.pen = pen
        self.is_visible = False
        self.is_flagged = False
        self.mine = False
        self.num_adjacent_mines = 0

    def draw(self):
        self.pen.goto(self.x, self.y)
        self.pen.setheading(0)
        self.pen.down()
        self.pen.fillcolor("gray")
        self.pen.begin_fill()
        for _ in range(4):
            self.pen.forward(BLOCK_SIZE)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.up()

        if self.is_visible:
            if self.mine:
                self.pen.goto(self.x + BLOCK_SIZE // 2, self.y + BLOCK_SIZE // 2)
                self.pen.dot(BLOCK_SIZE // 2, "red")
            elif self.num_adjacent_mines > 0:
                self.pen.color("black")
                self.pen.setposition(self.x + BLOCK_SIZE // 2, self.y + BLOCK_SIZE // 2)
                self.pen.write(str(self.num_adjacent_mines), align="center", font=("Arial", 16, "normal"))

        if self.is_flagged:
            self.pen.goto(self.x + BLOCK_SIZE // 2, self.y + BLOCK_SIZE - 10)
            self.pen.color("black", "red")
            self.pen.setheading(270)
            self.pen.begin_fill()
            self.pen.forward(20)
            self.pen.right(120)
            self.pen.forward(20)
            self.pen.right(120)
            self.pen.forward(20)
            self.pen.end_fill()

    def toggle_flag(self):
        if self.is_visible:
            return
        self.is_flagged = not self.is_flagged

    def reveal(self):
        if self.is_visible:
            return
        self.is_visible = True
        if self.mine:
            global GAME_OVER
            GAME_OVER = True
        elif self.num_adjacent_mines == 0:
            for i in range(max(0, row - 1), min(row + 2, BOARD_SIZE)):
                for j in range(max(0, col - 1), min(col + 2, BOARD_SIZE)):
                    self.board[i][j].reveal()

    def count_adjacent_mines(self, row, col):
        count = 0
        for i in range(max(0, row - 1), min(row + 2, BOARD_SIZE)):
            for j in range(max(0, col - 1), min(col + 2, BOARD_SIZE)):
                if self.board[i][j].mine:
                    count += 1
        self.num_adjacent_mines = count
        return count


class Minesweeper:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Minesweeper")
        self.screen.setup(BOARD_SIZE * BLOCK_SIZE + 50, BOARD_SIZE * BLOCK_SIZE + 50)
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    def create_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x = col * BLOCK_SIZE - BOARD_SIZE * BLOCK_SIZE // 2
                y = BOARD_SIZE * BLOCK_SIZE // 2 - row * BLOCK_SIZE
                self.board[row][col] = Block(x, y, self.pen)

    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                self.board[row][col].draw()

    def place_mines(self):
        placed_mines = 0
        while placed_mines < NUM_MINES:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            if not self.board[row][col].mine:
                self.board[row][col].mine = True
                placed_mines += 1

    def count_adjacent_mines(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                self.board[row][col].count_adjacent_mines(row, col)

    def on_click(self, x, y):
        global GAME_OVER
        if GAME_OVER:
            return
        row = (BOARD_SIZE * BLOCK_SIZE // 2 - y) // BLOCK_SIZE
        col = (x + BOARD_SIZE * BLOCK_SIZE // 2) // BLOCK_SIZE
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            block = self.board[row][col]
            if not block.is_visible and not block.is_flagged:
                block.reveal()
        if self.check_win():
            self.win()

    def on_right_click(self, x, y):
        global GAME_OVER
        if GAME_OVER:
            return
        row = (BOARD_SIZE * BLOCK_SIZE // 2 - y) // BLOCK_SIZE
        col = (x + BOARD_SIZE * BLOCK_SIZE // 2) // BLOCK_SIZE
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            block = self.board[row][col]
            if not block.is_visible:
                block.toggle_flag()
        if self.check_win():
            self.win()

    def check_win(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                block = self.board[row][col]
                if not block.is_visible and not block.mine:
                    return False
        return True

    def win(self):
        self.pen.goto(0, 0)
        self.pen.write("You Win!", align="center", font=("Arial", 24, "bold"))

    def lose(self):
        self.pen.goto(0, 0)
        self.pen.write("Game Over", align="center", font=("Arial", 24, "bold"))

    def play(self):
        self.create_board()
        self.draw_board()
        self.place_mines()
        self.count_adjacent_mines()
        self.screen.onclick(self.on_click)
        self.screen.onrightclick(self.on_right_click)
        turtle.done()

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
