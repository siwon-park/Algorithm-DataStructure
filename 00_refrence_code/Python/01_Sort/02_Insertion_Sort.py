# 삽입 정렬
"""
앞은 정렬되어 있다고 가정하고
매 순간 비교를 통해 정렬되지 않은 원소를 적절한 위치로 삽입하는 방식으로 구현됨
정렬된 부분이 있고, 정렬되지 않은 부분에서 작은 숫자를 앞으로 가져오는 방식임
"""


def insertion_sort(arr: list):
    N = len(arr)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]


arr = [10, 2, 3, 5, 2, 11, 12, 11, 10, 15, 10, 4, 6]
insertion_sort(arr)
print(arr)