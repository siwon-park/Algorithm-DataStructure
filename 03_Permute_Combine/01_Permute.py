# 순열
arr = [1, 2, 3]
N = len(arr)

# 방법 1) 백트랙킹 - 방문(사용)여부 체크(비트마스킹으로도 가능)
visited = [False] * N
ret = []


def permute(k, lst):
    if k == N:
        ret.append(lst[:])
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            lst.append(arr[i])
            permute(k + 1, lst)
            lst.pop()
            visited[i] = False


permute(0, [])
print(ret) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]


# 방법 2) 백트랙킹 - 자리 변경
ret2 = []
def permute2(k):
    if k == N:
        ret2.append(arr[:])
        return
    for i in range(k, N): # 일단 처음에는 자기 자신과 자리를 바꾸게 됨을 유의
        arr[i], arr[k] = arr[k], arr[i]
        permute2(k + 1)
        arr[i], arr[k] = arr[k], arr[i]


permute2(0)
print(ret2) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
