def minnum(n, m):
    if n < m:
        return n
    else:
        return m

arr = list(map(int, input().split()))

maxi = 101
for i in arr:
    maxi = minnum(i, maxi)
    
print(maxi)