def fi(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return n + fi(n - 2)

n = int(input())

print(fi(n))