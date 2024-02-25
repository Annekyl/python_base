import tkinter as tk
import tkinter.messagebox
from enum import Enum
import random
import time


# 方格状态枚举类型
class State(Enum):
    opened = 1
    marked = 2
    closed = 3


# 小方格
class Block:
    def __init__(self, master, x, y):
        self.master = master  # 窗口
        self.x = x  # 坐标
        self.y = y
        self.is_mine = False  # 是否有雷
        self.AroundMineCount = 0  # 周围雷数
        self.state = State.closed  # 当前状态
        self.button = tk.Button(master, width=3, height=1, bg="light gray")  # 外观
        self.button.grid(row=y, column=x)

    # 雷块设置为打开状态
    def reveal(self):
        if self.is_mine:
            # 更改按钮样式为雷的样式
            self.button.configure(text='雷', bg="black", fg="white")
        else:  # 显示周围雷数
            if self.AroundMineCount > 0:
                self.button.config(text=str(self.AroundMineCount), bg="white")
            else:
                self.button.config(bg="white")
            self.button.config(state="disabled")  # 禁用按钮

    # 雷块设置为标记状态
    def mark(self):
        # 更改按钮样式为旗子的样式
        self.button.configure(bg="red")
        self.state = State.marked

    # 雷块设置为关闭状态
    def reset(self):
        self.button.config(bg="light gray")
        self.state = State.closed


# 游戏区
class Field:
    def __init__(self, master, width, height, num_mines):
        self.mine_locations = None
        self.minefield = None
        self.blocks = []  # 存储方格对象
        self.master = master  # 窗口
        self.width = width  # 行列数
        self.height = height
        self.num_mines = num_mines  # 雷数

        self.create_minefield()  # 创建游戏区
        self.create_widgets()  # 实例化所需要的方格对象
        self.count_adjacent_mines()  # 计算周围雷数

    # 设置雷区的属性
    def create_minefield(self):
        self.minefield = [[0 for _ in range(self.width)] for _ in range(self.height)]

        self.mine_locations = random.sample([(x, y) for x in range(self.width) for y in range(self.height)],
                                            self.num_mines)
        for x, y in self.mine_locations:
            self.minefield[y][x] = -1

    # 实例化所需要的方格对象
    def create_widgets(self):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                block = Block(self.master, x, y + 1)
                if self.minefield[y][x] == -1:
                    block.is_mine = True
                row.append(block)
            self.blocks.append(row)

    # 一个雷的周围雷数
    def count_mine_nums(self, block):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= block.x + dx < self.width and 0 <= block.y - 1 + dy < self.height and \
                        self.minefield[block.y - 1 + dy][
                            block.x + dx] == -1:
                    count += 1
        return count

    # 计算周围雷数
    def count_adjacent_mines(self):
        for row in self.blocks:
            for block in row:
                count = self.count_mine_nums(block)
                block.AroundMineCount = count

    # 被点击后周围雷的显示
    def reveal_adjacent_blocks(self, block):
        # 被打开了或是地雷
        if block.state == State.opened or block.is_mine:
            return

        if block.state != State.marked:  # 没有被标记则打开
            block.reveal()  # 打开该雷
            block.state = State.opened  # 设置状态为打开

        if self.count_mine_nums(block) == 0:  # 周围雷数为0，递归
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= block.x + dx < self.width and 0 <= block.y - 1 + dy < self.height and \
                            self.blocks[block.y - 1 + dy][block.x + dx].state != State.opened:
                        self.reveal_adjacent_blocks(self.blocks[block.y - 1 + dy][block.x + dx])

    # 显示雷区所有方格内容（游戏失败显示所有雷）
    def display_all(self):
        for row in self.blocks:
            for block in row:
                if block.is_mine or block.state == State.opened:
                    block.reveal()
                elif block.state == State.closed:
                    block.reset()
                else:
                    block.mark()


# 计时器
class Timer:
    def __init__(self, root, x, y, interval):
        self.root = root  # 主窗口
        self.start_time = 0  # 计时开始时间
        self.running = False  # 是否计时
        self.interval = interval  # 显示间隔时间
        # 外观
        self.timer_label = tk.Label(root, text="Time: 0")
        self.timer_label.grid(row=y, column=x, columnspan=2, sticky='ne')

    # 开始计时
    def start(self):
        self.start_time = time.time()
        self.running = True

    # 更新时间
    def update_timer(self):
        if self.running:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.configure(text="Time: " + str(elapsed_time))
            self.root.after(self.interval, self.update_timer)


# 计数器
class Counter:
    def __init__(self, root, x, y):
        self.root = root
        # 外观
        self.label = tk.Label(root, text="flag: 0")
        self.label.grid(row=y, column=x, columnspan=2, sticky='w')

    def update(self, value):  # 更新数字
        self.label.config(text="flag: " + str(value))


