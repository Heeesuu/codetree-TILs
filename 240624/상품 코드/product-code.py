class pro:
    def __init__(self, name="codetree", code="50"):
        self.name = name
        self.code = code


pro1 = pro()

print(f"product {pro1.code} is {pro1.name}")

a, b = input().split()
pro1 = pro(a, b)

print(f"product {pro1.code} is {pro1.name}")