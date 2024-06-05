n = int(input())
flag = False

a = 1

for i in range(n):
    for j in range(i+1):
        print("*", end='')
    print()
    print()

for i in range(n-1, 0, -1):
    for j in range(i, 0, -1):
        print("*", end='')
    print()
    print()