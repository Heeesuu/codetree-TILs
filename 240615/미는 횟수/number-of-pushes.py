a = input()
b = input()

al = len(a)
count = 0

while(a != b):
    a = a[-1] + a[:al-1]
    count += 1
    
print(count)