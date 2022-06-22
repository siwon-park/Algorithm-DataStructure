# 삽입 정렬
def insertion_sort(arr):
    N = len(arr)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

arr = [10, 2, 3, 5, 2, 11, 12, 11, 10, 15, 10, 4, 6]
insertion_sort(arr)
print(arr)