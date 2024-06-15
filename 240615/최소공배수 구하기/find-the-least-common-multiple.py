def minx(n, m):
    count = 1
    while True:
        if (m * count) % n == 0:
            print(m * count)
            break
        count += 1

a, b = map(int, input().split())

if a > b:
    minx(b, a)
else:
    minx(a, b)