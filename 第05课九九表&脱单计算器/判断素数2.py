def isprime(a):
    if a < 2:
        return False
    if a < 4:
        return True
    if a % 2 == 0:
        return False
    for i in range(3, int(a ** 0.5) + 1, 2):
        if a % i == 0:
            return False
    else:
        return True


x = int(input())
if isprime(x):
    print("Yes")
else:
    print("No")
