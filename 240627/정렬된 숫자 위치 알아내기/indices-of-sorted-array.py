n = int(input())
nums = list(map(int, input().split()))

# 원래 리스트와 인덱스를 함께 저장
original_nums = [(num, i) for i, num in enumerate(nums)]

# 원래 리스트를 정렬
original_nums.sort()

# 각 원소의 새로운 위치를 계산
result = [0] * n
for i, (num, ori_idx) in enumerate(original_nums):
    result[ori_idx] = i + 1

print(" ".join(map(str, result)))