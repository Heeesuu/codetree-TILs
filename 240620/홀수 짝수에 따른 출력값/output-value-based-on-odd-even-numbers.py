def fi(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return n + fi(n - 2)
    else:
        return n + fi(n - 2)

n = int(input())

if n % 2 == 0:
    print(fi(n))
else:
    print(sum(i for i in range(1, n + 1, 2)))