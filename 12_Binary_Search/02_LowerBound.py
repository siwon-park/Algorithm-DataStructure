# lowerBound 구현(bisectleft)
# 배열에 어떤 요소를 집어 넣을 때, 넣을 수 있는 가장 왼쪽 위치


def lower_bound(arr: list, target: int) -> int:
    n = len(arr)
    s, e = 0, n - 1
    idx = n # 이분탐색으로 arr에 target이 들어갈 자리가 안 나오면 맨 마지막에 넣어야 하므로 n
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] >= target: # arr[mid]가 target보다 큰 가장 작은 인덱스인 mid를 찾음
            e = mid - 1
            idx = mid
        else:
            s = mid + 1
    return idx


arr = [1, 2, 2, 2, 3, 4, 5]
print(lower_bound(arr, 2)) # 1
print(lower_bound(arr, 5)) # 6
print(lower_bound(arr, 0)) # 0
