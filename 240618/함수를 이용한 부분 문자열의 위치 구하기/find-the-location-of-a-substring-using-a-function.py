word = input()


def cal(st):
    if st in word:
        return word.find(st)
    else:
        return False


st = input()
a = cal(st)
if a.isdigit():
    print(a)
else:
    print("-1")