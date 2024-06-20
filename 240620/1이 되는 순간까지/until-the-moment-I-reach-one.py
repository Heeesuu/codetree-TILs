def d(n, a):
    if n == 1:
        return a
    if n % 2 ==0:
        a+= 1
        return d(n//2, a)
    else:
        a+= 1
        return d(n//3, a)


n = int(input())
a = 0

print(d(n, a))