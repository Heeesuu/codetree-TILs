def du(n, m):
    sum = 1
    for i in range(m):
        sum *= n
    return sum

a, b = map(int, input().split())

print(du(a, b))