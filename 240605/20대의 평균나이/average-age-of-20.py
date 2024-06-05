answer = 0
cnt = 0

while True:
    a = int(input())
    if a >= 30 or a < 20:
        break
    else:
        answer += a
        cnt += 1

aver = answer/cnt


print(f"{aver:.2f}")