def get_remaining_area(first_rect, second_rect):
    x1, y1, x2, y2 = first_rect
    x3, y3, x4, y4 = second_rect
    
    # 교차 영역 계산
    inter_left = max(x1, x3)
    inter_right = min(x2, x4)
    inter_bottom = max(y1, y3)
    inter_top = min(y2, y4)
    
    # 교차 영역의 넓이 계산
    if inter_left < inter_right and inter_bottom < inter_top:
        inter_area = (inter_right - inter_left) * (inter_top - inter_bottom)
    else:
        inter_area = 0  # 교차 영역이 없으면 0
    
    # 첫 번째 직사각형의 전체 넓이
    first_area = (x2 - x1) * (y2 - y1)
    
    # 잔여 영역 넓이
    remaining_area = first_area - inter_area
    
    return remaining_area

# 입력 받기
x1, y1, x2, y2 = map(int, input().split())
first_rect = (x1, y1, x2, y2)

x3, y3, x4, y4 = map(int, input().split())
second_rect = (x3, y3, x4, y4)

# 남아있는 첫 번째 직사각형의 잔해물을 덮기 위한 최소 직사각형의 넓이 계산
result = get_remaining_area(first_rect, second_rect)
print(result)