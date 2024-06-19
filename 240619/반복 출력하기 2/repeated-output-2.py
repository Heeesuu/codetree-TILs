def je(n):
    if n == 0:
        return False
    print("HelloWorld")
    n -= 1
    je(n)

n = int(input())
je(n)