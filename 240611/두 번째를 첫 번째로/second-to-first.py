a = list(input())

first = a[0]
second = a[1]

answer =[]

for i in a:
    if i == second:
        c = first
        answer.append(c)
    else:
        answer.append(i)

for i in answer:
    print(i, end='')