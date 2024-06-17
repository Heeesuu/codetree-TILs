def g(n, m):
    if n > m:
        return(n, n+25)
    else:
        return(m, m+25)

    

a, b = map(int, input().split())

a, b = g(a, b)

print(a, b)