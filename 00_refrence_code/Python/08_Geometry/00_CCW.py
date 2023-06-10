# CCW (Counter Clock Wise)
def ccw(_x1: int, _y1: int, _x2: int, _y2: int, _x3: int, _y3: int) -> int:
    # python은 result의 결과를 그대로 return해도 상관 없음
    result = (_x2 - _x1) * (_y3 - _y1) - (_x3 - _x1) * (_y2 - _y1)
    if result > 0:
        return 1
    elif result < 0:
        return -1
    return 0


# 교차 여부 판별(ccw 활용) -> True: 교차, False: 교차 X
def is_intersect(_x1: int, _y1: int, _x2: int, _y2: int, _x3: int, _y3: int, _x4: int, _y4: int) -> bool:
    # ab (abc * abd)
    ab = ccw(_x1, _y1, _x2, _y2, _x3, _y3) * ccw(_x1, _y1, _x2, _y2, _x4, _y4)
    # cd (cda * cdb)
    cd = ccw(_x3, _y3, _x4, _y4, _x1, _y1) * ccw(_x3, _y3, _x4, _y4, _x2, _y2)

    # 두 선분이 일직선 상에 있을 경우
    if ab == 0 and cd == 0:
        # 대소 비교를 위해 점들의 위치를 변경
        mx1, my1 = min(_x1, _x2), min(_y1, _y2)
        mx2, my2 = max(_x1, _x2), max(_y1, _y2)

        mx3, my3 = min(_x3, _x4), min(_y3, _y4)
        mx4, my4 = max(_x3, _x4), max(_y3, _y4)
        # (x2, y2) >= (x3, y3) and (x4, y4) >= (x1, y1)인 경우에만 교차
        if mx4 >= mx1 and my4 >= my1 and mx2 >= mx3 and my2 >= my3:
            return True
        return False

    return ab <= 0 and cd <= 0
    