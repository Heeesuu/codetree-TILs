arr = [[0 for _ in range(2000)]for _ in range(2000)]

xx1, yy1, xx2, yy2 = map(int, input().split())
xx1 += 1000
yy1 += 1000
xx2 += 1000
yy2 += 1000

for i in range(xx1, xx2):
    for j in range(yy1, yy2):
        arr[i][j] = 1

x1, y1, x2, y2 = map(int, input().split())
x1 += 1000
y1 += 1000
x2 += 1000
y2 += 1000

for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i][j] = 0

xtemp = 0
ytemp = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            if xtemp < i:
                xtemp = i
            if ytemp < j:
                ytemp = j

print((xtemp-xx1 +1) * (ytemp-yy1 +1))