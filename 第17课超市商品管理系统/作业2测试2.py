import json

f = open("商品统计2.txt", "r", encoding="UTF-8")
js_data = f.readlines()
print(js_data)
data = json.loads(js_data)
f.close()

