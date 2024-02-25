a = "杨"
print(type(len(a.encode("UTF-8"))))
i = str(a.encode("UTF-8"))
i = i.replace("b", "")
i = i.replace("'", "")
print(a)
print(i)
print(type(i))
