a = input()

def consen(n):
    a1 = int(n[0])+ int(n[1])
    a2 = int(n)

    if a2 % 2 == 0 and a1 % 5 == 0:
        return("Yes")
    else:
        return("No")

print(consen(a))