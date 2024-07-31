n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))


count = 1
answer = []
for i in range(1, len(arr)):
    if arr[i] > 0 and arr[i-1] > 0:
        count += 1
    elif arr[i] < 0 and arr[i-1] < 0:
        count += 1
    else:
        answer.append(count)
        count = 1

answer.append(count)

print(max(answer))