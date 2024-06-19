def s(a, n):
    if a == n+1:
        return False
    print(a, end=' ')
    s(a+1, n)

def t(n):
    if n == 0:
        return False
    print(n, end=' ')
    t(n-1)


n = int(input())
s(1, n)
print()
t(n)