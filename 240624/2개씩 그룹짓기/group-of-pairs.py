n = int(input())
nums = list(map(int, input().split()))

nums.sort()

maxnum = 0

for i in range(n):
    sumnum = nums[i] + nums[2*n -1 - i]
    if sumnum > maxnum:
        maxnum = sumnum


print(maxnum)