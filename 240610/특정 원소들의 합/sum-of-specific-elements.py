arr = [list(map(int, input().split())) for _ in range(4)]
cnt = 1
sum = 0

for i in range(4):
    for j in range(cnt):
        sum += arr[i][j]
    cnt += 1 

print(sum)