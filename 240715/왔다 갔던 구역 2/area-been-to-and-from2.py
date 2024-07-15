n = int(input())
start = 0
arr = [0] * 200

for i in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'R':
        for j in range(start, a):
            arr[j] += 1
        start += a
    else:
        for k in range(start, a, -1):
            arr[k] += 1
        start -= a
count = 0

for j in arr:
    if j > 1:
        count += 1

print(count//2)