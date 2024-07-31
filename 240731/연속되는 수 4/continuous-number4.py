n = int(input())
arr =[]


for i in range(n):
    arr.append(int(input()))

a = len(arr)
count = 1
answer = []

for i in range(1, a):
    if arr[i] < arr[i-1]:
        answer.append(count)
        count =1
    else:
        count += 1
answer.append(count)

print(max(answer)-1)