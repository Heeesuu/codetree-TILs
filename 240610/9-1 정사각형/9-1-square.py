n = int(input())
cnt = 9

for i in range(1, (n*n)+1):
    if cnt == 0:
        cnt = 9
    if i % n == 0:
        print(cnt)
        cnt -= 1
    else:
        print(cnt, end='')  
        cnt -= 1