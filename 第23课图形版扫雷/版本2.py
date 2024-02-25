import turtle
import random

# 定义方格大小和数量
CELL_SIZE = 20
NUM_ROWS = 10
NUM_COLS = 10

# 颜色定义
COLOR_BG = "#CCCCCC"
COLOR_CELL_COVERED = "#999999"
COLOR_CELL_UNCOVERED = "#DDDDDD"
COLOR_CELL_TEXT = "#000000"
COLOR_CELL_BOMB = "#FF0000"

# 游戏状态
GAME_STATE_PLAYING = 0
GAME_STATE_GAME_OVER = 1
GAME_STATE_WIN = 2

class Cell:
    def __init__(self, row, col, has_bomb):
        self.row = row
        self.col = col
        self.has_bomb = has_bomb
        self.is_covered = True
        self.num_adjacent_bombs = 0

    def uncover(self):
        self.is_covered = False

    def set_num_adjacent_bombs(self, num_adjacent_bombs):
        self.num_adjacent_bombs = num_adjacent_bombs

class Board:
    def __init__(self, num_rows, num_cols, num_bombs):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_bombs = num_bombs
        self.game_state = GAME_STATE_PLAYING
        self.cells = []
        self.create_cells()
        self.place_bombs()

    def create_cells(self):
        for row in range(self.num_rows):
            cell_row = []
            for col in range(self.num_cols):
                cell = Cell(row, col, False)
                cell_row.append(cell)
            self.cells.append(cell_row)

    def place_bombs(self):
        bombs_to_place = self.num_bombs
        while bombs_to_place > 0:
            row = random.randint(0, self.num_rows-1)
            col = random.randint(0, self.num_cols-1)
            if not self.cells[row][col].has_bomb:
                self.cells[row][col].has_bomb = True
                bombs_to_place -= 1

    def get_cell(self, row, col):
        if row < 0 or row >= self.num_rows or col < 0 or col >= self.num_cols:
            return None
        return self.cells[row][col]

    def get_adjacent_cells(self, row, col):
        adjacent_cells = []
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                if d_row == 0 and d_col == 0:
                    continue
                adj_row = row + d_row
                adj_col = col + d_col
                adj_cell = self.get_cell(adj_row, adj_col)
                if adj_cell:
                    adjacent_cells.append(adj_cell)
        return adjacent_cells

    def calculate_num_adjacent_bombs(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell = self.cells[row][col]
                if cell.has_bomb:
                    continue
                adjacent_cells = self.get_adjacent_cells(row, col)
                num_adjacent_bombs = sum([adj_cell.has_bomb for adj_cell in adjacent_cells])
                cell.set_num_adjacent_bombs(num_adjacent_bombs)

    def uncover_cell(self, row, col):
        cell = self.get_cell(row, col)
        if not cell or not cell.is_covered:
            return
        if cell.has_bomb:
            self.game_state = GAME_STATE_GAME_OVER
        else:
            cell.uncover()
            if cell.num_adjacent_bombs == 0:
                adjacent_cells = self.get_adjacent_cells(row, col)
                for adj_cell in adjacent_cells:
                    self.uncover_cell(adj_cell.row, adj_cell.col)

    def is_game_won(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell = self.cells[row][col]
                if not cell.has_bomb and cell.is_covered:
                    return False
        return True

class Game:
    def __init__(self):
        self.board = Board(NUM_ROWS, NUM_COLS, 10)
        self.init_ui()
        self.running = True

    def init_ui(self):
        turtle.setup(self.board.num_cols * CELL_SIZE, self.board.num_rows * CELL_SIZE)
        turtle.title("扫雷游戏")
        turtle.bgcolor(COLOR_BG)
        turtle.penup()

        for row in range(self.board.num_rows):
            for col in range(self.board.num_cols):
                x = col * CELL_SIZE - (self.board.num_cols * CELL_SIZE) / 2
                y = (self.board.num_rows - row - 1) * CELL_SIZE - (self.board.num_rows * CELL_SIZE) / 2
                turtle.goto(x, y)
                turtle.pendown()
                turtle.begin_fill()
                turtle.color(COLOR_CELL_COVERED)
                for _ in range(4):
                    turtle.forward(CELL_SIZE)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()

    def run(self):
        turtle.onscreenclick(self.handle_click)
        while self.running:
            turtle.update()

    def handle_click(self, x, y):
        if self.board.game_state != GAME_STATE_PLAYING:
            return

        col = int((x + (self.board.num_cols * CELL_SIZE) / 2) // CELL_SIZE)
        row = int((-y + (self.board.num_rows * CELL_SIZE) / 2) // CELL_SIZE)

        if col < 0 or col >= self.board.num_cols or row < 0 or row >= self.board.num_rows:
            return

        self.board.uncover_cell(row, col)
        self.update_ui()

        if self.board.game_state == GAME_STATE_GAME_OVER:
            turtle.textinput("游戏结束", "你输了！")
            self.running = False
        elif self.board.is_game_won():
            turtle.textinput("游戏结束", "你赢了！")
            self.running = False

    def update_ui(self):
        for row in range(self.board.num_rows):
            for col in range(self.board.num_cols):
                cell = self.board.cells[row][col]
                x = col * CELL_SIZE - (self.board.num_cols * CELL_SIZE) / 2
                y = (self.board.num_rows - row - 1) * CELL_SIZE - (self.board.num_rows * CELL_SIZE) / 2
                turtle.goto(x, y)
                turtle.pendown()
                if cell.is_covered:
                    turtle.color(COLOR_CELL_COVERED)
                    turtle.begin_fill()
                    for _ in range(4):
                        turtle.forward(CELL_SIZE)
                        turtle.right(90)
                    turtle.end_fill()
                    turtle.penup()
                else:
                    turtle.fillcolor(COLOR_CELL_UNCOVERED)
                    turtle.begin_fill()
                    for _ in range(4):
                        turtle.forward(CELL_SIZE)
                        turtle.right(90)
                    turtle.end_fill()
                    turtle.penup()

                    if cell.num_adjacent_bombs > 0:
                        turtle.goto(x + CELL_SIZE / 2, y - CELL_SIZE / 2)
                        turtle.write(cell.num_adjacent_bombs, align="center", font=("Arial", 16, "normal"))
                    elif cell.has_bomb:
                        turtle.goto(x + CELL_SIZE / 2, y - CELL_SIZE / 2)
                        turtle.color(COLOR_CELL_TEXT)
                        turtle.write("*", align="center", font=("Arial", 16, "normal"))
                        turtle.color(COLOR_CELL_BOMB)
                        turtle.dot(CELL_SIZE / 2)

if __name__ == "__main__":
    game = Game()
    game.run()
