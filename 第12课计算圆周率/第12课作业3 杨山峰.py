total = 0
for x in range(6):
    for y in range(11):
        for z in range(51):
            if x + y * 0.5 + z * 0.1 == 5:
                print(f"一元硬币有{x}个，五角硬币有{y}个，一角硬币有{z}个")
                total += 1
print(f"共有{total}种方案")
