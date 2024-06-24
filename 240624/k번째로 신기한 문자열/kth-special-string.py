a, b, word = map(str, input().split())
dic = []

def certi(wo, word):
    for i in range(len(word)):
        if wo[i] != word[i]:
            return False
    return True

a = int(a)
b = int(b)

for i in range(a):
    wo = input()
    if certi(wo, word):
        dic.append(wo)

dic.sort()

print(dic[b-1])