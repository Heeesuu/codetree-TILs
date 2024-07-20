arr =[[0 for _ in range(2000)]for _ in range(2000)]

for i in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 1000
    y1 += 1000
    x2 += 1000
    y2 += 1000

    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] = 1

x1, y1, x2, y2 = map(int, input().split())
x1 += 1000
y1 += 1000
x2 += 1000
y2 += 1000

for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i][j] = 0

count = 0

for col in arr:
    for i in col:
        if i == 1:
            count += 1 

print(count)