a = int(input())

n = 1

while a != 0:
    a = a // n
    n += 1
    if n <= 1:
        break

print(n-1)