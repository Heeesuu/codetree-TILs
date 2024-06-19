def s(n):
    if n == 0:
        return False
    print(n, end=' ')
    s(n-1)
    print(n, end=' ')

n = int(input())

s(n)