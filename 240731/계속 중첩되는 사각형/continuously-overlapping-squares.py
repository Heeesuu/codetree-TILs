n = int(input())
arr = [[0 for _ in range(200)]for _ in range(200)]

for i in range(1, n+1):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100

    if i % 2 == 1:
        for i in range(x1, x2):
            for j in range(y1, y2):
                arr[i][j] = 1
    
    else:
        for i in range(x1, x2):
            for j in range(y1, y2):
                arr[i][j] = 2


count = 0

for i in arr:
    for j in i:
        if j == 2:
            count += 1

print(count)