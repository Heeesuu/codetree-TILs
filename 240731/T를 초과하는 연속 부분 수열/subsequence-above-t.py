a, b = map(int, input().split())
arr = list(map(int, input().split()))
a = len(arr)
answer = []
count = 1

for i in range(1, a):
    if arr[i] > b and arr[i-1] > b:
        count += 1
    else:
        answer.append(count)
        count = 1
answer.append(count)

if max(answer) == 1:
    print(0)
else:
    print(max(answer))