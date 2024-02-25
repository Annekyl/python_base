def read_txt_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # 去除行尾的换行符和空格
            lines = []
            for i in line:
                lines.append(int(i))
            data.append(lines)
    return data


# 指定要读取的txt文件路径
file_path = '简单模式迷宫.txt'

# 调用函数读取txt文件内容并转换为二维列表
result = read_txt_file(file_path)

# 打印结果
print(result)
print(type(result))
