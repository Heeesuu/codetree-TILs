a, b = map(int,input().split())
count = 0
answer =[1] * b

while a != 0:
    ans = a%b
    answer[ans] *= 2
    a = a // b

for i in range(len(answer)):
    if i == 0:
        answer[i] = 1
    if i != 0 and answer[i] == 1:
        answer[i] = 0 
    count += answer[i]
        
print(count)