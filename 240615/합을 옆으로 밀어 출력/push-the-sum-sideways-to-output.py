n = int(input())
sum = 0
for i in range(n):
    sum += int(input())

answer = str(sum)

answer = str(answer)[1:]+ str(answer)[:1]

print(answer)