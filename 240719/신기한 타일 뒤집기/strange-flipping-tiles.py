n = int(input())

arr = [0] * 200001
start = 100000
color_w = 0
color_b = 0

for i in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'R':
        for j in range(start, start + a):
            arr[j] = 2
        start += a - 1  
    else:
        for j in range(start, start - a, -1):
            arr[j] = 1
        start -= a - 1

for tile in arr:
    if tile == 1:
        color_w += 1
    elif tile == 2:
        color_b += 1

print(color_w, color_b)