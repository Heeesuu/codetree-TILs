def absing(arr):
    brr = []
    for i in arr:
        brr.append(abs(i))
    return brr

n = int(input())

arrlist = list(map(int, input().split()))
brr = []
brr = absing(arrlist)

for i in brr:
    print(i, end=' ')