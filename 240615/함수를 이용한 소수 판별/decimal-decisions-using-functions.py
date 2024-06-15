def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())
if a == 1:
    sum = 1
else:
    sum = 0

for i in range(a, b+1):
    if isPrime(i):
        sum += i

print(sum)