n, m ,k = map(int, input().split())

student = [0]*n
flag = False

for i in range(m):
    a = int(input())
    if student[a-1] == k-1:
        print(a)
        flag = True
        break
    else:
        student[a-1] += 1

if not flag:
    print(-1)