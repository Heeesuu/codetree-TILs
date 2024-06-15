def plus(n, m):
    return(n+m)

def minus(n, m):
    return(n - m)

def times(n, m):
    return(n * m)

def division(n, m):
    return n // m

a, b, c = map(str, input().split())

a = int(a)
c = int(c)

if b == "+":
    print(a, "+", c, "=", plus(a, c))
elif b == '-':
    print(a, "-", c, "=", minus(a, c))
elif b == '*':
    print(a, "*", c, "=", times(a, c))
elif b == '/':
    print(a, "/", c, "=", divide(a, c))
else:
    print("False")