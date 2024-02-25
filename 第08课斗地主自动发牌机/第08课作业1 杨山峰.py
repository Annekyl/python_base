import random

pk = ["红心A", "红心2", '红心3', '红心4', '红心5', '红心6', '红心7', '红心8', '红心9', '红心10',
      '红心J', '红心Q', '红心K', '方块A',  '方块2', '方块3', '方块4', '方块5', '方块6',
      '方块7', '方块8', '方块9', '方块10', '方块J', '方块Q', '方块K', '黑桃A',  '黑桃2',
      '黑桃3', '黑桃4', '黑桃5', '黑桃6', '黑桃7', '黑桃8', '黑桃9', '黑桃10', '黑桃J', '黑桃Q',
      '黑桃K', '梅花A', '梅花2', '梅花3', '梅花4', '梅花5', '梅花6', '梅花7', '梅花8', '梅花9',
      '梅花10', '梅花J', '梅花Q', '梅花K', '大王', '小王']
people1 = []
people2 = []
people3 = []
# 每人先发出17张牌
for piece in range(17):
    list_num = random.randint(0, 53 - piece)  #
    people1.append(pk[list_num])  # 追加给人
    del pk[list_num]  # 删除牌库中对应的牌

for piece in range(17):  # 每人先发17张
    list_num = random.randint(0, 53 - piece - 17)  #
    people2.append(pk[list_num])  # 追加给人
    del pk[list_num]  # 删除牌库中对应的牌

for piece in range(17):  # 每人先发17张
    list_num = random.randint(0, 53 - piece - 17 - 17)  #
    people3.append(pk[list_num])  # 追加给人
    del pk[list_num]  # 删除牌库中对应的牌

# 选出地主并发牌
select = random.randint(1, 3)
if select == 1:
    people1.extend(pk)
    print(f"people1为地主，他拥有的牌是：{people1}\n")
    print(f"people2为农民，他拥有的牌为：{people2}\n")
    print(f"people3为农民，他拥有的牌为：{people3}")

if select == 2:
    people2.extend(pk)
    print(f"people1为农民，他拥有的牌是：{people1}\n")
    print(f"people2为地主，他拥有的牌为：{people2}\n")
    print(f"people3为农民，他拥有的牌为：{people3}")

if select == 3:
    people3.extend(pk)
    print(f"people1为农民，他拥有的牌是：{people1}\n")
    print(f"people2为农民，他拥有的牌为：{people2}\n")
    print(f"people3为地主，他拥有的牌为：{people3}")
