n  = int(input())
arr = [[0 for _ in range(200)] for _ in range(200)]
start = 100


for i in range(n):
    a, b = map(int, input().split())
    a += 100
    b += 100
    for j in range(a, a+8):
        for k in range(b, b+8):
            arr[j][k] = 1

count = 0

for i in arr:
    for a in i:
        if a == 1:
            count += 1

print(count)