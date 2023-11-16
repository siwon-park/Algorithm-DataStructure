# 버블 정렬
"""
인접한 두 원소를 계속 비교해가면서 정렬함.
각 패스에서 가장 큰 원소가 맨 뒤로 이동하는 방식으로 정렬됨.
"""


def bubble_sort(arr: list):
    N = len(arr)
    for i in range(N - 1, 0, -1):  # 패스를 N번 반복함
        for j in range(i):  # 각 패스별로 가장 큰 원소를 뒤로 보내는 것을 반복
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [10, 2, 3, 5, 2, 11, 12, 11, 10, 15, 10, 4, 6]
bubble_sort(arr)
print(arr)
