def ans(n, m):
    for i in range(n):
        for j in range(m):
            print(1, end='')
        print()

a, b = map(int, input().split())
ans(a, b)