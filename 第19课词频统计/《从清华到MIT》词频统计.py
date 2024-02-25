import jieba
dk = {}


with open('data.txt','r',encoding='utf-8') as f:    #打开文件后即关闭
    sl = f.readlines()                              #得到文件内容的列表
#------把全文切成词，并统计出现次数，变成键值对填入到字典中-------

for s in sl:
    k=jieba.lcut(s, cut_all = True)             #全模式（一个字可能会组多个词），有冗余  （分词）
    for wo in k:
        if len(wo)==2:
           dk[wo] = dk.get(wo,0) + 1            #无此项则添加新项并填0值，有此项则加1


dp = list(dk.items())        #字典的items()函数作用：以列表返回可遍历的(键, 值) 元组数组

print(dp)

dp.sort(key= lambda x:x[1], reverse = True)       #降序  lambda匿名函数（临时函数，简易函数）
print(dp)

for i in range(10):
   print("{}:{}".format(dp[i][0],dp[i][1]))




