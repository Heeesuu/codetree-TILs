n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]


x, y = n - 1, n - 1
a = 1

while y >= 0:

    while x >= 0:
        arr[x][y] = a
        a += 1
        x -= 1
    y -= 1
    x += 1

    if y < 0:
        break
    while x < n:
        arr[x][y] = a
        a += 1
        x += 1
    y -= 1
    x -= 1


for row in arr:
    print(' '.join(map(str, row)))