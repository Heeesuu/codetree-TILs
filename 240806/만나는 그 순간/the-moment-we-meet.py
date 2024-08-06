n, m = map(int, input().split())
start = 0
sec = 0

arr = []
brr = []

for i in range(n):
    a, b = input().split()
    b = int(b)
    if a == 'R':
        for i in range(b):
            start += 1
            arr.append(start)
    else:
        for i in range(b):
            start -= 1
            arr.append(start)

start = 0

for i in range(m):
    a, b = input().split()
    b = int(b)
    if a == 'R':
        for i in range(b):
            start += 1
            brr.append(start)
    else:
        for i in range(b):
            start -= 1
            brr.append(start)

flag = False

for i in range(len(arr)):
    if arr[i] == brr[i]:
        print(i+1)
        flag = True
        break

if not flag:
    print("-1")