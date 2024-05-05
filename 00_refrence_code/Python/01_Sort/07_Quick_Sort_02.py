# 퀵 정렬(Pythonic)
def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [num for num in arr[1:] if num < pivot]
    right = [num for num in arr[1:] if num >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
