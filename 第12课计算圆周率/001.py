pai = 0
for i in range(100):
    pai += 1 / pow(16, i) * ((4 / (8 * i + 1)) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
print("Π的值为：{:.10f}".format(pai))
