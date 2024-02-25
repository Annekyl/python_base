# 导入random库，方便后续生成随机数  
import random as r
# 导入time库， 用于计时
import time
# 导入turtle库，用于图形绘制
import turtle as t

# 设置turtle的绘制速度为100，100是最快的速度  
t.tracer(0)
t1 = t.Pen()
t1.ht()
high = 0  # 初始值
add = 0.05 / 3  # 增加值


def time():
    while (1):
        global high
        t1.clear()
        add = 0.05 / 3
        high += add
        t1.penup()
        t1.goto(-200, 210)
        t1.write('{:.2f}'.format(high), font=('宋体', 30))

        k = 0
        if notfound == 10:
            break
        t1._tracer(10)
        break


# 定义一个函数where，输入为x坐标，返回值为所在的区域编号
def where(x):
    # 如果x坐标在-210到180之间  
    if -210 <= x <= 180:
        # 对于每个区域，判断x坐标是否在该区域内  
        for i in range(10):
            # 如果x坐标在区域i内  
            if -210 + 40 * i <= x <= -180 + 40 * i:
                # 返回区域编号i  
                return i


def click(x, y):
    try:
        mines[where(x)][where(y)].dig()
    except Exception:
        return


# 定义Mine类，继承自turtle库的Pen类，用于绘制雷块图形并实现一些功能  
class Mine(t.Pen):
    # 初始化方法，输入为x、y坐标，功能是创建一个Mine对象并将其放置在对应位置，同时设置一些属性
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        # 记录Mine对象的x,y坐标  
        self.pu()
        self.color('lightgreen')
        self.shape('square')
        # 设置画笔的形状为正方形  
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        # 设置画笔的形状大小比例，这里设置为宽度高度都是原来的1.5倍  
        self.goto(-195 + 40 * x, -195 + 40 * y)
        # 将画笔移动到对应位置，每个Mine对象之间的距离是40个像素  
        self.have = False
        # 是否已被点击的标志位，初始化为False  
        self.around = 0
        # 表示周围有多少雷的数值，初始化为0  

    # dig方法，功能是当Mine对象被点击时执行的操作
    def dig(self):
        global Game
        if self.have == True:
            # 如果Mine对象已经被点击过  
            Game = 1
            # 将全局变量Game设置为1，表示游戏结束  
            self.shape('blank')
            # 将Mine对象的形状设置为空白，即不再显示正方形形状  
            self.fd(-5)
            self.seth(-90)
            self.fd(15)
            self.write('X', font=('微软雅黑', 20))
            # 在当前位置写下字母X,表示雷
            return
        if self.around != 0:
            # 如果Mine对象的周围有雷（即self.around不为0）  
            self.shape('blank')
            # 将Mine对象的形状设置为空白，即不再显示正方形形状  
            self.fd(-5)
            self.seth(-90)
            self.fd(15)
            self.write(self.around, font=('微软雅黑', 20))
            # 在当前位置写下数字self.around（即周围有多少雷）
            self.fd(-15)
            self.seth(0)
            self.fd(5)
        if self.around == 0 and self.shape() == 'square':
            # 如果Mine对象的周围没有雷（即self.around为0）并且当前显示的是正方形形状
            self.shape('blank')
            # 将Mine对象的形状设置为空白，即不再显示正方形形状
            for i in range(self.x - 1, self.x + 2):
                # 防止超出范围
                # 对于当前Mine对象周围的每个Mine对象，调用dig方法
                for j in range(self.y - 1, self.y + 2):
                    if 0 <= i < 10 and 0 <= j < 10:
                        # 如果i、j在合法范围内
                        mines[i][j].dig()
                        # 调用对应Mine对象的dig方法
                        # 连锁


# 创建一个10x10的二维列表，每个元素初始化为0，代表该位置没有地雷
mines = [[0 for _ in range(10)] for _ in range(10)]

# 遍历整个mines列表，创建一个Mine对象代表每个格子  
for i in range(10):
    for j in range(10):
        mines[i][j] = Mine(i, j)

    # 初始化数字变量为0，用于记录地雷的数量
num = 0

# 循环直到数字变量num达到10，即在地毯式搜索之前，随机放置10颗地雷  
while num < 10:
    # 随机选择一个格子的坐标  
    a, b = r.randint(0, 9), r.randint(0, 9)
    # 如果选中的格子尚未被标记为地雷（have==False）  
    if mines[a][b].have == False:
        # 将选中的格子标记为地雷（have=True）并将num加1  
        mines[a][b].have = True
        num += 1

    # 再次遍历整个mines列表，计算每个格子周围地雷的数量并存储在around变量中
# 如果该格子有地雷，将around设为'X'  
for i in range(10):
    for j in range(10):
        around = 0
        for x in range(max(0, i - 1), min(10, i + 2)):  # 这里保证x,y一定在0~9之间
            for y in range(max(0, j - 1), min(10, j + 2)):
                around += mines[x][y].have
        mines[i][j].around = around
        if mines[i][j].have:
            mines[i][j].around = 'X'

        # 初始化Game变量为0，用于控制游戏是否结束
Game = 0

# 初始化notfound变量为0，用于记录还有多少格子尚未被点击  
notfound = 0

# 当Game为0时，循环执行下面的代码块，直到所有格子都被点击或找到地雷为止  
while Game == 0:
    notfound = 0
    # 遍历所有格子，如果格子的形状仍为正方形（即尚未被点击），则将notfound加1  
    for i in range(10):
        for j in range(10):
            if mines[i][j].shape() == 'square':
                notfound += 1

                # 如果notfound等于10，说明所有格子都被点击了，此时跳出循环，游戏结束
    if notfound == 10:
        break
    time()
    t.update()
    t.onscreenclick(click)

if Game == 1:
    print('Loss')
if notfound == 10:
    print('Win')
