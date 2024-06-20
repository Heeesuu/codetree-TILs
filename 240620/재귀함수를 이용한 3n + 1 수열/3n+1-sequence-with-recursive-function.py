def s(a, n):
    if n == 1:
        return a
    if n % 2 == 0:
        return s(a+1, n//2)
    else:
        return s(a+1, n*3+1)


n = int(input())
a= 0
print(s(a, n))