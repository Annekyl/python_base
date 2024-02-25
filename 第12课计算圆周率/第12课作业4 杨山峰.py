for x in range(17):
    for y in range(26):
        z = 30 - x - y
        if x * 3 + y * 2 + z == 50 and x != 0 and y != 0 and z != 0:
            print(f"男人有{x}个，女人有{y}个，小孩有{z}个")
