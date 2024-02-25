import pygame

# 设置颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)


def read_txt_file(file_path):
    """
    读取txt文件转换成二维列表
    :param file_path: 迷宫的文本文件
    :return: 迷宫的二维列表
    """
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # 去除行尾的换行符和空格
            lines = []
            for i in line:
                lines.append(int(i))
            data.append(lines)
    return data


class Map:
    def __init__(self, window, window_size, maze_map):
        """
        地图设计
        :param window:显示的界面
        :param window_size:界面的宽和高
        :param maze_map:地图设计
        """
        self.maze_map = maze_map
        # 计算迷宫的大小
        self.maze_width = len(self.maze_map[0])  # 长为10
        self.maze_height = len(self.maze_map)  # 宽为8

        # 定义墙壁和路径的宽和高
        self.rect_width = window_size[0] / self.maze_width
        self.rect_height = window_size[1] / self.maze_height
        self.window = window

    def draw(self):
        """画迷宫"""
        for row in range(self.maze_height):
            for col in range(self.maze_width):
                x = col * self.rect_width
                y = row * self.rect_height
                if self.maze_map[row][col] == 1:  # 路
                    pygame.draw.rect(self.window, WHITE, (x, y, self.rect_width, self.rect_width), 0)
                else:  # 墙壁
                    pygame.draw.rect(self.window, BLACK, (x, y, self.rect_width, self.rect_width), 0)
        pygame.display.update()
