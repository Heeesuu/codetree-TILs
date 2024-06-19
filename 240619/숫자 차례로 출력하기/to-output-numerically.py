def s(n):
    if n == 8:
        return False
    print(n, end=' ')
    s(n+1)

def t(n):
    if n == 0:
        return False
    print(n, end=' ')
    t(n-1)


n = int(input())
s(1)
print()
t(n)