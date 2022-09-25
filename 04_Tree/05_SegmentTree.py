# 세그먼트 트리 구현
import math

class SegmentTree:

    tree = None

    # 생성자
    def __init__(self, n):
        h = math.ceil(math.log(n, 2)) + 1
        node = round(math.pow(2, h)) # -1
        self.tree = [0] * node

    # 세그먼트 트리에 값을 삽입
    def insert(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return self.tree[node]
        else:
            mid = (start + end) // 2
            self.tree[node] = self.insert(arr, node * 2, start, mid) + self.insert(arr, node * 2 + 1, mid + 1, end)
            return self.tree[node]

    # 세그먼트 트리의 구간 합(구현 여부에 따라 곱, 나눗셈 등)을 반환
    def sum(self, node, left, right, start, end):
        if right < start or end < left:
            return 0
        elif left <= start and end <= right:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            return self.sum(node * 2, left, right, start, mid) + self.sum(node * 2 + 1, left, right, mid + 1, end)

    # 세그먼트 트리의 값을 업데이트
    def update(self, node, start, end, index, value):
        if index < start or end < index:
            return self.tree[node]
        elif index == start and end == index:
            self.tree[node] = value
            return self.tree[node]
        else:
            mid = (start + end) // 2
            self.tree[node] = self.update(node * 2, start, mid, index, value) + self.update(node * 2 + 1, mid + 1, end, index, value)
            return self.tree[node]


# 예시
N, M, K = map(int, input().split())

arr = [0]
for _ in range(N):
    arr.append(int(input().rstrip()))

segmentTree = SegmentTree(N)
segmentTree.insert(arr, 1, 1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        segmentTree.update(1, 1, N, b, c)
    else:
        ret = segmentTree.sum(1, b, c, 1, N)
        print(ret)

# print(math.ceil(math.log(5, 2)))