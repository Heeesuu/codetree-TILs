n = int(input())

cnt = n

for i in range(n):
    for j in range(cnt, n+1):
        print(j, end=' ')

    cnt -= 1   
    print()