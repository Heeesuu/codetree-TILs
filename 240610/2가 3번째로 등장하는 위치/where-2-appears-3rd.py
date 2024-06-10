n = int(input())

answer =list(map(int, input().split()))

count = 0

for i in range(len(answer)):
    if count == 3:
        print(i)
        break
    if answer[i]== 2:
        count += 1