def s(n):
    if n == 0:
        return False
    s(n-1)
    print(n, end=' ')
    

def t(n):
    if n == 0:
        return False
    print(n, end=' ')
    t(n-1)


n = int(input())
s(n)
print()
t(n)