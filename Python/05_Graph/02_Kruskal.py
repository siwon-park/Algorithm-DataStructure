# 크루스칼 알고리즘
import sys
input = sys.stdin.readline

V, E = map(int, input().split())

edges = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

parent =[i for i in range(V+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a, b = find_parent(parent, a), find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
cnt = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        cnt += 1
        if cnt == V - 1:
            break

print(result)