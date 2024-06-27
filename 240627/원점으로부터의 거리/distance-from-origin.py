n = int(input())
distance = []

def distan(x, y):
    return abs(x) + abs(y)

for i in range(n):
    a, b = map(int, input().split())
    distance.append((distan(a, b), i + 1))

distance.sort()

for _, idx in distance:
    print(idx)