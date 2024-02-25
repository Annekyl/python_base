import random
import turtle
import time

BLOCK_SIZE = 30  # 游戏中雷块的大小
NUM_MINES = 10  # 真雷的数量
BOARD_SIZE = 10  # 游戏面板的大小


class Block:
    """雷块类"""

    def __init__(self, x, y):
        self.x = x  # 横坐标
        self.y = y  # 纵坐标
        self.mine = False  # 是否为雷
        self.opened = False  # 是否被点击
        self.near_mines = 0  # 附近的真雷的数量

    def draw(self, pen):
        """画方块"""
        pen.penup()
        pen.goto(self.x - BLOCK_SIZE / 2, self.y - BLOCK_SIZE / 2)
        pen.pendown()
        if self.opened:  # 如果被点击,颜色为白色
            color = "white"
        else:
            color = "gray"
        pen.color("pink", color)
        pen.begin_fill()
        for _ in range(4):
            pen.forward(BLOCK_SIZE)
            pen.right(90)
        pen.end_fill()


class MineGame:
    def __init__(self):
        """
        创建二维列表对象用于存放方块，创建画笔并设置画笔速度为0
        board:用于存放10*10的方块的二维列表，其中横纵坐标已赋值
        row:第几行  横着看
        line：第几列  竖着看
        pen:画笔
        """
        self.board = [[Block(row * BLOCK_SIZE, line * BLOCK_SIZE)
                       for row in range(BOARD_SIZE)]
                      for line in range(BOARD_SIZE)]
        self.pen = turtle.Pen()
        self.pen2 = turtle.Pen()
        turtle.tracer(0)
        self.start_time = None

    def draw_board(self):
        """画出全部的方块并统计附近的雷的数量"""
        for line in self.board:
            for block in line:
                block.draw(self.pen)
        turtle.update()

    def place_mines(self):
        """设置真雷"""
        mines_placed = 0
        while mines_placed < NUM_MINES:
            row = random.randint(0, BOARD_SIZE - 1)
            line = random.randint(0, BOARD_SIZE - 1)
            block = self.board[row][line]
            if not block.mine:
                block.mine = True
                mines_placed += 1

    def count_adjacent_mines(self, row, line):
        """统计附近的真雷的数量"""
        count = 0
        for i in range(max(0, row - 1), min(row + 2, BOARD_SIZE)):
            for j in range(max(0, line - 1), min(line + 2, BOARD_SIZE)):
                if self.board[i][j].mine:  # 如果为雷，数量加1
                    count += 1
        return count

    def game_over(self):
        """点击到真雷，游戏结束"""
        # 弹出提示框询问用户是否重新开始游戏
        choice = turtle.numinput("点击到雷", "要再来一次吗 (1: Yes, 0: No)", minval=0, maxval=1)
        if choice == 1:
            self.reset_game()  # 重新开始游戏
            self.game_start()  # 开始新游戏

    def open_block(self, row, line):
        """翻开雷块后的操作"""
        block = self.board[row][line]
        self.count_adjacent_mines(row, line)
        self.pen.penup()
        self.pen.goto(row * BLOCK_SIZE, line * BLOCK_SIZE)
        self.pen.pendown()
        self.pen.write(self.board[row][line].near_mines, align="center", font=("华文仿宋", 5, "normal"))
        if not block.opened:
            block.opened = True
            if block.mine:  # 如果为雷块，结束游戏
                self.game_over()
            elif self.count_adjacent_mines(row, line) == 0:  # 如果附近雷块为0，进行递归将周围的雷块都翻开
                for i in range(max(0, row - 1), min(row + 2, BOARD_SIZE)):
                    for j in range(max(0, line - 1), min(line + 2, BOARD_SIZE)):
                        self.open_block(i, j)

    def on_click(self, x, y):
        """点击方块"""
        row = int(x // BLOCK_SIZE)
        line = int(y // BLOCK_SIZE)
        if 0 <= row < BOARD_SIZE and 0 <= line < BOARD_SIZE:
            self.open_block(row, line)
            self.draw_board()

    def start_timer(self):
        """计时器函数"""
        self.pen2.clear()
        elapsed_time = time.time() - self.start_time  # 计算已经过的时间
        self.pen2.penup()
        self.pen2.goto(-100, -200)
        self.pen2.pendown()
        self.pen2.write("已用时间: {:.2f}s".format(elapsed_time), align="center", font=("华文仿宋", 20, "normal"))
        turtle.ontimer(self.start_timer, 100)  # 每隔100毫秒更新计时器

    def game_start(self):
        self.place_mines()
        self.draw_board()
        turtle.onscreenclick(self.on_click)
        self.start_time = time.time()  # 记录游戏开始的时间
        self.start_timer()  # 开启计时器
        turtle.mainloop()

    def reset_game(self):
        """重置游戏状态和计时器"""
        self.board = [[Block(row * BLOCK_SIZE, line * BLOCK_SIZE)
                       for row in range(BOARD_SIZE)]
                      for line in range(BOARD_SIZE)]
        self.pen.clear()
        self.start_time = None


game = MineGame()
game.game_start()
