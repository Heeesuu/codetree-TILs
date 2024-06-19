def s(n):
    if n == 0:
        return
    print("* " * n)
    s(n-1)
    print("* " * n)

a = int(input())

s(a)