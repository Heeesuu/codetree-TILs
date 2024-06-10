a, b = map(int,input().split())
ans = 0
answer = [0] * b

while a >= 1:
   ans = a % b
   answer[ans] += 1
   a = a // b

sum = 0
for i in answer:
    sum += i ** 2  

print(sum)