answer = []
temp = 10000
sum = 0

n = int(input())
num = list(map(int, input().split()))

for i in range(len(num)-1):
    if abs(num[i] - num[i+1]) < temp:
        temp = abs(num[i] - num[i+1])

print(temp)