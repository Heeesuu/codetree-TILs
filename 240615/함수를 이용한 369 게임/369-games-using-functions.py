def is3x(n):
    return n % 3 == 0

def ishas3(n):
    strn = str(n)
    return is3x(n) or "3" in strn or "6" in strn or "9" in strn

a, b = map(int, input().split())

count = 0
for i in range(a, b+1):
    if ishas3(i):
        count += 1

print(count)