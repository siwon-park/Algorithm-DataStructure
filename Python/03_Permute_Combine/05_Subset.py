# 부분 집합 구하기 (재귀 호출)
arr = [1, 2, 3]
N = len(arr)

ret = []  # 집합 모음


def subset(k, lst):
    if k == N:
        ret.append(lst)
        return
    # 현재 값을 선택하지 않음
    subset(k + 1, lst)
    # 현재 값을 선택함
    subset(k + 1, lst + [arr[k]])


subset(0, [])
print(ret)  # [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
