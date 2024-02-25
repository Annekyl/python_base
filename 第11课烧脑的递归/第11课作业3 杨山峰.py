def hannuota(i, A, B, C):  # i为汉诺塔层数，参数A为起始柱子，参数B为中转柱子，参数C为目标柱子
    if i == 1:
        print(A, "移动到", C)  # 将盘子从传入的第一个塔移动到第三个塔
    else:
        hannuota(i - 1, A, C, B)  # 如果不是最下面的盘子，调换目标位置为中转柱子
        print(A, "移动到", C)  # 此时塔1上已经只剩下一个盘子，移到目标柱子
        hannuota(i - 1, B, A, C)  # 将剩下的盘子通过起始柱子移到目标柱子


num = int(input("请输入层数"))
hannuota(num, "塔1", "塔2", "塔3")
