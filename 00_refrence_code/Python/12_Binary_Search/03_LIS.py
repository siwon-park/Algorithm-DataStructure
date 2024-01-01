# 03_LIS (Longest Increasing Subsequence); 최장 증가 부분 수열

lst = [10, 20, 10, 30, 20, 50]
lis = [lst[0]]


def lower_bound(arr: list, target: int) -> int:
    s = 0
    idx = len(arr)
    e = idx - 1
    while s <= e:
        mid = (s + e) >> 1
        if arr[mid] >= target:
            e = mid - 1
            idx = mid
        else:
            s = mid + 1
    return idx


for i in range(1, len(lst)):
    if lst[i] > lis[-1]:
        lis.append(lst[i])
    else:
        _idx = lower_bound(lis, lst[i])
        lis[_idx] = lst[i]

print(lis)  # 10, 20, 30, 50
print(len(lis))  # 4
