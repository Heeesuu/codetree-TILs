a = input()
count1 =0
count2 =0

for i in range(len(a)-1):
    if a[i] == "e" and a[i+1]== "e":
        count1 += 1
    if a[i] == "e" and a[i+1]== "b":
        count2 += 1

print(count1, count2)