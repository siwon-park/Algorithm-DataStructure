# 선택 정렬
"""
배열을 순회하면서 최솟값(또는 최댓값)인 원소의 인덱스를 찾아
정렬된 부분의 맨 앞에 배치하는 방식으로 동작
"""


def selection_sort(arr: list):
    N = len(arr)
    for i in range(N):
        min_idx = i
        for j in range(i + 1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [10, 2, 3, 5, 2, 11, 12, 11, 10, 15, 10, 4, 6]
selection_sort(arr)
print(arr)
