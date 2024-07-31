a, b = map(int, input().split())
arr = list(map(int, input().split()))
a = len(arr)
answer = []
count = 1
flag = False

for i in range(a):
    if arr[i] > b and flag:
        count += 1
    elif arr[i] > b:
        flag = True
    else:
        answer.append(count)
        count = 1
        flag = False
answer.append(count)

if max(answer) == 1:
    print(0)
else:
    print(max(answer))