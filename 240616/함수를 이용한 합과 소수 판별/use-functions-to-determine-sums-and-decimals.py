def decimal(n):
    count = 0
    for i in range(2, n+1):
        if n % i == 0:
            count += 1
    if count > 1:
        return False
    else:
        return True

def even(n):
    a = 0
    b = 0
    answer = 0
    if n >= 10 and n != 100:
        a = n // 10
        b = n % 10
        answer = a + b
    elif n < 10:
        b = n % 10
        answer = a + b
    else:
        answer = 1
    
    if answer % 2 == 0:
        return True
    else:
        return False
    
count = 0
a, b = map(int, input().split())

for i in range(a, b+1):
    if decimal(i) and even(i):
        count += 1

print(count)