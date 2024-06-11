a = list(input())

if len(a) % 2 == 1:
    for i in range(len(a)-2, -1, -2):
        print(a[i], end='')

else:
    for i in range(len(a)-1, -1, -2):
        print(a[i], end='')