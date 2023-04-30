# 다익스트라 알고리즘
import sys, heapq
input = sys.stdin.readline

INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    # graph[b].append((a, cost)) # 무방향성 그래프일 경우(아닐 경우 삭제)

s, e = map(int, input().split())

# 최단거리 구하기(최단 거리 역행, 도착 지점을 알고 있을 경우)
# 혹, 최단거리 나온 값의 인덱스가 도착지점이므로 그 값을 활용
p = [0] * (N + 1)
path = [e]

def dijkstra(s, e):
    q = []
    heapq.heappush(q, (0, s)) # 거리, 시작점
    distance = [INF] * (N + 1)
    distance[s] = 0
    while q:
        d, cur = heapq.heappop(q)
        if distance[cur] < d:
            continue
        for nxt, cost in graph[cur]:
            nxt_cost = d + cost
            if nxt_cost < distance[nxt]:
                distance[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))
                p[nxt] = cur # cur 이후에 nxt로 갔다(nxt의 부모는 cur)

    return distance

dist = dijkstra(s, e)

end = e
while p[end]:
    path.append(p[end])
    end = p[end]

print(dist[e])
# print(len(path))
print(*path[::-1]) # 경로 역행이므로 뒤집어서 출력함