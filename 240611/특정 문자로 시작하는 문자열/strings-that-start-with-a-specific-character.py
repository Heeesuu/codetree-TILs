n = int(input())
answer=[]

for i in range(n):
    answer.append(input())

count = 0
length = 0

b = input()
for i in answer:
    if b in i:
        count += 1
        length += len(i)

print(f"{count} {length/count:.2f}")