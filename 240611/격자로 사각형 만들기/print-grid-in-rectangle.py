n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
a, b, c = 0, 0, 0

for i in range(n):
    for j in range(n):
        if i == 0:
            arr[i][j] = 1
        else:
            if j-1<0 :
                a = 0
                b = arr[i-1][j]
                c = 0
                arr[i][j] = a+b+c
            else:
                a = arr[i-1][j-1]
                b = arr[i-1][j]
                c = arr[i][j-1]
                arr[i][j] = a+b+c

for i in arr:
    for a in i:
        print(a, end=' ')
    print()