a = input()
b = input()

al = len(a)
count = 0

while(a != b):
    if count > al:
        print(-1)
        break
    a = a[-1] + a[:al-1]
    count += 1

if count <= al:
    print(count)