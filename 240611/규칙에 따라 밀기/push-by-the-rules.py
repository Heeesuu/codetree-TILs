a = input()
b = input()

count = 0

for i in b:
    if i == "L":
        count -= 1
    else:
        count += 1

count = count % len(a)

if count < 0:
    count = len(a) + count

answer = a[-count:] + a[:-count]

print(answer)