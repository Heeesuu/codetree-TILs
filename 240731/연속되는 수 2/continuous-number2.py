n = int(input())
arr = []

for i in range(n):
    a = int(input())
    arr.append(a)

le = len(arr)
answer = []
count = 1

for i in range(1, le):
    if arr[i] != arr[i-1]:
        answer.append(count)
        count = 1      
    else:
        count += 1
answer.append(count)


print(max(answer))