answer = []

for i in range(3):
    a = input()
    answer.append(len(a))

print(max(answer) - min(answer))