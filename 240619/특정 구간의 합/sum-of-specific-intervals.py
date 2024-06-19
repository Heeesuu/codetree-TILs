a, b = map(int, input().split()) 

arr = list(map(int, input().split()))

for i in range(b):
    m, n = map(int, input().split())
    sum = 0
    for j in range(m-1, n):
        sum += arr[j]
    print(sum)