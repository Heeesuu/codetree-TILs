n = int(input())
arr = []

for i in range(n):
    a = int(input())
    arr.append(a)

le = len(arr)
answer = []
count = 0

for i in range(le):
    if i == 0 or arr[i] != arr[i-1]:
        answer.append(count)
        count = 0
        count += 1
    else:
        count += 1

if le < 2:
    print(1)
else:
    print(max(answer))