def two(a):
    arr = []
    brr = [0]*100
    for i in a:
        arr.append(i)
        brr[a.index(i)] += 1
        if 2 in brr:
            return False
    return True



a = input()

if two(a):
    print("No")
else:
    print("Yes")