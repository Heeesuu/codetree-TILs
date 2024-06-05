answer = []

for i in range(5):
    a = int(input())
    if a % 3 == 0:
        answer.append(1)

if len(answer)==5:
    print(1)
else:
    print(0)