def je(n):
    if n == 0:
        return False
    print("HelloWorld")
    je(n-1)

n = int(input())
je(n)