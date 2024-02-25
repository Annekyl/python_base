def age(n):
    if n == 5:
        return 10
    else:
        return age(n + 1) + 2


t = age(1)
print(t)