# 扫雷游戏界面
class MinesweeperGame:
    def __init__(self, root, cols, rows, minenum, restart_game_callback):
        self.cols = cols  # 行列数
        self.row = rows
        self.minenum = minenum  # 雷数
        self.counter = None  # 计数器
        self.gamefield = None  # 游戏区
        self.timer = None  # 计时器
        self.root = root  # 主窗口
        self.restart_game_callback = restart_game_callback  # 游戏重启控制

        self.flagnum = 1  # 允许标记数
        self.game(self.root, cols, rows, minenum)  # 开启游戏过程

    # 游戏逻辑处理
    def game(self, root, cols, rows, minenum):
        self.gamefield = Field(root, cols, rows, minenum)  # 新建游戏区
        self.flagnum = minenum  # 旗子数等于雷数
        for row in self.gamefield.blocks:  # 按键绑定点击事件
            for block in row:
                block.button.bind("<Button-1>", self.handle_click)
                block.button.bind("<Button-3>", self.handle_click)
        # 重置按钮
        button = tk.Button(root, width=3, height=1, relief=tk.RIDGE, bg="blue")  # 外观
        button.grid(row=0, column=int(cols / 2) - 1, columnspan=2)
        button.bind("<Button-1>", lambda event: self.reset_game())

        # 计数器
        self.counter = Counter(root, 0, 0)
        self.counter.update(minenum)

        # 计时器
        self.timer = Timer(root, cols - 2, 0, 1000)
        self.timer.start()
        self.timer.update_timer()

    # 重置游戏
    def reset_game(self):
        self.game(self.root, self.cols, self.row, self.minenum)

    # 按键处理事件
    def handle_click(self, event):
        button = event.widget  # 获取触发事件的按钮对象
        y = button.grid_info()["row"]
        x = button.grid_info()["column"]
        block = self.gamefield.blocks[y - 1][x]
        if block.state == State.marked:  # 被标记时按键即为取消标记状态
            self.flagnum += 1
            self.counter.update(self.flagnum)
            block.state = State.closed
            block.reset()
        else:
            if event.num == 1:  # 左键
                if block.is_mine:  # 打开是雷失败
                    self.game_fail()
                self.gamefield.reveal_adjacent_blocks(block)  # 不是雷递归打开
                if self.success():  # 是否成功
                    self.game_succeed()
            elif event.num == 3:  # 右键
                if self.flagnum != 0 and block.state == State.closed:  # 标记
                    self.flagnum -= 1
                    self.counter.update(self.flagnum)
                    block.state = State.marked
                    block.mark()

    # 游戏失败后的显示
    def game_fail(self):
        self.timer.running = False
        self.gamefield.display_all()
        for row in self.gamefield.blocks:  # 解除按钮绑定
            for block in row:
                block.button.unbind('<Button-1>')
                block.button.unbind('<Button-3>')
        tk.messagebox.showinfo("提示", "扫雷失败!")
        self.restart_game_callback()  # 重启游戏难度选择界面

    # 游戏成功后的显示
    def game_succeed(self):
        self.timer.running = False
        self.gamefield.display_all()
        for row in self.gamefield.blocks:  # 解除按钮绑定
            for block in row:
                block.button.unbind('<Button-1>')
                block.button.unbind('<Button-3>')
        tk.messagebox.showinfo("提示", "扫雷成功！")
        self.restart_game_callback()  # 重启游戏难度选择界面

    # 判断胜利
    def success(self):
        mine_open_num = 0  # 被打开格数
        for row in self.gamefield.blocks:
            for block in row:
                if block.state == State.opened:
                    mine_open_num += 1
        if mine_open_num == self.gamefield.width * self.gamefield.height - self.gamefield.num_mines:
            return True
        else:
            return False


# 游戏进入前难度选择界面
class GameSetup:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Setup")
        # 难度关卡选择
        difficulty_label = tk.Label(root, text="选择难度关卡:")
        difficulty_label.grid(row=0, column=0, sticky=tk.W)

        self.difficulty_var = tk.StringVar(root)
        self.difficulty_var.set("Easy")  # 默认选中"Easy"

        difficulty_options = ["Easy", "Medium", "Hard"]
        difficulty_menu = tk.OptionMenu(root, self.difficulty_var, *difficulty_options)
        difficulty_menu.grid(row=0, column=1, sticky=tk.W)

        # 开始游戏按钮
        start_button = tk.Button(root, text="开始游戏", command=self.start_game, width=10, height=2)
        start_button.grid(row=1, column=1, padx=5, pady=10)

        # 退出游戏按钮
        quit_button = tk.Button(root, text="退出游戏", command=self.quit_game, width=10, height=2)
        quit_button.grid(row=1, column=2, padx=5, pady=10)

    # 开始游戏按钮绑定函数
    def start_game(self):
        # 获取选择的难度关卡
        difficulty = self.difficulty_var.get()
        for widget in self.root.winfo_children():  # 清除当前界面所有内容（准备绘制游戏界面内容）
            widget.destroy()
        if difficulty == 'Easy':
            MinesweeperGame(self.root, 10, 10, 10, self.restart_game)
        elif difficulty == 'Medium':
            MinesweeperGame(self.root, 16, 16, 40, self.restart_game)
        else:
            MinesweeperGame(self.root, 30, 16, 99, self.restart_game)

    # 退出游戏按钮绑定函数
    def quit_game(self):
        # 关闭所有窗口并退出程序
        self.root.destroy()

    # 重启游戏难度选择界面
    def restart_game(self):
        # 销毁当前游戏界面
        for widget in self.root.winfo_children():
            widget.destroy()
        # 重新创建游戏设置界面
        self.__init__(self.root)


def main():
    # 创建主窗口
    root = tk.Tk()
    # 创建游戏设置界面对象
    GameSetup(root)
    # 启动主事件循环
    root.mainloop()


if __name__ == "__main__":
    main()
