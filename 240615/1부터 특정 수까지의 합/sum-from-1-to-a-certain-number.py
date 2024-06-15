def add(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(add(int(input())) // 10)