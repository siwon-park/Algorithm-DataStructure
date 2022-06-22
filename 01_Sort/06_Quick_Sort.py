# 퀵 정렬
def quick_sort(s, e):
    if s >= e:
        return
    pvt = s
    left, right = s+1, e
    while left <= right:
        while left <= e and arr[pvt] >= arr[left]:
            left += 1
        while arr[pvt] < arr[right]:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[pvt], arr[right] = arr[right], arr[pvt]
    # 현재 피벗을 기준으로 왼쪽 영역과 오른쪽 영역을 나누므로 right-1, right+1
    quick_sort(s, right-1)
    quick_sort(right+1, e)

arr = [10, 2, 3, 5, 2, 11, 12, 11, 10, 15, 10, 4, 6]
# arr = [16, 15, 17, 8, 19]
quick_sort(0, len(arr)-1)
print(arr)