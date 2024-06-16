def yun(n):
    if (n % 400 == 0) or (n % 100 != 0 and n % 4 == 0):
        return True
    else:
        return False

def season(n):
    if n >= 3 and n <= 5:
        return "Spring"
    if n >= 6 and n <= 8:
        return "Summer"
    if n >= 9 and n <= 11:
        return "Fall"
    else:
        return "Winter"

def yunable(n, m):
    if n == 2:
        if m > 29 or m < 1:
            return False
    elif n == 4 or n == 6 or n == 9 or n == 11:
        if m > 30 or m < 1:
            return False
    else:
        if m > 31 or m < 1:
            return False
    return True

def able(n, m):
    if n == 2:
        if m > 28 or m < 1:
            return False
    elif n == 4 or n == 6 or n == 9 or n == 11:
        if m > 30 or m < 1:
            return False
    else:
        if m > 31 or m < 1:
            return False
    return True

a, b, c = map(int, input().split())

if yun(a):
    if yunable(b, c):
        print(season(b))
    else:
        print("-1")
else:
    if able(b, c):
        print(season(b))
    else:
        print("-1")