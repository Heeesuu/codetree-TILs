# 입력 받기
xx1, yy1, xx2, yy2 = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

# 두 직사각형의 교차 영역 계산
inter_left = max(xx1, x1)
inter_right = min(xx2, x2)
inter_bottom = max(yy1, y1)
inter_top = min(yy2, y2)

# 교차 영역이 있는지 확인
if inter_left < inter_right and inter_bottom < inter_top:
    # 교차 영역이 있으면
    # 첫 번째 직사각형의 잔해물을 덮기 위한 최소 직사각형의 네 꼭짓점 좌표
    min_x = min(xx1, inter_right)
    max_x = max(xx2, inter_left)
    min_y = min(yy1, inter_top)
    max_y = max(yy2, inter_bottom)
    
    # 잔해물을 덮기 위한 최소 직사각형의 넓이 계산
    remaining_width = max_x - min_x
    remaining_height = max_y - min_y
    remaining_area = remaining_width * remaining_height
    
    print(remaining_area)
else:
    # 교차 영역이 없으면 첫 번째 직사각형의 넓이 반환
    remaining_area = (xx2 - xx1) * (yy2 - yy1)
    print(remaining_area)