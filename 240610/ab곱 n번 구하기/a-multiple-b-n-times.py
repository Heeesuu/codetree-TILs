n = int(input())
sum = 1

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        sum *= j
    print(sum)
    sum = 1