n, m ,k = map(int, input().split())

student = [0]*n

for i in range(m):
    a = int(input())
    if student[a-1] == k-1:
        print(a)
        break
    else:
        student[a-1] += 1