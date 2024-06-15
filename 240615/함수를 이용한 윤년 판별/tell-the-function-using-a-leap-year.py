def yun(n):
    if n % 100 == 0 and n % 400 != 0:
        return False
    elif n % 4 != 0:
        return False
    else:
        return True

a = int(input())

if yun(a):
    print("true")
else:
    print("false")