def two(a):
    arr = []
    for i in a:
        if i in arr:
           return False
        else:
            arr.append(i)
    return True



a = input()

if two(a):
    print("No")
else:
    print("Yes")