n = int(input())

class Info:
    def __init__(self, h, w, index):
        self.h = h
        self.w = w
        self.index = index

people = []

for i in range(n):
    a, b = map(int, input().split())
    ind = i + 1
    person = Info(a, b, ind)
    people.append(person)

people.sort(key = lambda x: (x.h, -x.w))

for i in people:
    print(i.h, i.w, i.index)