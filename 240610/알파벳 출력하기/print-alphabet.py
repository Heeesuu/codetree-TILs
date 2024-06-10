n = int(input())
cnt = 1
num = 65

for i in range(n):
    for j in range(cnt):
        if num == 91:
            num = 65
        print(chr(num), end='')
        num += 1
    print()
    cnt +=1