a = input()
b = []

for i in a :
    if i.isupper():
        b.append(i.lower())
    else:
        b.append(i.upper())

for i in b:
    print(i, end='')