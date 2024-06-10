n = int(input())
cnt = 1

for i in range(1, n+1):
    for j in range(n):
        if i % 2 == 1:
            print(cnt, end=' ')
            cnt += 1
        else:
            cnt += 1
            print(cnt, end= ' ')
            cnt += 1
    print()