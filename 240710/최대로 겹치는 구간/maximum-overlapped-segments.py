n = int(input())
arr = [0] * 100

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a-1, b-1):
        arr[j] += 1 


print(max(arr))