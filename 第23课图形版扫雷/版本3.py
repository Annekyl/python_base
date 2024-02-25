import turtle
import random

# 定义常量
WIDTH, HEIGHT = 300, 300
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH / COLS

class Cell(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.is_mine = False
        self.is_revealed = False
        self.neighbor_mines = 0
        self.flagged = False

class Minesweeper:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(WIDTH, HEIGHT)
        self.cells = [[Cell(i, j) for j in range(COLS)] for i in range(ROWS)]
        self.place_mines()
        self.calculate_neighbor_mines()
        self.draw_grid()

    def place_mines(self):
        num_mines = 20
        for _ in range(num_mines):
            x, y = random.randint(0, ROWS-1), random.randint(0, COLS-1)
            self.cells[x][y].is_mine = True

    def calculate_neighbor_mines(self):
        for i in range(ROWS):
            for j in range(COLS):
                if not self.cells[i][j].is_mine:
                    count = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if 0 <= i+dx < ROWS and 0 <= j+dy < COLS and self.cells[i+dx][j+dy].is_mine:
                                count += 1
                    self.cells[i][j].neighbor_mines = count

    def draw_cell(self, cell):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(cell.x * CELL_SIZE - WIDTH / 2, cell.y * CELL_SIZE - HEIGHT / 2)
        turtle.pendown()
        if cell.is_revealed:
            turtle.fillcolor("light gray")
        else:
            turtle.fillcolor("white")
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(CELL_SIZE)
            turtle.right(90)
        turtle.end_fill()
        turtle.hideturtle()

        if cell.is_revealed and not cell.is_mine and cell.neighbor_mines > 0:
            turtle.color("black")
            turtle.penup()
            turtle.goto(cell.x * CELL_SIZE - WIDTH / 2 + CELL_SIZE / 2, cell.y * CELL_SIZE - HEIGHT / 2 + CELL_SIZE / 2)
            turtle.pendown()
            turtle.write(cell.neighbor_mines, align="center", font=("Arial", 12, "normal"))

    def draw_grid(self):
        for row in self.cells:
            for cell in row:
                self.draw_cell(cell)

    def play(self):
        self.screen.onclick(self.click_handler)

    def click_handler(self, x, y):
        cell_x = int((x + WIDTH / 2) // CELL_SIZE)
        cell_y = int((y + HEIGHT / 2) // CELL_SIZE)
        clicked_cell = self.cells[cell_x][cell_y]

        if clicked_cell.is_mine:
            print("Game Over!")
            self.reveal_all_mines()
        else:
            self.reveal_cell(clicked_cell)

    def reveal_cell(self, cell):
        if not cell.is_revealed and not cell.flagged:
            cell.is_revealed = True
            self.draw_cell(cell)
            if cell.neighbor_mines == 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= cell.x+dx < ROWS and 0 <= cell.y+dy < COLS:
                            self.reveal_cell(self.cells[cell.x+dx][cell.y+dy])

    def reveal_all_mines(self):
        for row in self.cells:
            for cell in row:
                if cell.is_mine:
                    cell.is_revealed = True
                    self.draw_cell(cell)

# 创建游戏实例并运行
game = Minesweeper()
game.play()

turtle.mainloop()
