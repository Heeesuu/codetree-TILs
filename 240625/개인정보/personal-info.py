n = 5

class Info:
    def __init__(self, name, hei, wei):
        self.name = name
        self.hei = hei
        self.wei = wei


arr = [tuple(input().split())for _ in range(n)]
students= [Info(name, int(hei), float(wei))for name, hei, wei in arr]


students.sort(key= lambda x: (x.name, -x.hei, -x.wei))

print("name")
for stu in students:
    print(stu.name, stu.hei, end=' ')
    print("{:.1f}".format(stu.wei))

students.sort(key= lambda x: (-x.hei))
print()
print("height")
for stu in students:
    print(stu.name, stu.hei, end=' ')
    print("{:.1f}".format(stu.wei))