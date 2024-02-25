import json

f = open("商品统计2.txt", "r", encoding="UTF-8")
js_data = f.readlines()
data = {}
for i in js_data:
    data = json.loads(i)
print(data)
f.close()
