a, b = map(int, input().split())

def cal(a, b):
    if a > b:
        a = a* 2
        b = b + 10
        return a, b
    else:
        b = b * 2
        a = a + 10
        return a, b

n, m = cal(a, b)
print(n, m)