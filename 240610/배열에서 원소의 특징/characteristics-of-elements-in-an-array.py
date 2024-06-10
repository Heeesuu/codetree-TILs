answer = list(map(int, input().split()))

for i in range(len(answer)):
    if answer[i] % 3 == 0:
        print(answer[i-1])
        break