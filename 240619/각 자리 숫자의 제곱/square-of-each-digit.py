def fact(n):
    if n < 10:
        return n * n
    
    digit = (n % 10)
    return fact(n//10) + digit * digit

a = int(input())
print(fact(a))