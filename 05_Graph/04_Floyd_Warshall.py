# 플로이드-워셜 알고리즘
import sys
input = sys.stdin.readline

# N = int(input())
# M = int(input())
N, M = map(int, input().split())
INF = sys.maxsize
graph = [[INF]*(N+1) for _ in range(N+1)]
path = [[0]*(N+1) for _ in range(N+1)] # 경로 추적을 위한 배열

for _ in range(M):
    a, b, cost = map(int, input().split())
    # if graph[a][b] > cost:
    graph[a][b] = cost
    # graph[b][a] = cost # 무방향 그래프일 경우(단방향일 경우 삭제)

for i in range(1, N+1):
    graph[i][i] = 0 # 자기자신으로 가는 길은 0으로 초기화

def Floyd():
    for k in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                cost = graph[a][k] + graph[k][b]
                if cost < graph[a][b]:
                    graph[a][b] = cost
                    path[a][b] = k # a -> b로 가는데 k를 경유해서 갔다

# 경로 찾는 함수
def find_path(s, e):
    if not path[s][e]:
        return []
    w = path[s][e]
    return find_path(s, w) + [w] + find_path(w, e)

Floyd()
for lst in graph:
    print(*lst)

print([1] + find_path(1, N) + [N])

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i == j:
#             print(0)
#         else:
#             route = [i] + find_path(i, j) + [j]
#             print(len(route), *route)
