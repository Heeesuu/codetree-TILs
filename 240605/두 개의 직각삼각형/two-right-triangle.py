n = int(input())
cnt = 0

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end='')
    for k in range(cnt):
        print(" ", end='')
    for l in range(i):
        print("*", end='')
    cnt += 2
    print()