a, b, c = map(int, input().split())

def su(n):
    if n < 10:
        return n

    return su(n//10) + n % 10

print(su(a * b* c))