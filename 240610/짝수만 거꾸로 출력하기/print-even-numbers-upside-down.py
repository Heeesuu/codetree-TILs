n = int(input())

answer = list(map(int, input().split()))

for i in range(len(answer)-1, -1, -1):
    if answer[i] % 2 == 0:
        print(answer[i], end =' ')