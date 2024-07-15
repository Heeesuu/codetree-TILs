n = int(input())
arr = [0] * 201  # 마이너스 영역까지 포함할 수 있도록 배열 크기 설정
start = 100  # 시작 위치를 100으로 설정

for i in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'R':
        for j in range(start, start + a):
            arr[j] += 1
        start += a
    else:
        for k in range(start - a, start):
            arr[k] += 1
        start -= a

count = 0
for x in arr:
    if x > 1:
        count += x - 1

print(count-1)