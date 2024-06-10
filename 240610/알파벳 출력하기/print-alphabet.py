n = int(input())
cnt = 1
num = 65

for i in range(n):
    for j in range(cnt):
        print(chr(num), end='')
        num += 1
    print()
    cnt +=1