a, b = map(int, input().split())
answer = []

answer.append(a)
answer.append(b)

for i in range(10):
    if i <= 1:
        print(answer[i], end=' ')
    else:
        ans = answer[i-1] + (2* answer[i-2])
        answer.append(ans)
        print(ans, end=' ')