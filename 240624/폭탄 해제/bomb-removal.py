class bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
        

a = (input().split())

code, color, second = a

bomb1 = bomb(code, color, second)

print(f"code : {bomb1.code}")
print(f"color : {bomb1.color}")
print(f"second : {bomb1.second}")