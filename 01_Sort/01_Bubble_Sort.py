# 버블 정렬
def bubble_sort(arr):
    N = len(arr)
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [10, 2, 3, 5, 2, 11, 12, 11, 10, 15, 10, 4, 6]
bubble_sort(arr)
print(arr)