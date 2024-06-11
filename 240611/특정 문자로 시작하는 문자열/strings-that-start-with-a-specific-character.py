n = int(input())
answer=[]

for i in range(n):
    answer.append(input())

count = 0
length = 0

b = input()
for i in answer:
    if i.startswith(b):
        count += 1
        length += len(i)


if count ==0:
    print("0 -nan")
elif length ==0:
    print("0 -nan")
else:
    print(f"{count} {length/count:.2f}")