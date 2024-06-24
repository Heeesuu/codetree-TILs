code, point, time = input().split()


class st:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

st1 = st(code, point, time)

print(f"secret code : {st1.code}")
print(f"meeting point : {st1.point}")
print(f"time : {st1.time}")