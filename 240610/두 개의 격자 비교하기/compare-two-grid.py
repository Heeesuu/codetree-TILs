a, b = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(a)]
arr2= [list(map(int, input().split())) for _ in range(a)]
arr3= [[0 for _ in range(b)] for _ in range(a)]

for i in range(a):
    for j in range(b):
        if arr[i][j] != arr2[i][j]:
            arr3[i][j] = 1



for i in arr3:
    for j in i:
        print(j, end=' ')
    print()