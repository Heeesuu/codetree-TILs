def f(n):
    if n == 0:
        return arr[0]

    return max(f(n-1), arr[n])

n = int(input())
arr = list(map(int, input().split()))


print(f(n-1))