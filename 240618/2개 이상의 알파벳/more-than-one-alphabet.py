def two(a):
    an = a[0]
    for i in a:
        if i == a[0]:
            continue
        else:
            return False
        
    return True

a = input()

if two(a):
    print("No")
else:
    print("Yes")