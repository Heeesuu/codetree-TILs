answer = [0]*5

for i in range(5):
    a = int(input())
    if a % 3 == 0:
        answer[i] = a

if len(answer)==5:
    print(1)
else:
    print(0)