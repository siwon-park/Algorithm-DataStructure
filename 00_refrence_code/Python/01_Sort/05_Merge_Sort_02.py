# 병합 정렬(리스트 형태 반환)
def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    mid = n // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0
    l, r = len(left), len(right)
    while i < l and j < r:
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

arr = [69, 10, 30, 2, 16, 8, 31, 22, 2]
arr = merge_sort(arr)
print(arr)
