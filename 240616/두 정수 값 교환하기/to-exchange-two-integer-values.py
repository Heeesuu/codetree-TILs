def swap(n, m):
    n, m = m, n
    return n, m

a, b = map(int, input().split())
a, b = swap(a, b)
print(a, b)