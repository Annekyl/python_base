from tabulate import tabulate

data = {"id": ['9787572218194', '9787572218194', '9787544654166', '9787530217610', '9787530221099'],
        "name": ['四级词汇书', '听力练习上册', '听力练习下册', '《兄弟》', "《文城》"]
        }
table = tabulate(data, headers="keys",showindex=True, tablefmt='simple',numalign='left')
print(table)