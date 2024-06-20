n = int(input())

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

def check(arr, brr):
    return sorted(arr) == sorted(brr)

if check(arr, brr):
    print("Yes")
else:
    print("No")