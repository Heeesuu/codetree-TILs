n = int(input())

def su(n):
    if n == 0:
        return
    
    su(n-1)
    print("*" * n)


su(n)