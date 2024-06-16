def susu(arr, brr, index ,blength):
    for i in range(blength):
        if arr[index] != brr[i]:
            return False
        else:
            index += 1
    return True


a, b = map(int, input().split())

aarr= list(map(int, input().split()))
barr = list(map(int, input().split()))
bleng = len(barr)

for i in range(len(aarr)):
    if aarr[i] == barr[0]:
        if susu(aarr, barr, i, bleng):
            print("Yes")
        else:
            print("No")
    else:
        print("No")