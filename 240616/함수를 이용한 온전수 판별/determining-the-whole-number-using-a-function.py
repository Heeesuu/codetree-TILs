def on(n):
    if n % 2 == 0:
        return False
    elif n % 3 ==0 and n % 9 != 0:
        return False
    elif str(n)[-1] == "5":
        return False
    else:
        return True
    
a, b = map(int, input().split())
count = 0

for i in range(a, b+1):
    if on(i):
        count += 1

print(count)