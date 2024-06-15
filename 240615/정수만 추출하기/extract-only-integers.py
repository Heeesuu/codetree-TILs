a, b = input().split()
numA=''
numB=''

for i in a:
    if i.isdigit():
        numA += i
    else:
        break
    
for i in b:
    if i.isdigit():
        numB += i
    else:
        break

print(int(numA) + int(numB))