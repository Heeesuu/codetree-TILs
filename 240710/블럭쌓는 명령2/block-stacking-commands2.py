n, k = map(int, input().split())
arr = [0] * n


for i in range(k):
    a, b = map(int, input().split())
    for i in range(a-1, b):
        arr[i] += 1

count = max(arr)

print(count)