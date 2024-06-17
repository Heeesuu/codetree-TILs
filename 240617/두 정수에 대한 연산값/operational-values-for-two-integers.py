def g(n, m):
    if n > m:
        return(n+25, m*2)
    else:
        return(n*2, m+25)

    

a, b = map(int, input().split())

a, b = g(a, b)

print(a, b)