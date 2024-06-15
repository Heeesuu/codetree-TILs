a = input()
b = input()

numA=''
numB=''

for i in a:
    if i.isdigit():
        numA += i
    
for i in b:
    if i.isdigit():
        numB += i

print(int(numA) + int(numB))