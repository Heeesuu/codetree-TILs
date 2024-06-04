a, se = map(str, input().split())
b, ex = map(str, input().split())

a = int(a)
b = int(b)

if a >= 19 and se=="M":
    print(1)
elif b>= 19 and ex =="M":
    print(1)
else:
    print(0)