a, b, word = map(str, input().split())
dic = []

a = int(a)
b = int(b)

for i in range(a):
    wo = input()
    if word in wo:
        dic.append(wo)

dic.sort()

print(dic[b-1])