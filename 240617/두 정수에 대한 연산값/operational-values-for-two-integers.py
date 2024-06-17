def g(n, m):
    if n > m:
        return(m*2, n+25)
    else:
        return(n*2, m+25)

    

a, b = map(int, input().split())

a, b = g(a, b)

print(a, b)