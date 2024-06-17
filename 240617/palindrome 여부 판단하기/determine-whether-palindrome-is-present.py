def palin(string):
    for i in range(len(string)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True

string = input()

if palin(string):
    print("Yes")
else:
    print("No")