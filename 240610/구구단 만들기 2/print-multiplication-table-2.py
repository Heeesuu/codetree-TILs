a, b = map(int, input().split())
cnt = 2

for i in range(4):
    for i in range(b, a-1, -1):
        if i == a:
            print(f"{i} * {cnt} = {i * cnt}", end ='')
        else:
            print(f"{i} * {cnt} = {i * cnt} / ", end ='')
    cnt += 2
    print()