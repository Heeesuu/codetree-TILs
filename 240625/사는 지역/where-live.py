n = int(input())

class region:
    def __init__(self, name, num, reg):
        self.name = name
        self.num = num
        self.reg = reg

arr = [tuple(input().split())for _ in range(n)]
people = [region(name, num, reg) for name, num, reg in arr]

ind = 0

for i, person in enumerate(people):
    if person.name > people[ind].name:
        ind = i

print(f"name {people[ind].name}")
print(f"addr {people[ind].num}")
print(f"city {people[ind].reg}")