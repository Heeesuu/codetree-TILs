n = int(input())
cnt = 0
num = 65

for i in range(n):
    for j in range(cnt):
        print(" ", end =' ')
    for k in range(n-cnt):
        if num == 91:
            num = 65
        print(chr(num), end=' ')
        num += 1
    print()
    cnt += 1