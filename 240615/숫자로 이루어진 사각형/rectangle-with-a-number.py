def ans(n):
    count = 1
    for i in range(n):
        for j in range(n):
            print(count, end = ' ')
            count += 1
            if count > 9:
                count = 1
        print()

ans(int(input()))