n = int(input())

class Info:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math


arr = [tuple(input().split()) for _ in range(n)]
students = [Info(name, int(kor), int(eng), int(math)) for name, kor, eng, math in arr]


students.sort(key = lambda x: x.kor + x.eng + x.math)

for student in students:
    print(student.name, student.kor, student.eng, student.math)