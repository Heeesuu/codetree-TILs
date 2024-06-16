n = int(input())

def division(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i]//2
    return arr


arr = list(map(int, input().split()))

arr = division(arr[:])

for i in arr:
    print(i, end=' ')