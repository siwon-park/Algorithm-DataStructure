# upperBound 구현(bisectright)
# 배열에 어떤 요소를 집어 넣을 때, 넣을 수 있는 가장 오른쪽의 위치

# Java에서 LIS를 구하기 위해 upperBound 구현 시에는 LIS의 길이를 매개 변수로 넣어줄 것
def uppper_bound(arr: list, target: int) -> int:
    n = len(arr)
    s, e = 0, n - 1
    idx = n  # 이분탐색으로 arr에 target이 들어갈 자리가 안 나오면 맨 마지막에 넣어야 하므로 n
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] > target: # arr[mid]가 target보다 큰 가장 작은 인덱스인 mid를 찾음
            e = mid - 1
            idx = mid
        else:
            s = mid + 1
    return idx


arr = [1, 2, 2, 2, 3, 4, 5]
print(uppper_bound(arr, 5)) # 7
print(uppper_bound(arr, 3)) # 5
print(uppper_bound(arr, 0)) # 0

