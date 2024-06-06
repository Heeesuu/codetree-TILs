n = int(input())
cnt = 0

for i in range(1, n+1):
    if i % 2 == 1:
        for j in range(n-cnt):
            print("*", end =' ')
        cnt += 1
    else:
        for j in range(cnt):
            print("*", end =' ')
    print()

for i in range(1, n+1):
    if i % 2 == 1:
        for j in range(cnt):
            print("*", end =' ')
    else:
        for j in range(n-cnt):
            print("*", end =' ')
        cnt += 1
        
    print()