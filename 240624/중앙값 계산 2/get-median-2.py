n = int(input())

arr = list(map(int, input().split()))
arr2 = []

def middle(arr):
    arr.sort()
    return arr[len(arr)//2]

for i in range(1, len(arr)+1):
    arr2.append(arr[i-1])
    if i % 2 == 1:
        print(middle(arr2), end=' ')