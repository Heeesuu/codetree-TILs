def d31(n):
    if n <= 31 and n > 0:
        return True
    else:
        return False

def d30(n):
    if n <= 30 and n > 0:
        return True
    else:
        return False

def d28(n):
    if n <= 28 and n > 0:
        return True
    else:
        return False


a, b = map(int, input().split())

if a > 12 or a < 1:
    print("No")
elif a == "2":
    if d28(b):
        print("Yes")
    else:
        print("No")
elif a == "4" or a == "6" or a == "4" or a == "9" or  a == "11":
    if d30(b):
        print("Yes")
    else:
        print("No")
else:
    if d31(b):
        print("Yes")
    else:
        print("No")