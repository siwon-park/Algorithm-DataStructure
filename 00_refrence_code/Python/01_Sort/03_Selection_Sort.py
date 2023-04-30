# 선택 정렬
def selection_sort(arr):
    N = len(arr)
    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [10, 2, 3, 5, 2, 11, 12, 11, 10, 15, 10, 4, 6]
selection_sort(arr)
print(arr)