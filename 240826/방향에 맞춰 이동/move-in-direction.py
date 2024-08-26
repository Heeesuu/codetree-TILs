n = int(input())

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

nx, ny = 0, 0

for i in range(n):
    a, b = input().split()
    b = int(b)

    if a == 'N':
        a = 3
    elif a =='E':
        a = 0
    elif a =='S':
        a = 1
    else:
        a = 2

    for i in range(b):
        nx += dx[a]
        ny += dy[a]


print(nx, ny)