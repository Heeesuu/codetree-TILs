n, m = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = a*b


for i in arr:
    for a in i:
        print(a, end=' ')
    print()