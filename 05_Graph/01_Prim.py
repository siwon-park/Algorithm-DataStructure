# 프림 알고리즘(다익스트라 알고리즘과 매우 유사함)
import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [False]*(V+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  
    graph[b].append((a, c))

INF = int(1e9)
def Prim(start):
    distance = [INF] * (V+1)
    # 0번 노드에서부터 출발함
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start)) # 비용(c)를 기준으로 우선순위 큐 활용
    total_cost = 0
    while pq:
        cost, cur = heapq.heappop(pq)
        if visited[cur]:
            continue
        visited[cur] = True
        total_cost += cost
        for nxt, nxt_cost in graph[cur]:
            if not visited[nxt] and nxt_cost < distance[nxt]:
                distance[nxt] = nxt_cost
                heapq.heappush(pq, (nxt_cost, nxt))
    return total_cost

print(Prim(1))