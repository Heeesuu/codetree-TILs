n = int(input())
tn = n
cnt = -1

for i in range(n):
    for j in range(tn, 0, cnt):
        print(j, end=' ')
    print()
    cnt -= 1
    tn += n