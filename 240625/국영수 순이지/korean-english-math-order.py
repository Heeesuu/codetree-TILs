n = int(input())

class Info:
    def __init__(self, name, ko, eng, math):
        self.name= name
        self.ko = ko
        self.eng = eng
        self.math = math


arr = [tuple(input().split()) for _ in range(n)]

students = [Info(name, int(ko), int(eng), int(math)) for name, ko, eng, math in arr]

students.sort(key= lambda x: (-x.ko, -x.eng, -x.math))

for student in students:
    print(student.name, student.ko, student.eng, student.math)