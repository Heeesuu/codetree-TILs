n = int(input())

class Info:
    def __init__(self, hei, wei, index):
        self.hei = hei
        self.wei = wei
        self.index = index

students = []
for i in range(1, n+1):
    hei, wei = tuple(map(int, input().split()))
    students.append(Info(hei, wei, i))

students.sort(key = lambda x: (-x.hei, -x.wei, x.index))

for student in students:
    print(student.hei, student.wei, student.index)