n = int(input())

class Info:
    def __init__(self, name, hei, wei):
        self.name = name
        self.hei = hei
        self.wei = wei

arr = [tuple(input().split())for _ in range(n)]
students = [Info(name, int(hei), int(wei))for name, hei, wei in arr]

students.sort(key= lambda x:(x.hei, -x.wei))

for i in students:
    print(i.name, i.hei, i.wei)