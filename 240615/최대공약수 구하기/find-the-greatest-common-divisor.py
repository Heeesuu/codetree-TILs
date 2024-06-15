def maxnum(n, m):
    temp = 0
    for i in range(1, n+1):
        if n % i ==0 and m % i == 0:
            if temp < i:
                temp = i
    print(temp)

a, b = map(int, input().split())
if a > b :
    maxnum(b, a)
else:
    maxnum(a, b)