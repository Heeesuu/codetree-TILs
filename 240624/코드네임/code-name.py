class codename:
    def __init__(self, code, score):
        self.code = code
        self.score = score

codenames = []

for i in range(5):
    a, b = tuple(input().split())
    codenames.append(codename(a, int(b)))


minindex = 0
for i in range(1, 5):
    if codenames[minindex].score > codenames[i].score:
        minindex = i 


print(codenames[minindex].code, codenames[minindex].score)