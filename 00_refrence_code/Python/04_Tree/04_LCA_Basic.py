# 최소 공통 조상 알고리즘(기본)
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline


# 루트에서 시작해서 깊이 탐색하기 위한 dfs
def dfs(cur: int, d: int) -> None:
    visited[cur] = True
    depth[cur] = d
    for nxt in graph[cur]:
        if not visited[nxt]:
            parent[nxt] = cur
            dfs(cur, d + 1)


# 최소 공통 조상을 찾는 알고리즘
def lca(a: int, b: int) -> int:
    while depth[a] != depth[b]:  # 두 노드의 깊이가 다른 동안
        # 노드를 올라가며 깊이를 같게 맞춤
        if depth[a] < depth[b]:
            b = parent[b]
        else:
            a = parent[a]
    # 깊이가 같아졌으면
    while a != b:  # 부모가 같지 않은 동안
        a = parent[a]
        b = parent[b]
    return a


N = int(input())  # 트리의 노드 수

graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

parent = [i for i in range(1,  + 1)]  # 부모 배열
visited = [False] * (N + 1)
depth = [0] * (N + 1)  # 깊이 배열

dfs(1, 0)

print(lca(15, 28))
