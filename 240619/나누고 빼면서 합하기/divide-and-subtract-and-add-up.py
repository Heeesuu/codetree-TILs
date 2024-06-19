def su(a, b, arr):
    suma = 0
    while(b > 0):
        suma += arr[b-1]
        if b % 2 == 0:
            b = b // 2
        else:
            b = b - 1
    return suma

a, b = map(int, input().split())
arr = list(map(int, input().split()))

a = su(a, b, arr)

print(a)