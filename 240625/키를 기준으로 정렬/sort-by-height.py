n = int(input())

class An:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


arr = [tuple(input().split())for _ in range(n)]
people = [An(name, height, weight)for name, height, weight in arr]

people.sort(key=lambda x: x.height)

for person in people:
    print(person.name, person.height, person.weight)